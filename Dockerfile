# Stage 1: build
FROM node:16-bullseye AS builder

ARG HUGO_VERSION=0.111.3
ARG BASE_URL=https://openmower.de/latest/
ARG VERSION=latest

RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL \
    "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
    | tar -xz -C /usr/local/bin hugo

WORKDIR /site
COPY . .

RUN npm install

RUN scripts/gen-doc-versions.sh 2>/dev/null \
 || echo '# no git tags found — version selector disabled' \
    > config/_generated_versions.toml

RUN printf 'baseURL = "%s"\n[params]\nversion = "%s"\n' "${BASE_URL}" "${VERSION}" \
    > config/_build_override.toml

RUN hugo --minify \
    --config config.toml,config/_generated_versions.toml,config/_build_override.toml

# Stage 2: export — scratch layer holds only the built site
FROM scratch
COPY --from=builder /site/public /
