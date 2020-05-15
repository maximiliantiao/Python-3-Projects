import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

amazon_email = input("Enter email: ")
amazon_password = getpass.getpass()

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

driver.get("https://www.amazon.com/")
signin = driver.find_element_by_id("nav-link-accountList")
signin.click()

driver.implicitly_wait(5)
email = driver.find_element_by_id("ap_email")
email.send_keys(amazon_email)

next_button = driver.find_element_by_id("continue")
next_button.click()

password = driver.find_element_by_id("ap_password")
password.send_keys(amazon_password)

signin = driver.find_element_by_id("signInSubmit")
signin.click()

end = input("Type 'y' to exit\n")
if end == "y":
  menu_button = driver.find_element_by_id("nav-hamburger-menu")
  menu_button.click()
  driver.implicitly_wait(5)
  signout = driver.find_element_by_link_text("Sign Out")
  signout.click()
  driver.close()
