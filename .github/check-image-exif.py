#!/usr/bin/env python3
"""Reject EXIF in tracked images; optionally limit the scan to a PR diff."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


# Content detection also finds images with missing or misleading extensions.
# Extensions make unreadable image files fail instead of silently being skipped.
IMAGE_EXTENSIONS = {
    '.avif', '.bmp', '.cr2', '.cr3', '.dng', '.gif', '.heic', '.heif', '.ico',
    '.j2c', '.j2k', '.jfif', '.jp2', '.jpe', '.jpeg', '.jpg', '.jxl', '.nef',
    '.orf', '.pbm', '.pcx', '.pef', '.pgm', '.png', '.pnm', '.ppm', '.psd',
    '.raf', '.raw', '.rw2', '.srw', '.svg', '.tga', '.tif', '.tiff', '.webp',
    '.xcf',
}


def git(*args):
    return subprocess.check_output(['git', *args])


def report_error(message):
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        escaped = message.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
        print(f'::error::{escaped}')
    else:
        print(f'ERROR: {message}', file=sys.stderr)


def tracked_paths(base):
    if base:
        # A three-dot diff includes only changes introduced by this branch.
        # Disabling rename detection also checks the destination of copies/renames.
        output = git('diff', '--name-only', '-z', '--diff-filter=ACMT',
                     '--no-renames', f'{base}...HEAD', '--')
    else:
        output = git('ls-files', '-z')
    return [os.fsdecode(path) for path in output.split(b'\0') if path]


def scan(paths):
    images = 0
    affected = []
    errors = []
    for start in range(0, len(paths), 100):
        batch = paths[start:start + 100]
        result = subprocess.run(
            ['exiftool', '-json', '-G0', '-u', '-EXIF', '-EXIF:all',
             '-MIMEType', '-Error', '-Warning', '--',
             *['./' + path for path in batch]],
            capture_output=True, text=True,
        )
        # Unsupported non-image files cause exit 1 too; inspect each record.
        if result.returncode not in (0, 1):
            raise RuntimeError(f'ExifTool exited with status {result.returncode}')
        records = json.loads(result.stdout)
        if {r['SourceFile'] for r in records} != {'./' + p for p in batch}:
            raise RuntimeError('ExifTool did not return a result for every file')
        for record in records:
            path = record['SourceFile'][2:]
            tags = sorted(key[5:] for key in record if key.startswith('EXIF:'))
            is_image = (record.get('File:MIMEType', '').startswith('image/')
                        or Path(path).suffix.lower() in IMAGE_EXTENSIONS
                        or bool(tags))
            images += int(is_image)
            error = record.get('ExifTool:Error')
            if error and (is_image or error not in ('Unknown file type', 'File is empty')):
                errors.append(f'{path!r}: could not inspect file ({error})')
            if (Path(path).suffix.lower() in IMAGE_EXTENSIONS and not error
                    and not record.get('File:MIMEType', '').startswith('image/')):
                errors.append(f'{path!r}: could not inspect as an image (unrecognized image data)')
            warning = record.get('ExifTool:Warning')
            if is_image and warning and not warning.startswith('[minor]'):
                errors.append(f'{path!r}: incomplete metadata scan ({warning})')
            if tags:
                # Never include metadata values (in particular GPS coordinates).
                affected.append({'path': path, 'tags': tags})
    return images, affected, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='compare HEAD to the merge base with this Git ref')
    parser.add_argument('--report', type=Path, help='write audit JSON containing tag names only')
    args = parser.parse_args()
    report_path = args.report.resolve() if args.report else None
    try:
        os.chdir(os.fsdecode(git('rev-parse', '--show-toplevel')).strip())
        paths = tracked_paths(args.base)
        # Git symlinks contain a link target, not image bytes. Never follow them.
        paths = [path for path in paths if not Path(path).is_symlink()]
        if not paths:
            print('No added or modified files to check.')
            return 0
        if not shutil.which('exiftool'):
            raise RuntimeError('ExifTool is required; install libimage-exiftool-perl (Ubuntu) or exiftool (Homebrew)')
        images, affected, errors = scan(paths)
        if report_path:
            report_path.write_text(json.dumps({
                'commit': git('rev-parse', 'HEAD').decode().strip(),
                'scanned_files': len(paths),
                'images': images,
                'affected': affected,
                'errors': errors,
            }, indent=2) + '\n')
        for item in affected:
            tags = ', '.join(tag for tag in item['tags'] if tag != 'EXIF') or 'EXIF block'
            report_error(f"{item['path']!r}: contains EXIF ({tags})")
        for error in errors:
            report_error(error)
        print(f'Checked {images} images in {len(paths)} files: '
              f'{len(affected)} with EXIF, {len(errors)} scan errors.')
        if affected:
            print('Remove EXIF before committing, for example: exiftool -EXIF:all= path/to/image.jpg')
        return 1 if affected or errors else 0
    except (OSError, subprocess.CalledProcessError, ValueError, KeyError, RuntimeError) as error:
        report_error(f'EXIF check failed: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
