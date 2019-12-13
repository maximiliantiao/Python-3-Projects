import requests
from bs4 import BeautifulSoup
import datetime
import time
import keyboard

current_time = datetime.datetime.now()
day_of_week = current_time.strftime("%A")
month = current_time.strftime("%B")
day = current_time.strftime("%d")
year = current_time.strftime("%Y")
hour = current_time.strftime("%I")
minutes = current_time.strftime("%M")
AMorPM = current_time.strftime("%p")

print("=" * 100)
print("\nWelcome to the HLTV Parser\n")
print("=" * 100)

time.sleep(1)
print("\nWhich did you want to check out?")
time.sleep(0.2)
print("1. HLTV - Today's News")
time.sleep(0.2)
print("2. HLTV - Today's Matches")
time.sleep(0.2)
print("3. HLTV - 2019's Top 10 Best Players")

which_check_out = input()

if which_check_out == "1":

    resultA = requests.get("https://www.hltv.org")
    #print(resultA.status_code)
    srcA = resultA.content
    soupA = BeautifulSoup(srcA, "html.parser")

    print("\n")
    print("HTLV News - " + day_of_week + " " + month + " " + day + " " + year + "\n")

    for divA_tag in soupA.find_all("div", class_="standard-box standard-list")[0]:
        headline = divA_tag.find("div", class_="newstext")
        print("- " + headline.string)
        time.sleep(0.2)

    print("\n")

elif which_check_out == "2":

    resultB = requests.get("https://hltv.org")
    srcB = resultB.content
    soupB = BeautifulSoup(srcB, "html.parser")
    print("\nToday's Games\n")

    for a_tag in soupB.find_all("a", class_="hotmatch-box"):
        teamA = a_tag.find_all("span", class_="team")[0]
        teamB = a_tag.find_all("span", class_="team")[1]
        print(teamA.string + " vs. " + teamB.string)

    print("\n")

elif which_check_out == "3":

    resultC = requests.get("https://www.hltv.org/stats/players?startDate=2019-01-01&endDate=2019-12-31&rankingFilter=Top20")
    srcC = resultC.content
    # print(resultC.status_code)
    soupC = BeautifulSoup(srcC, "lxml")
    print("\nTop Players - " + day_of_week + ", " + month + " " + day + ", " + year + "\n")

    playerNames = []
    playerTeams = []
    playerKDRatio = []
    playerMapNum = []
    playerKDDiff = []
    player2Ratio = []
    count = 1

    for players in soupC.find_all("td", class_="playerCol"):
        player = players.find("a")
        playerNames.append(player.string)

    for teamCol in soupC.find_all("td", class_="teamCol"):
        team = teamCol.find("img", class_="logo")
        playerTeams.append(team.attrs['alt'])

    for statsDetail in soupC.find_all("td", class_="statsDetail"):
        if float(statsDetail.string) < 3.0:
            playerKDRatio.append(statsDetail.string)
        else:
            playerMapNum.append(statsDetail.string)

    for kdDiff in soupC.find_all("td", class_="kdDiffCol"):
        playerKDDiff.append(kdDiff.string)

    for rankingRatio in soupC.find_all("td", class_="ratingCol"):
        player2Ratio.append(rankingRatio.string)

    print("What would you like to see?")
    print("1. Each player listed out one by one")
    print("2. List out all players")

    listHow = input()

    if listHow == "1":
        print("As each player is listed, you must either press return to continue down the list")
        print("or press 'N' to stop")
        x = 0
        count = 1

        continueOrNot = input()
        while continueOrNot == "":
            print(str(count) + ". " + playerNames[x] + " (" + playerTeams[x] + ")")
            print("Maps: " + playerMapNum[x])
            print("K-D Diff: " + playerKDDiff[x])
            print("K/D: " + playerKDRatio[x])
            print("Rating 2.0: " + player2Ratio[x])
            x += 1
            count += 1
            continueOrNot = input()
    else:
        for x in range(10):
            print(str(count) + ". " + playerNames[x] + " (" + playerTeams[x] + ")")
            print("Maps: " + playerMapNum[x])
            print("K-D Diff: " + playerKDDiff[x])
            print("K/D: " + playerKDRatio[x])
            print("Rating 2.0: " + player2Ratio[x])
            count += 1
            time.sleep(0.5)

else:
    print("Choose a valid option!")






