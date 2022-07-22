from flask import Flask, redirect, request
from webdriver import WebDriverService
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=['GET'])
def hello_world():
  return "Hello, World!"

@app.route("/webpage/topdf", methods=['GET'])
def webpage_topdf():
    pageURI = request.args.get('uri')
    service = WebDriverService()
    return service.webPageToPDF(pageURI)


# https://en.wikipedia.org/wiki/Main_Page
# https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMain_Page
# curl -i -o file.pdf -X GET http://127.0.0.1:8001/webpage/topdf?uri=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMain_Page
