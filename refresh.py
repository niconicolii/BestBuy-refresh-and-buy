import time
from selenium import webdriver
from tkinter import *
from tkinter import messagebox
import winsound
import os
import keyboard

refreshCart = False

message = "Finished!"

driver = webdriver.Chrome()

driver.get("https://www.bestbuy.ca/identity/en-ca/signin?tid=1m12CbrgeuiwHnH%252FAzfIQDdxhOwAHGnXHd%252BVFXydmi8Lc293h6QAkJ5koKCBjR2drs9kYXefg7itXTooldGMJgZLvnXw5ITUScb1io93N1lPhr5SwcnttrpZ%252BWJOq9FWLMr7ji%252FE8muXeTw93YzWl7yU24Xxy1x5wGMzWMXp2Wum6GPZS8lDkKbV%252B8PyZ2rfg7nIhAZllP4NUocoKNxH0YOJVGsYNqcHfyhaylYV%252BjNPd18kmUAMxQaeQ%252BXYNgSqiXniBFzFYFy7BaoXiEKXKKCxpcC2hnvZ01ewevVYlIBZqux1wDA4QsniJfpGiNqJ/")

try:
	# trying to log into account
	driver.find_element_by_id("username").send_keys("xxxxx@xxx.com")
	driver.find_element_by_id ("password").send_keys("xxxxxxxxx")
	driver.find_elements_by_xpath('//*[@id="signIn"]/div/button')[0].click()
	time.sleep(50) # allow time for logging in before going to another page


	if refreshCart == False:
		# open product pages
		driver.get("https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625")
		time.sleep(1)

		# refresh if the "Add to Cart" button is disabled
		while(not driver.find_element_by_xpath('//*[@id="test"]/button').is_enabled()):
			driver.refresh()
			time.sleep(1)

		# click the "Add to Cart" button if it is enabled
		driver.find_element_by_xpath('//*[@id="test"]/button').click()
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="cartIcon"]/div[1]/a').click()
	else:
		# this if for when I successfully added the product into my cart but then it was sold out again before I could check out
		# then I could start refreshing the cart page then I can check out immediately when a stock appears

		driver.find_element_by_xpath('//*[@id="cartIcon"]/div[1]/a').click()
		while(len(driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/section/section[2]/div[2]/div')) == 0):
			driver.refresh()
			time.sleep(1)

	# Open payment page
	driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/section/section[2]/div[2]/div').click()

	# Wait till the pament page finished loading so I can enter my cvv number to pay
	while(len(driver.find_elements_by_id('cvv')) == 0):
		print("wait")

	# enter cvv number for the saved credit card
	driver.find_element_by_id('cvv').send_keys('000')
	driver.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button').click()
	# Ring the alarm!!!!
	winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
except:
	message = 'ERROR！'
	

# open wechat application on computer and sent notice to my phone
# uncomment this if you have a wechat application signed in on your computer
# os.system('wechat')
# keyboard.press_and_release('ctrl+f')
# keyboard.write('file')
# time.sleep(2)
# keyboard.press_and_release('enter')
# firstT = 1
# for i in range(3):
# 	keyboard.write(message)
# 	keyboard.press_and_release('enter')
# 	time.sleep(1)