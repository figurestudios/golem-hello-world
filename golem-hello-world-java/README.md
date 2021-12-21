# golem-hello-world-java

## Pre-requisites
* Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop) is installed and running.
* Make sure you have the gvmkit-build module installed. [This](https://handbook.golem.network/requestor-tutorials/vm-runtime) page might be useful if you want to understand more in-depth how pushing and converting images work.
* Make sure that you have gone through the [quick primer example](https://handbook.golem.network/requestor-tutorials/flash-tutorial-of-requestor-development) as to get your environment running and understood.

## Building
### Linux Build instructions
Java lets us build and test our code, then just copy the `.jar` into a docker image with jre installed.

Lets build a simple java program from [Provider.java](Provider.java)

The image is using java version 11, so for best results set your jdk to java 11 when building.
```
javac Provider.java
jar cfe Provider.jar Provider Provider.class
```


note: you may need `sudo` to run `docker` commands.
```
docker build -t golem-hello-world-java:latest .
gvmkit-build golem-hello-world-java:latest
gvmkit-build golem-hello-world-java:latest --push
```

Copy the hash link, which in my case is `cc4d7097d7a5aa1cd2630e90c482b79e6a1a706165e7438b563b37a5` and swap it out in the requestor.py file.

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
