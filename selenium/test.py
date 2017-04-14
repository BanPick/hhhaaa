#-*- coding: UTF-8 -*-
import time
from selenium import webdriver
from pytesser3 import *
from PIL import ImageEnhance 

browser = webdriver.Firefox()
browser.get("https://njtest.mhealth365.cn//passport/captcha.html?v=58d1e659a744b")
time.sleep(2)
# left = element.location['x']
# print(left)
# left
# top = element.location['Y']

# bottom = element.location['y'] + element.size['height']
browser.get_screenshot_as_file("123123.png")


browser.quit()