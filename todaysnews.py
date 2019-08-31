import requests
from bs4 import BeautifulSoup
import datetime

current_time = datetime.datetime.now()
day_of_week = current_time.strftime("%A")
month = current_time.strftime("%B")
day = current_time.strftime("%d")
year = current_time.strftime("%Y")
hour = current_time.strftime("%I")
minutes = current_time.strftime("%M")
AMorPM =  current_time.strftime("%p")

print("Which did you want to check out?")
print("1. HLTV News")
print("2. New Posts on r/UCSC")
print("3. New Posts on r/todayilearned")

which_check_out = input()

print("\n")

if which_check_out == "1":

    resultA = requests.get("https://www.hltv.org")
    print(resultA.status_code)
    srcA = resultA.content

    soupA = BeautifulSoup(srcA, "html.parser")

    countA = 1

    for divA_tag in soupA.find_all("div", class_="standard-box standard-list")[0]:
        headline = divA_tag.find("div", class_="newstext")
        print(str(countA) + ". " + headline.string)
        countA += 1

    print("\n")

elif which_check_out == "2":

    resultB = requests.get("https://www.reddit.com/r/UCSC/new/")

    srcB = resultB.content
    print(resultB.status_code)
    soupB = BeautifulSoup(srcB, "html.parser")

    countB = 1

    for divB_tag in soupB.find_all("div", class_="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe"):
        post_title = divB_tag.find("h3", class_="_eYtD2XCVieq6emjKBH3m")
        print(str(countB) + ". " + post_title.string)
        countB += 1

    print("\n")

elif which_check_out == "3":

    resultC = requests.get("https://www.reddit.com/r/todayilearned/new/")

    srcC = resultC.content

    soupC = BeautifulSoup(srcC, "html.parser")

    count = 1

    for div_tag in soupC.find_all("div", class_="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe "):
        today_I_learned_post = div_tag.find("h3", class_="_eYtD2XCVieq6emjKBH3m")
        print(str(count) + ". " + today_I_learned_post)
        count += 1

    print("\n")

elif
