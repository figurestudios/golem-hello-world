FROM alpine:latest

# install java runtime
RUN apk add openjdk11-jre
COPY Provider.jar /

VOLUME /golem/input /golem/work /golem/output
WORKDIR /golem/work