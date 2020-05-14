import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

amazon_email = input("Enter email: ")
amazon_password = getpass.getpass()

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/")
signin = driver.find_element_by_id("nav-link-accountList")
signin.click()

email = driver.find_element_by_id("ap_email")
email.send_keys(amazon_email)

next_button = driver.find_element_by_id("continue")
next_button.click()

password = driver.find_element_by_id("ap_password")
password.send_keys(amazon_password)

signin = driver.find_element_by_id("signInSubmit")
signin.click()

menu_button = driver.find_element_by_id("nav-hamburger-menu")
menu_button.click()

end = input("Type 'y' to exit\n")
if end == "y":
  driver.close()
