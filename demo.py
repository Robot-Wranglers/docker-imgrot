"""
# Usage:
#  Change main function with ideal arguments
#  then
#  python demo.py [name of the image] [degree to rotate] ([ideal width] [ideal height])
#  e.g.,
#  python demo.py img/000001.jpg 360
#  python demo.py img/000001.jpg 45 500 700
#
# Parameters:
#  img_path  : path of image that you want rotated
#  shape     : ideal shape of input image, None for original size.
#  theta     : rotation around the x axis
#  phi       : rotation around the y axis
#  gamma     : rotation around the z axis (basically a 2D rotation)
#  dx        : translation along the x axis
#  dy        : translation along the y axis
#  dz        : translation along the z axis (distance to the image)
"""

import os
import sys
import logging
import subprocess

import click

from util import save_image
from image_transformer import ImageTransformer

# Read log level from environment variable
log_level = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - imgrot - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@click.command()
@click.option("--range", "rot_range", default="360", help="Range to rotate through")
@click.option(
    "--stream/--no-stream",
    default=False,
    help="Stream output in raw format (for use with pipes).  Implies --animate",
)
# @click.option(
#     "--animate/--no-animate",
#     default=False,
#     help="Generate an animated gif.  (Not required for --display)",
# )
@click.option("--display/--no-display", default=False, help="Display output with chafa")
@click.option(
    "--view/--no-view",
    default=False,
    help="View a file with chafa (don't generate anything)",
)
@click.option("--output-dir", default="/tmp/imgrot", help="Output directory for frames")
@click.option(
    "--output-file", default="/tmp/imgrot.gif", help="Output file for animated gif"
)
@click.option(
    "--img-shape", default=None, help="Ideal image shape in WxH format (optional)"
)
# @click.option(
#     "--loop",
#     default="1",
#     help="How many times to loop the animation.  (Use 0 for forever)",
# )
# @click.option(
#     "--background", default="1", help="Background color (passed forward to 'convert')"
# )
@click.argument("img_path", required=True)
def run(
    img_path: str,
    # animate: bool = False,
    display: bool = False,
    img_shape=None,
    output_dir: str = "/tmp",
    # background: str = "black",
    # loop: str = "1",
    output_file: str = "/tmp/imgrot.gif",
    rot_range: str = "360",
    stream: bool = False,
    view: bool = False,
):
    if not os.path.exists(img_path):
        logger.debug(f"{img_path} does not exist!")
        raise SystemExit(1)
    rot_range = int(rot_range)
    img_shape = img_shape and list(map(int, img_shape.split("x")))
    # animate = animate or stream
    # rotate = not view
    # if rotate:
    it = ImageTransformer(img_path, img_shape)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    logger.debug(f"Rotating {img_path} .. ")

    # yz-axis from 0 to 360 degree
    # rotargs=dict(phi = ang, gamma=ang)
    # z-axis(Normal 2D) from 0 to 360 degree
    # rotargs=dict(gamma=ang)
    # y-axis from 0-360 degree, 5 pixel shift in +X
    for ang in range(0, rot_range):
        rotargs = dict(phi=ang, dx=5)
        rotated_img = it.rotate_along_axis(**rotargs)
        save_image(f"{output_dir}/{str(ang).zfill(3)}.png", rotated_img)
    logger.debug("Done")

    command = f"ls {output_dir}/|wc -l"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        logger.debug(f"Command failed with return code {result.returncode}\n")
        raise SystemExit(result.returncode)
    else:
        logger.debug("Total Frames: {result.stdout.strip()}")
    # if animate:
    logger.debug("Animating..")
    # command = f"convert -background {background} -alpha remove -alpha off -delay .01 -loop {loop} {output_dir}/*.png {output_file}"
    command = f"ffmpeg -y -framerate 140  -pattern_type glob -i '{output_dir}/*.png' -vf 'fps=60,scale=320:-1:flags=lanczos' {output_file} 2>/dev/null"
    result = subprocess.run(command, shell=True, stdout=sys.stderr, stderr=sys.stderr)
    if result.returncode != 0:
        logger.debug(f"Command failed with return code {result.returncode}")
        raise SystemExit(result.returncode)

    if view:
        logger.debug(f"Viewing {img_path}")
        os.system(f"chafa --duration=5 {img_path}")
    elif display:
        # if animate:
        logger.debug("Displaying animated gif..")
        os.system(f"chafa --symbols 'braille' {output_file}")
        # else:
        #     logger.debug("Displaying framewise..")
        #     os.system(f"chafa --clear --symbols braille --duration .05 {output_dir}/*png")
    elif stream:
        logger.debug("Streaming animation..")
        with open(output_file, "rb") as binary_file:
            content = binary_file.read()
            sys.stdout.buffer.write(content)
    else:
        logger.debug("No instructions, not sure what to do")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
