# golem-hello-world-c

## Pre-requisites
* Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop) is installed and running.
* Make sure you have the gvmkit-build module installed. [This](https://handbook.golem.network/requestor-tutorials/vm-runtime) page might be useful if you want to understand more in-depth how pushing and converting images work.
* Make sure that you have gone through the [quick primer example](https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development) as to get your environment running and understood.

## Building
The Docker image for C is very similar to one for C++. look at `Dockerfile_cpp` to see how to build for C++. more or less just swap out `gcc` with `g++`, and `libc-dev` with `libstdc++`

### Linux Build instructions
note: you may need `sudo` to run `docker` commands.
```
docker build -t golem-hello-world-c:latest .
gvmkit-build golem-hello-world-c:latest
gvmkit-build golem-hello-world-c:latest --push
```

Copy the hash link, in my case
```
C: 9ba449e948b3249732a67e2f557a17085101a7d60c9d7c27a4c93a20
C++: 8f22d6f76c115a51bdb08fe1ce8306621f58ed9049e86380da178cc0
```
and swap it out in the requestor.py file.

## Running

### Linux
```
export YAGNA_APPKEY=<YOUR_APPKEY>
yagna payment init --sender
python3 requestor.py
```

### Windows
```
set YAGNA_APPKEY=<YOUR_APPKEY>
yagna payment init --sender
py requestor.py
```
