from selenium import webdriver
import time
# this simple code is for dealing with sample auto login on website
def db_login():
	browser= webdriver.Firefox()
	browser.get('https://www.douban.com')#get the link address
	time.sleep(1) #wait the browser to response
	user =browser.find_element_by_css_selector('#form_email')#find the place to insert the username
	user.send_keys('dbtlive@gmail.com')# user name 
	password = browser.find_element_by_css_selector('#form_password')# find the place to insert the password
	password.send_keys('')
	login =browser.find_element_by_css_selector('.bn-submit') #find the button you want to click
	login.click() #click it
	time.sleep(2)# wait browser to responce
	input_stuff =browser.find_element_by_css_selector('#inp-query')#find the new place to typing
	input_stuff.send_keys('candyme') #typing content 
	click_stuff = browser.find_element_by_css_selector('.inp-btn > input:nth-child(1)') #find the button
	click_stuff.click()#click
	time.sleep(2)
	candy= browser.find_element_by_css_selector('div.result-list:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)')
	candy.click()

db_login()
