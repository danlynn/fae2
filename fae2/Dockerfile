# FROM django:1.8-python3
# FROM django:python3
FROM django:python3-onbuild

MAINTAINER Dan Lynn <docker@danlynn.org>

RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8
# ENV JAVA_VERSION 6b36

RUN apt-get update && apt-get install -y openjdk-7-jdk && rm -rf /var/lib/apt/lists/*

# TODO: ONBUILD setup env and run fae-util/build
