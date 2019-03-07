#CSGO Danger Zone case opening simulator

import time

wallet = 0
totalMoneySpent = 0

print ("Open Danger Zone case for $2?")

answer1 = raw_input("Yes or No: ")

time.sleep(2)

#checking wallet for money and adding funds if needed

if answer1 == "Yes" or answer1 == "Yes":
	
	if wallet > 1:
		totalMoneySpent += 1
		wallet -= 1
	else:
		print ("Add funds to continue your purchase?")
		answer2 = raw_input("Yes or No: ")
		
		if answer2 == "Yes" or answer2 == "yes":
			print ("Enter amount to add")
			answer3  = raw_input("5 10 15 20 Custom")

			if answer3 == "Custom" or answer3 == "custom":
				answer4 = raw_input("Enter custom amount: ")
			else:
				wallet += answer3
			
		elif answer2 == "No" or answer2 == "no":
			pass
		else:
			break
else:
	break


	
			
		

		
	
	





