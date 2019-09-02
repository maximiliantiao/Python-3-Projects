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

#print("Which did you want to check out?")
#print("1. HLTV - Today's News")
#print("2. HLTV - Today's Matches")

#which_check_out = input()

#if which_check_out == "1":
'''
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

#elif which_check_out == "2":

resultB = requests.get("https://hltv.org")

srcB = resultB.content
soupB = BeautifulSoup(srcB, "html.parser")

print("Today's Games\n")

for div_tag in soupB.find_all("a", class_="hotmatch-box a-reset"):
    teamA = div_tag.find_all("span", class_="team")[0]
    teamB = div_tag.find_all("span", class_="team")[1]
    print(teamA.string + " vs " + teamB.string)


print("\n")
'''

resultC = requests.get("https://www.hltv.org/stats/players?startDate=2019-01-01&endDate=2019-12-31&rankingFilter=Top20")
srcC = resultC.content
print(resultC.status_code)
soupC = BeautifulSoup(srcC, "lxml")
print("Top Players - " + day_of_week + ", " + month + " " + day + ", " + year + "\n")

countB = 1

for players in soupC.find_all("td", class_="playerCol"):
    if countB < 11:
        player = players.find("a")
        country = players.find("img")

        for rating in soupC.find_all("td", class_="ratingCol"):
            print(str(countB) + ". " + player.string + " (" + country.attrs['title'] + ") - Rating:", rating.text)
            break

        countB += 1
    else:
        print("\n")
        exit()









