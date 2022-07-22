import os
import time
from PIL import Image


def fullpage_screenshot(driver, file):
    """
    Saves full page screenshot from selenium webdriver
    Originally copied from https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver
    (c) ihightower
    Slightly refactored by pashawnn
    :param driver: Selenium webdriber
    :param file: Filename to save screenshot
    """
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width = driver.execute_script("return document.body.clientWidth")
    viewport_height = driver.execute_script("return window.innerHeight")
    
    rectangles = []
    i = 0
    while i < total_height:
        j = 0
        top_height = i + viewport_height
    
        if top_height > total_height:
            top_height = total_height
    
        while j < total_width:
            top_width = j + viewport_width
    
            if top_width > total_width:
                top_width = total_width
    
            rectangles.append((j, i, top_width,top_height))
    
            j += viewport_width
    
        i += viewport_height
    
    stitched_image = Image.new('RGB', (total_width, total_height))
    previous = None
    part = 0
    
    for rectangle in rectangles:
        if previous is not None:
            driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            time.sleep(0.2)
    
        file_name = "part_{0}.png".format(part)
    
        driver.get_screenshot_as_file(file_name)
        screenshot = Image.open(file_name)
    
        if rectangle[1] + viewport_height > total_height:
            offset = (rectangle[0], total_height - viewport_height)
        else:
            offset = (rectangle[0], rectangle[1])
        stitched_image.paste(screenshot, offset)
        del screenshot
        os.remove(file_name)
        part += 1
        previous = rectangle
    
    stitched_image.save(file)
