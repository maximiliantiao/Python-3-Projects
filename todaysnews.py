import requests
from bs4 import BeautifulSoup

print("Which news do you want to see?")

which_news = input("HLTV, ... more to come in the future\n")

if (which_news == "HLTV"):

    result = requests.get("https://www.hltv.org")

    src = result.content

    soup = BeautifulSoup(src, "html.parser")

    print("\n")
    count = 1

    for div_tag in soup.find_all("div", class_="standard-box standard-list")[0]:
        headline = div_tag.find("div", class_="newstext")
        print(str(count) + ". " + headline.string)
        count += 1

    print("\n")

else:
    print("Other choices not implemented yet!")



