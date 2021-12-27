# docker tf gpu
> 项目环境的隔离和实例发布上线目前都是基于docker, tf直接宿主机环境会有很多限制和冲突, 下面列出了不同tf版本如何打包成一个可以使用gpu的docker镜像.

## tensorflow 版本要求细节
```python
https://tensorflow.google.cn/install/source#linux
```

| 版本                  | Python 版本  | 編譯器    | 建構工具     | cuDNN | CUDA |
| :-------------------- | :----------- | :-------- | :----------- | :---- | :--- |
| tensorflow-2.6.0      | 3.6-3.9      | GCC 7.3.1 | Bazel 3.7.2  | 8.1   | 11.2 |
| tensorflow-2.5.0      | 3.6-3.9      | GCC 7.3.1 | Bazel 3.7.2  | 8.1   | 11.2 |
| tensorflow-2.4.0      | 3.6-3.8      | GCC 7.3.1 | Bazel 3.1.0  | 8.0   | 11.0 |
| tensorflow-2.3.0      | 3.5-3.8      | GCC 7.3.1 | Bazel 3.1.0  | 7.6   | 10.1 |
| tensorflow-2.2.0      | 3.5-3.8      | GCC 7.3.1 | Bazel 2.0.0  | 7.6   | 10.1 |
| tensorflow-2.1.0      | 2.7、3.5-3.7 | GCC 7.3.1 | Bazel 0.27.1 | 7.6   | 10.1 |
| tensorflow-2.0.0      | 2.7、3.3-3.7 | GCC 7.3.1 | Bazel 0.26.1 | 7.4   | 10.0 |
| tensorflow_gpu-1.15.0 | 2.7、3.3-3.7 | GCC 7.3.1 | Bazel 0.26.1 | 7.4   | 10.0 |
| tensorflow_gpu-1.14.0 | 2.7、3.3-3.7 | GCC 4.8   | Bazel 0.24.1 | 7.4   | 10.0 |
| tensorflow_gpu-1.13.1 | 2.7、3.3-3.7 | GCC 4.8   | Bazel 0.19.2 | 7.4   | 10.0 |
| tensorflow_gpu-1.12.0 | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.15.0 | 7     | 9    |
| tensorflow_gpu-1.11.0 | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.15.0 | 7     | 9    |
| tensorflow_gpu-1.10.0 | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.15.0 | 7     | 9    |
| tensorflow_gpu-1.9.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.11.0 | 7     | 9    |
| tensorflow_gpu-1.8.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.10.0 | 7     | 9    |
| tensorflow_gpu-1.7.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.9.0  | 7     | 9    |
| tensorflow_gpu-1.6.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.9.0  | 7     | 9    |
| tensorflow_gpu-1.5.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.8.0  | 7     | 9    |
| tensorflow_gpu-1.4.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.5.4  | 6     | 8    |
| tensorflow_gpu-1.3.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.4.5  | 6     | 8    |
| tensorflow_gpu-1.2.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.4.5  | 5.1   | 8    |
| tensorflow_gpu-1.1.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.4.2  | 5.1   | 8    |
| tensorflow_gpu-1.0.0  | 2.7、3.3-3.6 | GCC 4.8   | Bazel 0.4.2  | 5.1   | 8    |


## 宿主机相关配置
```
0. 查看tensorflow版本对驱动,cuda, cudnn的版本要求: https://www.tensorflow.org/install/source#tested_build_configurations
1. 宿主机安装驱动, https://www.nvidia.com/Download/index.aspx?lang=en-us
2. 安装docker cuda toolkit, https://github.com/NVIDIA/nvidia-docker
   ubuntu16.04/18.04:
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
   curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
   curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
   sudo systemctl restart docker
```


## docker镜像构建
```python
cd docker-tf-gpu/tf2.2.0-cuda10.1-cudnn7.6

docker build -t tf/gpu_dev:tf2.2-cuda10.1-cudnn7.6 .

sudo docker run -it --gpus all --rm tf/gpu_dev:tf2.2-cuda10.1-cudnn7.6

sudo docker run -dti --gpus all  --name tf2.2-cuda10.1-cudnn7.6 tf/gpu_dev:tf2.2-cuda10.1-cudnn7.6
```

## 关于docker基础镜像的一点小tips
```python
需要nvcc环境的用nvidia的devel镜像, 否则用runtime的
```

## test
```python
import tensorflow as tf

x = tf.random.uniform([3, 3])

print("Is there a GPU available: ")
print(tf.config.experimental.list_physical_devices("GPU"))

print("Is the Tensor on GPU #0:  ")
print(x.device.endswith('GPU:0'))

```
