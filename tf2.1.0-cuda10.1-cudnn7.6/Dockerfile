FROM nvidia/cuda:10.1-runtime-ubuntu16.04

# base requirements
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
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip

# model requirements
RUN pip3 install --no-cache-dir tensorflow-gpu==2.1.0


# copy project files
COPY libcudnn7_7.6.4.38-1+cuda10.1_amd64.deb /data/gpu/tf2.1.0-cuda10.1-cudnn7.6/libcudnn7_7.6.4.38-1+cuda10.1_amd64.deb
RUN  dpkg -i /data/gpu/tf2.1.0-cuda10.1-cudnn7.6/libcudnn7_7.6.4.38-1+cuda10.1_amd64.deb

