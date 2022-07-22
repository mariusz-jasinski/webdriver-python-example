FROM python:3.8-slim

# Add bash, tzdata
RUN apt-get install -y bash tzdata
ENV TZ="Europe/Warsaw"

USER root

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt


RUN date
RUN mkdir -p workspaces/tests
COPY . workspaces/tests/
WORKDIR workspaces/tests
