FROM alpine:latest

# install build dependancies for compiling c files
RUN apk add gcc libc-dev

COPY provider.c /

RUN gcc provider.c -o provider_bin 

# remove source and build resources to reduce the image size
RUN rm provider.c
RUN apk del gcc libc-dev

VOLUME /golem/input /golem/work /golem/output
WORKDIR /golem/work