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
from seleniumwire import webdriver  # Import from seleniumwire

# ./imageutil.py.py
import imageutil


BROWSER_URL = 'http://browser:4444/wd/hub'
BROWSER_PATH = '/usr/bin/chromedriver'
PAGE_URI = 'https://en.wikipedia.org/wiki/Main_Page'
#PAGE_URI = 'https://httpbin.org/headers'
DOWNLOAD_DIR = "/tmp"
TOKEN_JWT = 'bearer any'


class Tests(unittest.TestCase):
    def test_smth(self):
        chrome_options = Options()
        
        chrome_options.add_argument('--kiosk-printing')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--enable-print-browser')
        #chrome_options.add_argument('--disable-notifications')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        wire_options = {
            'addr': hostname
        }

        # Create a request interceptor
        def header_interceptor(request):
            del request.headers['Authorization']
            request.headers['Authorization'] = TOKEN_JWT

        #  21.0 x 29.7cm, 8.27 x 11.69 inches
        printOptions = PrintOptions()
        printOptions.orientation = 'portrait'
        printOptions.page_width = 21.0
        printOptions.page_height = 29.7
        printOptions.scale = 0.90

        print (wire_options)
        # browserDriver = webdriver.Remote(command_executor=BROWSER_URL, options=chrome_options, seleniumwire_options=wire_options)
        # browserDriver = webdriver.Remote(command_executor=BROWSER_URL, options=chrome_options)
        browserDriver = webdriver.Chrome(service=Service(BROWSER_PATH), options=chrome_options)

        # Set the interceptor on the driver
        browserDriver.request_interceptor = header_interceptor
        browserDriver.maximize_window()
        browserDriver.set_page_load_timeout(30)

        
        browserDriver.get(PAGE_URI)
        
        # print(browserDriver.get_screenshot_as_file('/tmp/page.png'))
        imageutil.fullpage_screenshot(browserDriver, '/tmp/page.png')
        
        pdf64Text = browserDriver.print_page(printOptions)
        base64_bytes = pdf64Text.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)

        with open(DOWNLOAD_DIR + '/file.pdf', 'wb') as f:
            f.write(  message_bytes )
            f.close()
        
        browserDriver.close()
        browserDriver.quit()
        print(f'test finished')
        
        # list file and directories
        res = os.listdir(DOWNLOAD_DIR)
        print(res)        
        


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Tests))
    return test_suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=3).run(suite())
