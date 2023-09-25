<p align="center">
  <a>
    <h1 align="center">openmower.de</h1>
    <img align="center" src="./.img/open_mower_header.jpg">
  </a>
</p>
<br>
<p align="center">
  This is the source code for the <a href="https://github.com/ClemensElflein/openmower.de">openmower.de</a> website.
</p>

<br>
<hr>
<br>

<p align="center">
  If you find some issues with the documentation or want to add to it, please fork this repo and open a pull request.<br>It's a good idea to tell us that you are working on some part of the website. This maximises the chance, that your changes will be merged to the website.
</p>

<br>
<hr>
<br>

<ul>
<li><a href="#openmoweros">Running the website on OpenMowerOS <i>(Very easy)</i></a></li>
  <li><a href="#running-local">Running the website locally...</a></li>
  <ul>
    <li><a href="#running-local-hugo">on Bare Metal</a></li>
    <li><a href="#running-local-container">on Podman/Docker</a></li>
    <li><a href="#running-local-docker-compose">on Docker Compose</a></li>
  </ul>
<li><!--<a href="#github-pages">-->Running the website on github pages <i>(To be written)</i><!--</a>--></li>
<br>
<li><a href="#troubleshooting">Troubleshooting...</a></li>
</ul>

<br>
<hr>
<br>

<h2 id="openmoweros">
  Running the website on OpenMowerOS
</h2>

Since [OpenMowerOS](https://github.com/ClemensElflein/OpenMowerOS) already ships with the container engine [Podman](https://podman.io/) it is very easy to use deploy a container here.

- ssh as the openmower user into your mower and then clone this repo: 
  ```sh
  cd ~/
  git clone --depth=1 https://github.com/ClemensElflein/openmower.de
  cd ~/openmower.de/
  ```

- Build the container:
  ```sh
  podman build -t openmower.de .
  ```

- Now make your changes to the files and then start the container.
  ```sh
  podman run --detach --name openmower.de --publish 1313:1313 --volume ./:/src/ openmower.de
  ```

- Be patient while the container installs all dependencies and builds the website. 🍵 \
  You can check its logs by
  ```sh
  podman logs -f openmower.de
  ```

  <br>
  <details><summary>A successfull start may looks like this - <i>(Click to expand)</i></summary>

  ```
  > tech-doc-hugo@0.0.1 prepare
  > npm run _prepare:docsy


  > tech-doc-hugo@0.0.1 _prepare:docsy
  > cd themes/docsy && npm install --no-bin-links


  changed 4 packages, and audited 180 packages in 18s

  42 packages are looking for funding
    run `npm fund` for details

  found 0 vulnerabilities

  changed 5 packages, and audited 75 packages in 21s

  19 packages are looking for funding
    run `npm fund` for details

  found 0 vulnerabilities
  npm notice
  npm notice New major version of npm available! 9.6.6 -> 10.2.0
  npm notice Changelog: https://github.com/npm/cli/releases/tag/v10.2.0
  npm notice Run npm install -g npm@10.2.0 to update!
  npm notice
  Start building sites …
  hugo v0.111.3-5d4eb5154e1fed125ca8e9b5a0315c4180dab192+extended linux/amd64 BuildDate=2023-03-12T11:40:50Z VendorInfo=hugoguru

                     | EN
  -------------------+------
    Pages            | 134
    Paginator pages  |   0
    Non-page files   |  52
    Static files     | 100
    Processed images | 149
    Aliases          |   0
    Sitemaps         |   1
    Cleaned          |   0

  Built in 11309 ms
  Watching for changes in /src/{assets,content,layouts,package.json,static,themes}
  Use watcher with poll interval 1s
  Watching for config changes in /src/config.toml, /src/themes/docsy/config.yaml
  Environment: "DEV"
  Serving pages from memory
  Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
  Web Server is available at //localhost:1313/ (bind address 0.0.0.0)
  Press Ctrl+C to stop
  ```
  </details>
  <br>

  If you see the following lines the container successfully build the website and you can access it on port `1313` of you mower ([openmower.local:1313](http://openmower.local:1313))
  ```
  Web Server is available at //localhost:1313/ (bind address 0.0.0.0)
  Press Ctrl+C to stop
  ```

<br>

> [!TIP]
> You can now make your changes on the fly - the container watches the source and will rebuild individual sites automatically on changes.

If for some circumstances it does not rebuild you can try to restart the container:
```sh
podman restart openmower.de
```

<br>
<hr>
<br>

Once you are done you can stop the container
```sh
podman stop openmower.de
```

If you do not plan to edit the site once more you can remove the container and the images.
```sh
podman rm openmower.de
podman rmi openmower.de docker.io/klakegg/hugo:0.111.3-ext-ubuntu
```



<br>
<hr>
<br>

<h2 id="running-local">
  Running the website locally...
</h2>

<br>

<h3 id="running-local-hugo">
  Running the website locally on Bare Metal
</h3>

Building and running the site locally requires a recent `extended` version of [Hugo](https://gohugo.io). \
You can find out more about how to install Hugo for your environment in our
[Getting started](https://www.docsy.dev/docs/getting-started/#prerequisites-and-installation) guide.

Once you've made your working copy of the site repo, from the repo root folder, run:
```sh
hugo server
```

<br>

<h3 id="running-local-container">
  Running the website locally on Podman/Docker
</h3>

_to be writen..._


<br>

<h3 id="running-local-docker-compose">
  Running the website locally on Docker Compose
</h3>

You can run openmower.de inside a container _([Docker](https://docs.docker.com/) or [Podman](https://podman.io/))_, the container runs with a volume bound to the `docsy-example` folder. This approach doesn't require you to install any dependencies other than [Docker Desktop](https://www.docker.com/products/docker-desktop) on Windows and Mac, and [Docker Compose](https://docs.docker.com/compose/install/) on Linux.

- Build the docker image
   ```sh
   docker compose build
   ```

- Run the built image
   ```sh
   docker compose up
   ```
> [!TIP]
> You can run both commands at once with `docker compose up --build`.

- Verify that the service is working.

   Open your web browser and type `http://localhost:1313` in your navigation bar,
   This opens a local instance of the openmower.de homepage. You can now make
   changes to the website and those changes will immediately show up in your
   browser after you save (not on Windows though. Hot reload only works on the non-dockerized hugo!).

### Cleanup

To stop Docker Compose, on your terminal window, press <kbd>Ctrl</kbd>+<kbd>C</kbd>.

To remove the produced images run:
```sh
docker compose rm
```
For more information see the [Docker Compose documentation](https://docs.docker.com/compose/gettingstarted/).

<br>
<hr>
<br>

<h2 id="troubleshooting">
  Troubleshooting
</h2>

As you run the website locally, you may run into the following error:
```
➜ hugo server

INFO 2021/01/21 21:07:55 Using config file: 
Building sites … INFO 2021/01/21 21:07:55 syncing static files to /
Built in 288 ms
Error: Error building site: TOCSS: failed to transform "scss/main.scss" (text/x-scss): resource "scss/scss/main.scss_9fadf33d895a46083cdd64396b57ef68" not found in file cache
```

This error occurs if you have not installed the extended version of Hugo.
See this [section](https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/#install-hugo) of the user guide for instructions on how to install Hugo.

Or you may encounter the following error:
```
➜ hugo server

Error: failed to download modules: binary with name "go" not found
```

This error occurs if you have not installed the `go` programming language on your system.
See this [section](https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/#install-go-language) of the user guide for instructions on how to install `go`.
