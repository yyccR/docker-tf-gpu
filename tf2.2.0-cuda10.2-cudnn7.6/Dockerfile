#FROM nvidia/cuda:10.2-cudnn7-runtime-ubuntu18.04
FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

# base requirements
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get autoclean && apt-get install -y \
    python3-pip \
    python3 \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    python-skimage \
    vim \
    language-pack-zh-hans \


&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade "pip < 21.0"
# model requirements
RUN pip3 install --no-cache-dir tensorflow-gpu==2.2.0
