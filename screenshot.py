#!/usr/bin/env python
from selenium import webdriver
import time, sys, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This script, when run after adjusting and filling in the credentials in the script, will login for the user, and go to a certain page within the site and 
	continuously take screenshots (dynamically resizing the page to take full screenshots of the entire page), and automatically press the next button. This 
	script was designed for a certain website that was of use to me, however it is up to the end user to format this script for his/her needs."""


#assuming the links and folder/file names are included in a text file
with open('____________', 'r') as file:
	while True:
		fileName = file.readline().strip()
		if not fileName:
			break
		folder1 = r"C:\Users\__________\Desktop\_________\{}\Questions".format(fileName)
		if not os.path.exists(folder1):
			os.makedirs(folder1)
		folder2 = r"C:\Users\__________\Desktop\__________\{}\Answers".format(fileName)
		if not os.path.exists(folder2):
			os.makedirs(folder2)
		firstLink = file.readline().strip()
		secondLink = file.readline().strip()
		thirdLink = file.readline().strip()

		#utilizes selenium gecko webdriver for Firefox
		driver = webdriver.Firefox(executable_path = r"C:\Users\_________\Desktop\geckodriver.exe")
		#gets the website
		driver.get("_______________________")
		
		#searches for the username and password forms
		username = driver.find_element_by_id("username")
		password = driver.find_element_by_id("password")
		
		#fills out the username and password forms and "clicks" the link
		username.send_keys('_________')
		password.send_keys('__________')
		driver.find_element_by_name("signIn").click()
		#makes sure the DOM has been fully loaded before interacting with the site
		time.sleep(3)
		driver.get(firstLink)
		time.sleep(3)
		driver.get(secondLink)
		time.sleep(3)
		driver.get(thirdLink)
		
		#checks for how many pages to screenshot
		numberIter = int(input("how many _______?"))
		for num in range(1,numberIter+1):
			#dynamically resizes the page to screenshot it in its entirety
			total_width = driver.execute_script("return document.body.offsetWidth")
			total_height = driver.execute_script("return document.documentElement.scrollHeight")
			driver.set_window_size(total_width, total_height)
			
			#screenshots the page
			fileName = r"{}\a{}.png".format(aFolder, str(num))
			driver.save_screenshot(fileName)
			
			#finds the next button
			driver.findElement(By.xpath('//a[@class = "Next"]')).click()
