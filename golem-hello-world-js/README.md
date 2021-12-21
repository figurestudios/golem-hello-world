# golem-hello-world-js

## Pre-requisites
* Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop) is installed and running.
* Make sure you have the gvmkit-build module installed. [This](https://handbook.golem.network/requestor-tutorials/vm-runtime) page might be useful if you want to understand more in-depth how pushing and converting images work.
* Make sure that you have gone through the [quick primer example](https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development) as to get your environment running and understood.

## Building
### Windows Build instructions
```
docker build -t golem-hello-world-js:latest .
python -m gvmkit_build golem-hello-world-js:latest
python -m gvmkit_build golem-hello-world-js:latest --push
```
Note that normally it's `gvmkit-build` rather than `gvmkit_build` but something is wrong in my installation.

Copy the hash link, which in my case is `48d399e06dba275294b642c4d1c9de10d84186ef0e6f91371b9d5fd2` and swap it out in the requestor.js file.

## Installing dependencies

[This](https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development/run-first-task-on-golem) page might be relevant for more details. The dependencies are copied 1:1 from this example and not tailored to this repository.
```
yarn
```

## Running

```
set YAGNA_APPKEY=<YOUR_APPKEY>
yagna payment init --sender
node requestor.js
```
