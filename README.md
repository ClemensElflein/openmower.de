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


<h2 id="running-local-docker-compose">
  Running the website locally on Docker Compose
</h2>

You can run openmower.de inside a Docker container. This approach doesn't require you to install any dependencies other than [Docker Desktop](https://www.docker.com/products/docker-desktop) on Windows and Mac, and [Docker Compose](https://docs.docker.com/compose/install/) on Linux.


Run the following command to start the website:
```bash
docker compose up
```

Open your web browser and type `http://localhost:8080` in your navigation bar,
This opens a local instance of the openmower.de homepage. You can now make
changes to the website and those changes will immediately show up in your
browser after you save.

### Cleanup

To stop Docker Compose, on your terminal window, press <kbd>Ctrl</kbd>+<kbd>C</kbd>.

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

