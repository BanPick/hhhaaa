#-*- coding: UTF-8 -*-
import time
from element import *
from selenium import webdriver


browser = webdriver.Firefox()
# browser.get("http://saas.mhealth365.cn/pati/patcase?id=14628892864988")
browser.get('file:///C:/Users/nihao/Desktop/test.html')
browser.maximize_window()
browser.find_element_by_css_selector('input[value=新增病程]').click()
element = find_element(browser,"class","el-icon-plus")

# operate_element(element, 'click')
enter_value(element, 'Hydrangeas.jpg')
time.sleep(3)
browser.quit()