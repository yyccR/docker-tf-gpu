#FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04
FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

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
#RUN pip install --no-cache-dir jupyter notebook
# model requirements
RUN pip3 install --no-cache-dir tensorflow-gpu==2.2.0


# copy project files
#COPY libcudnn7_7.6.5.32-1+cuda10.1_amd64.deb /data/gpu/tf2.2.0-cuda10.1-cudnn7.6/libcudnn7_7.6.5.32-1+cuda10.1_amd64.deb
#RUN  dpkg -i /data/gpu/tf2.2.0-cuda10.1-cudnn7.6/libcudnn7_7.6.5.32-1+cuda10.1_amd64.deb

#CMD ["jupyter", "notebook", "--allow-root", "--port 8888", "--ip 0.0.0.0"]
