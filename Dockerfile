# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm
RUN apt-get update -qq && apt-get -qq -y install chafa imagemagick ffmpeg libsm6 libxext6 
WORKDIR /workspace
RUN mkdir /opt/imgrot 
COPY . /opt/imgrot
RUN pip3 install -r /opt/imgrot/requirements.txt --break-system-packages
ENTRYPOINT [ "python3", "/opt/imgrot/imgrot.py" ]
