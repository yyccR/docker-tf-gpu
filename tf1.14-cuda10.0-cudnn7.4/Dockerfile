FROM nvidia/cuda:10.0-runtime-ubuntu16.04

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
RUN pip3 install --no-cache-dir tensorflow-gpu==1.14


# copy project files
COPY libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb /data/gpu/tf1.14-cuda10.0-cudnn7.4/libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb
RUN  dpkg -i /data/gpu/tf1.14-cuda10.0-cudnn7.4/libcudnn7_7.4.2.24-1+cuda10.0_amd64.deb

