import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

print("What email provider would you like to use?")
print("1. Gmail")
print("2. Yahoo")
print("3. Outlook")
print("4. Aol")
print("5. iCloud")
print("6. Other")

choice = input("Enter a number: ")

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)

if choice == "1":
  driver.get("https://mail.google.com/")
elif choice == "2":
  driver.get("https://mail.yahoo.com/")
  # find sign in button
  sign_in = driver.find_element_by_link_text("Sign in")
  sign_in.click()
elif choice == "3":
  driver.get("https://www.outlook.com/")
  # find sign in button
  sign_in = driver.find_element_by_link_text("Sign in")
  sign_in.click()
elif choice == "4":
  driver.get("https://www.mail.aol.com/")
elif choice == "5":
  driver.get("https://www.icloud.com/")
else:
  exit()

exit_window = input("Press 'y' to exit\n")
if exit_window == 'y':
  driver.close()
