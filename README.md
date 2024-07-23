<p align=center>
<table width=100%>
  <tr>
    <td colspan=2><strong>
    imgrot
      </strong>&nbsp;&nbsp;&nbsp;&nbsp;
    </td>
  </tr>
  <tr>
    <td width=15%><img src=https://raw.githubusercontent.com/Robot-Wranglers/docker-imgrot/master/img/icon.png style="width:150px"></td>
    <td width=80% align=center>
    <center>
    Tool for creating 3D rotation gifs from 2D images<br/>
    <img align=center width=150px src=img/demo.gif>
    </center>
    </td>
  </tr>
</table>
</P>
<a href="https://hub.docker.com/r/robotwranglers/imgrot"><img src="https://img.shields.io/badge/dockerhub--blue.svg?logo=Docker"></a>

-------------------------------------

## Overview

A fork / update for the excellent original work at [eborboihuc/rotate_3d](https://github.com/eborboihuc/rotate_3d).

The original uses `opencv` to rotate 2d -> 3d.  This version adds better CLI parsing, support for python3, newer opencv, ability to animate and render animations with `ffmpeg`, and works via docker.

Besides creating gifs, it can display them inside a terminal, using [chafa](https://github.com/hpjansson/chafa).

See also [the original docs](docs/README.original.md)

-------------------------------------

## Installation

Nothing on pypi.  See [dockerhub](https://hub.docker.com/r/robotwranglers/imgrot) for available releases.

```
pip install -r requirements.txt
```

-------------------------------------

## Usage

**Basic usage info follows:**

```bash
Usage: demo.py [OPTIONS] IMG_PATH

Options:
  --range TEXT              Range to rotate through
  --stream / --no-stream    Stream output in raw format (for use with pipes).
                            Implies --animate
  --display / --no-display  Display output with chafa
  --view / --no-view        View a file with chafa (don't generate anything)
  --output-dir TEXT         Output directory for frames
  --output-file TEXT        Output file for animated gif
  --img-shape TEXT          Ideal image shape in WxH format (optional)
  --help                    Show this message and exit.

```

-------------------------------------

## Usage from Docker

**A few examples of usage from docker:**

```bash
# Saves the animated gif to a file. 
$ docker run -it --rm -v `pwd`:/workspace -w /workspace robotwranglers/imgrot img/icon.png --range 360 --img-shape 200x200  --stream > demo.gif
```

<p align=center>
<img width=25% align=center src=img/demo.gif>
</p>

```bash 
# Renders a gif from a static image, then displays it in a terminal-friendly way with chafa
$ docker run -it --rm -v `pwd`:/workspace -w /workspace robotwranglers/imgrot img/icon.png --range 360 --img-shape 200x200 --display
```

<p align=center>
<img width=50% align=center src=img/demo.chafa.gif>
</p>

