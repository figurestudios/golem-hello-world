# golem-hello-world-py

## Pre-requisites
* Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop) is installed and running.
* Make sure you have the gvmkit-build module installed. [This](https://handbook.golem.network/requestor-tutorials/vm-runtime) page might be useful if you want to understand more in-depth how pushing and converting images work.
* Make sure that you have gone through the [quick primer example](https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development) as to get your environment running and understood.

## Building

```
docker build -t golem-hello-world-py:latest .
python -m gvmkit_build golem-hello-world-py:latest
python -m gvmkit_build golem-hello-world-py:latest --push
```

Note that normally it's `gvmkit-build` rather than `gvmkit_build` but something is wrong in my installation.

Copy the hash link, which in my case is `eb26fc55959db9901148fc6dfaed8578b2f8fb7067c88feaeb1846f8` and swap it out in the provider.py file.

## Running

```
set YAGNA_APPKEY=<YOUR_APPKEY>
yagna payment init --sender
py requestor.py
```
