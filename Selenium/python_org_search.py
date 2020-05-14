import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search = input("Type in a search: ")

driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
end = input("Type 'y' to exit\n")
if end == "Y":
  driver.close()
