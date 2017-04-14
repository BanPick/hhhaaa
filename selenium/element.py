from selenium import webdriver

def find_element(driver, locator, value):
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
	elif locator == 'css_selector':
		element = driver.find_element_by_css_selector(value)	
	return element

def operate_element(element, oper):
	element.oper

def enter_value(element, value)
	element.send_keys(value)

def assert_element(element, attr, value)
	try:



