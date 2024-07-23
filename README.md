<table width=100%>
  <tr>
    <td colspan=2><strong>
    imgrot
      </strong>&nbsp;&nbsp;&nbsp;&nbsp;
    </td>
  </tr>
  <tr>
    <td width=15%><img src=https://raw.githubusercontent.com/Robot-Wranglers/docker-imgrot/master/img/icon.png style="width:150px"></td>
    <td align=center>
    <center>
    Tool for creating 3D rotation gifs from 2D images
    </center>
    </td>
  </tr>
</table>
<a href="https://hub.docker.com/r/robotwranglers/imgrot"><img src="https://img.shields.io/badge/dockerhub--blue.svg?logo=Docker"></a>

-------------------------------------

## Overview

A fork / update for the excellent original work at [eborboihuc/rotate_3d](https://github.com/eborboihuc/rotate_3d).

This adds better CLI parsing, support for python3, newer opencv, and works via docker.

-------------------------------------

## Installation

See [dockerhub](https://hub.docker.com/r/robotwranglers/imgrot) for available releases.

```
pip install -r requirements.txt
```

-------------------------------------

## Usage

Usage info follows:

```bash
Usage: demo.py [OPTIONS] IMG_PATH

Options:
  --range TEXT              Range to rotate through
  --stream / --no-stream    Stream output in raw format (for use with pipes).
                            Implies --animate
  --animate / --no-animate  Generate an animated gif.  (Not required for
                            --display)
  --display / --no-display  Display output with chafa
  --view / --no-view        View a file with chafa (don't generate anything)
  --output-dir TEXT         Output directory for frames
  --output-file TEXT        Output file for animated gif
  --img-shape TEXT          Ideal image shape in WxH format (optional)
  --help                    Show this message and exit.

```

-------------------------------------

## Usage from Docker

If you want to build locally, see the [Dockerfile in this repo](Dockerfile) and use the [Makefile](Makefile):

```bash
$ make docker-build docker-test
```

If you don't want to build the container yourself, you can pull it like this:

```bash
$ docker pull robotwranglers/imgrot
Using default tag: latest
latest: Pulling from robotwranglers/imgrot
docker.io/robotwranglers/imgrot:latest
```

See a typical invocation below.  The 1st volume is for authenticating with SSM.  The 2nd volume shares the working directory with the container so commands using files (like `ssm put --file ./path/to/file /path/to/key`) can still work.

```bash
$ docker run \
  -v ~/.aws:/root/.aws \
  -v `pwd`:/workspace \
  -w /workspace \
  docker.io/robotwranglers/imgrot:latest \
    --help
```
