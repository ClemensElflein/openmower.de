FROM docker.io/klakegg/hugo:0.111.3-ext-ubuntu

EXPOSE 1313/tcp

ENTRYPOINT ["/bin/bash", "-c", "mkdir -p /tmp/.npm && chown -R 1000:1000 /tmp/.npm && npm install --no-bin-links && hugo server --poll 1s"]
