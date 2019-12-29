import requests
import random
from bs4 import BeautifulSoup

quote_site = requests.get("https://www.brainyquote.com/topics/daily-quotes")

quote_site_content = quote_site.content

soup = BeautifulSoup(quote_site_content, 'html.parser')



print("\n***************************************** Quote of The Day *****************************************")
quote = soup.find_all("a", class_="b-qt")
index = random.randint(0, 25)
print("\n" + quote[index].text, end="\n\n")
author = soup.find_all("a", class_="bq-aut")
print(author[index].text, end="\n\n")
print("*" * 100, end="\n")
