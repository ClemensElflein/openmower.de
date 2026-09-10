#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');

const script = fs.readFileSync(path.join(__dirname, '../assets/js/language-preference.js'), 'utf8');
const key = 'openmower.language';

function visit(options = {}) {
    const storage = options.storage || new Map();
    const location = {
        href: options.url || 'https://openmower.de/',
        replace(href) { this.redirect = href; },
    };
    const window = {
        location,
        localStorage: {
            getItem(name) {
                if (options.storageBlocked) throw new Error('Storage disabled');
                return storage.get(name) || null;
            },
            setItem(name, value) {
                if (options.storageBlocked || options.storageFull) throw new Error('Cannot save');
                storage.set(name, value);
            },
        },
        history: {
            state: null,
            replaceState(state, title, href) { location.href = href; },
        },
    };
    vm.runInNewContext(script, {
        URL,
        window,
        navigator: {
            languages: options.languages === undefined ? ['en-US'] : options.languages,
            language: options.language || 'en-US',
        },
        document: { currentScript: { dataset: {
            pageLanguage: options.current || 'en',
            languageTargets: JSON.stringify(options.targets || { en: '/', de: '/de/' }),
        } } },
    });
    return { redirect: location.redirect, url: location.href, storage };
}

let cases = 0;
function check(name, test) {
    test();
    cases++;
    console.log(`Passed: ${name}`);
}

check('German regional preferences select German and settle without a redirect loop', () => {
    const first = visit({ languages: ['de-AT', 'en-US'] });
    assert.equal(first.redirect, 'https://openmower.de/de/');
    const second = visit({ url: first.redirect, current: 'de', storage: first.storage });
    assert.equal(second.redirect, undefined);
});
check('English first in the preference list wins', () => {
    assert.equal(visit({ languages: ['en-GB', 'de-DE'] }).redirect, undefined);
});
check('Skip unsupported languages to find the first supported preference', () => {
    assert.equal(visit({ languages: ['fr-FR', 'de-CH', 'en'] }).redirect, 'https://openmower.de/de/');
});
check('Unsupported browser languages fall back to English', () => {
    assert.equal(visit({ current: 'de', url: 'https://openmower.de/de/', languages: ['fr-FR'] }).redirect, 'https://openmower.de/');
});
check('Fall back to navigator.language when navigator.languages is empty or absent', () => {
    for (const languages of [[], null]) {
        assert.equal(visit({ languages, language: 'de-DE' }).redirect, 'https://openmower.de/de/');
    }
});
check('Saved manual choice wins over the browser language', () => {
    const storage = new Map([[key, 'en']]);
    assert.equal(visit({ storage, languages: ['de-DE'] }).redirect, undefined);
});
check('Menu choice replaces an earlier preference and removes only its own query parameter', () => {
    const storage = new Map([[key, 'de']]);
    const result = visit({ storage, url: 'https://openmower.de/?q=rtk&lang=en#build', languages: ['de'] });
    assert.equal(result.redirect, undefined);
    assert.equal(result.url, 'https://openmower.de/?q=rtk#build');
    assert.equal(visit({ storage, languages: ['de'] }).redirect, undefined);
});
check('No matching translation leaves the requested English page intact', () => {
    const storage = new Map([[key, 'de']]);
    const result = visit({ storage, url: 'https://openmower.de/latest/docs/english-only/', targets: { en: '/latest/docs/english-only/' } });
    assert.equal(result.redirect, undefined);
    assert.equal(storage.get(key), 'de');
});
check('Missing translation on first visit still retains the preferred language for other pages', () => {
    const first = visit({ targets: { en: '/' }, languages: ['de'] });
    assert.equal(first.redirect, undefined);
    assert.equal(visit({ storage: first.storage }).redirect, 'https://openmower.de/de/');
});
check('Documentation paths, query parameters, and fragments survive switching', () => {
    const result = visit({
        url: 'https://openmower.de/latest/docs/getting-started/?q=GPS#important-warnings',
        languages: ['de'],
        targets: { en: '/latest/docs/getting-started/', de: '/latest/de/docs/getting-started/' },
    });
    assert.equal(result.redirect, 'https://openmower.de/latest/de/docs/getting-started/?q=GPS#important-warnings');
});
check('Development prefixes and archive versions stay intact', () => {
    for (const prefix of ['/dev-prefix/', '/archive/v1.2.0/']) {
        assert.equal(visit({
            url: `http://localhost:1313${prefix}docs/`, languages: ['de'],
            targets: { en: `${prefix}docs/`, de: `${prefix}de/docs/` },
        }).redirect, `http://localhost:1313${prefix}de/docs/`);
    }
});
check('Invalid saved or query preferences are ignored', () => {
    const result = visit({ url: 'https://openmower.de/?lang=xx', languages: ['de'], storage: new Map([[key, 'xx']]) });
    assert.equal(result.redirect, 'https://openmower.de/de/?lang=xx');
});
check('Blocked or full storage preserves normal navigation and manual menu links', () => {
    for (const unavailable of [{ storageBlocked: true }, { storageFull: true }]) {
        assert.equal(visit({ ...unavailable, languages: ['de'] }).redirect, undefined);
        assert.equal(visit({ ...unavailable, languages: ['de'], url: 'https://openmower.de/?lang=en' }).redirect, undefined);
    }
});
check('Translation targets cannot send a visitor to another origin', () => {
    assert.equal(visit({ languages: ['de'], targets: { en: '/', de: 'https://example.com/de/' } }).redirect, undefined);
});

console.log(`Passed: ${cases} automatic language selection checks`);
