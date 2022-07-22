FROM selenium/standalone-chrome:102.0

# ubuntu
# python:3.8
# /usr/bin/chromedriver

USER root

RUN sudo apt-get update -y
RUN sudo apt-get install -y software-properties-common \
    && sudo add-apt-repository ppa:deadsnakes/ppa

RUN    sudo apt-get install -y python3.9 \
    && python3 --version
RUN sudo apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

RUN sudo apt-get install -y tzdata
ENV TZ="Europe/Warsaw"

RUN date
RUN mkdir -p workspaces/tests
COPY . workspaces/tests/
WORKDIR workspaces/tests
