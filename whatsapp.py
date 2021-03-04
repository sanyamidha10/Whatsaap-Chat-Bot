# Importing of different modules required for whatsapp automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Firefox webdriver is used here
driver = webdriver.Firefox()

#getting the url of whatsapp
driver.get("https://web.whatsapp.com/")

#Manual steps required for scanning and pressing of any key to let the code initialise further 
input("Please scan QR code and press any key to continue.")

#Let the code sleep for 5 seconds so that all contacts are loaded.
# sleep time can vary. 
time.sleep(5)

#Finds the name of contact to whom you want to text
Text = driver.find_element_by_xpath('//span[@title="Bhai"]')

#clicks the name of that person found
Text.click()

#Finds the text input area
testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

#this step is optional, I have done this so that code's action is visible for you.
time.sleep(2)

#pressing of keys
#write the message here that you want to send.
testinput.send_keys("hey, This message is sent through whatsapp automation")
testinput.send_keys(Keys.RETURN)

