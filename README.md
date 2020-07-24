# BestBuy-refresh-and-buy
For automatically signing in bestbuy account and add a product to cart and proceed to checkout.

## Motivation
In 2020 mid-April, when the quarantine started, reacting to the spread of COVID-19, stock shortages of goods started to exist, including the Nintendo Switch Consoles. Nintendo announced Switch replenishment very soon. However, due to slow replenishment and shipments, BestBuy controls the stock by releasing one console at a time online, at a random time for few times in a day. I was so amazed that the one console could be sold right after it was released within a minute or even half a minute, and then the product page will show that the product is out of stock again. It would be impossible for me to sit down and keep refreshing the page every second to fight for a Switch. So there comes the idea to write a program that would help me to refresh the page for every few seconds and check out a Switch when BestBuy releases one.

## Usage
Requirement:
* python selenium-webdriver
* chromedriver
* BestBuy account (Canada account probably, not sure if BestBuy webpage for the U.S. and Mexico would be the same)
  * modify account username/email and password here
  ```python
  driver.find_element_by_id("username").send_keys("xxxxx@xxx.com")
  driver.find_element_by_id ("password").send_keys("xxxxxxxxx")
  ```
* Credit card saved in BestBuy account
  * enter the cvv number of credit card here
  ```python
  driver.find_element_by_id('cvv').send_keys('000')
  ```
* Product page of product you wanted to buy
  * modify the product page url here
  ```python
  (line 27)  driver.get("https://www.bestbuy.ca/en-ca/product/nintendo-switch-console-with-neon-red-blue-joy-con/13817625")
  ```

Through terminal, run:
```cmd
python refresh.py
```
* A new chrome application will start
* Signs into BestBuy with given account
* If Google Verification pops up, you will need to verify yourself by hand, you have 50 seconds to do so
* After logging in, it will automatically jump to the product page
* Stock status of the product:
  * Product in stock => Automatically add to cart and check out with saved credit card
  * Product out of stock => Refresh until the product is in stock, add to cart and check out with saved credit card
* There are cases when a product is added to cart but happens to be out of stock just before checking out, then modify in the code here:
  ```python
  (line 9)  refreshCart = True
  ```
  Restart the program, the program will start refreshing on the page of your cart instead since it could proceed faster to check out than the previous way.
* An alarming voice will sound if it successfully checked out the product
* If something went wrong, it will output an error message
* If you have a WeChat application signed in on your computer, you can uncomment the following code at the bottom so that the code will open your WeChat and send notifications to your phone! Messages will either be "Finished!" or "ERROR!".
  ```python
  os.system('wechat')
  keyboard.press_and_release('ctrl+f')
  keyboard.write('文件')
  time.sleep(2)
  keyboard.press_and_release('enter')
  firstT = 1
  for i in range(3):
    keyboard.write(message)
    keyboard.press_and_release('enter')
    time.sleep(1)
  ```
  
  
  P.S. So I got one Switch for myself and two for two of my best friends!!!!!!!!!!!!!!!! 
