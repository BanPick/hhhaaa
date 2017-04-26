#-*- coding: UTF-8 -*-
from selenium import webdriver
import SendKeys

def find_element(driver, locator, value):   #定位元素
	element = ''
	if locator == 'id':
		element = driver.find_element_by_id(value)
	elif locator == 'name':
		element = driver.find_element_by_name(value)
	elif locator == 'class':
		element = driver.find_element_by_class_name(value)
	elif locator == 'xpath':
		element = driver.find_element_by_xpath(value)
	elif locator == 'link_text':
		element = driver.find_element_by_link_text(value)
	elif locator == 'partial_link_text':
		element = driver.find_element_by_partial_link_text(value)	
	elif locator == 'css':
		element = driver.find_element_by_css_selector(value)	
	return element

def operate_element(element, oper):
	if oper == 'click':
		element.click()
	# elif oper == 


def drop_dowm_list():
	pass

def enter_value(element, value):     #输入值
	element.send_keys(value)

def upload_file(url):               #上传文件
	SendKeys.SendKeys(url)  
	SendKeys.SendKeys("{ENTER}") 

# def assert_element(element, attr, value)
# 	try:



