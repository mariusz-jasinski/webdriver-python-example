import unittest
import json
import time
import os
import base64
import socket


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions

import logging
from flask import Flask
from app import app

# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

BROWSER_URL = 'http://browser:4444/wd/hub'
BROWSER_PATH = '/usr/bin/chromedriver'
DOWNLOAD_DIR = "/tmp"
TOKEN_JWT = 'bearer TEST'


class WebDriverService():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--kiosk-printing')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--enable-print-browser')
        
        app.logger.info('driver Remote')
        self.browserDriver = webdriver.Remote(command_executor=BROWSER_URL, options=chrome_options)
        # browserDriver = webdriver.Chrome(service=Service(BROWSER_PATH), options=chrome_options)

    
    def webPageToPDF(self, pageURI):
        self.app = app
        
        #  21.0 x 29.7cm, 8.27 x 11.69 inches
        printOptions = PrintOptions()
        printOptions.orientation = 'portrait'
        printOptions.page_width = 21.0
        printOptions.page_height = 29.7
        printOptions.scale = 0.90

        app.logger.debug('driver start')
        browserDriver = self.browserDriver
        browserDriver.start_session()

        browserDriver.maximize_window()
        browserDriver.set_page_load_timeout(10)
        
        browserDriver.get(pageURI)
        
        pdf64Text = browserDriver.print_page(printOptions)
        base64_bytes = pdf64Text.encode('ascii')

        browserDriver.close()
        app.logger.debug('driver close')

        message_bytes = base64.b64decode(base64_bytes)
        return message_bytes
