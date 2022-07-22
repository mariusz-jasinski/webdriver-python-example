FROM python:3.8-slim

# Add bash, tzdata
RUN apt-get install -y bash tzdata
ENV TZ="Europe/Warsaw"

USER root

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

RUN date
RUN mkdir -p workspace
COPY . workspace/
WORKDIR workspace

# flask depends on this env variable to find the main file
EXPOSE 5000
ENV FLASK_APP=index.py
CMD ["/bin/bash", "-c", "flask run -h 0.0.0.0"]


# * Serving Flask app 
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# source $(pipenv --venv)/bin/activate
