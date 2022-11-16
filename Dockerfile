FROM klakegg/hugo:ext-ubuntu

RUN apt-get update
# Get git in order to do last-updated etc
RUN apt-get install -y git && \
  git config --global --add safe.directory /src

# Get NPM im order to do the npm_install
RUN apt-get install -y npm
