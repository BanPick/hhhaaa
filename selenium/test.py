#-*- coding: UTF-8 -*-
import time
from element import *
from selenium import webdriver
import SendKeys


driver = webdriver.Firefox()
# browser.get("http://saas.mhealth365.cn/pati/patcase?id=14628892864988")
driver.get('http://saas.mhealth365.cn/Pers/setHeard')
driver.maximize_window()
driver.find_element_by_id('imgInput').click()
# driver.find_element_by_class_name('el-input__inner').click()
# driver.find_element_by_css_selector('input[]').click()
# driver.find_element_by_xpath("//input[@placeholder='请选择']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//li[contains(.,'男')]").click()
# element = find_element(browser,"class","el-icon-plus")

# # operate_element(element, 'click')
# enter_value(element, 'Hydrangeas.jpg')
# time.sleep(1)
# SendKeys.SendKeys('E:\work\hhhaaa.git\\trunk\selenium\Hydrangeas.jpg')  # 发送文件地址
# SendKeys.SendKeys("{ENTER}") # 发送回车键
time.sleep(3)
driver.quit()

