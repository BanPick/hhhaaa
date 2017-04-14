#-*- coding: UTF-8 -*-
import time
from element import *
from selenium import webdriver


browser = webdriver.Firefox()
browser.get("https://njtest.mhealth365.cn/")
browser.maximize_window()
element = find_element(browser,"id",'AdminLoginForm_username')
element.send_keys("qwe")
time.sleep(3)
browser.quit()