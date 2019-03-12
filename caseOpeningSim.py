# CSGO Danger Zone case opening simulator

import time
import random
import decimal



def walletCheckAdd():
    
    wallet = 10
    totalMoneySpent = 0
    costOfCase = 2
    moneyAdded = 0
    
    print ("\nCurrent balance: $%1d" % (wallet))
    
    print ("\nWould you like to add funds to open Danger Zone case?")
    answer2 =  raw_input("Yes or No?\n")
    
    time.sleep(0.8)
    
    if answer2 == "No" or answer2 == "no":
        wallet -= 2
        totalMoneySpent += 2
        pass
    
    else:
        
        if answer2 == "Yes" or answer2 == "yes":
            print ("\nEnter amount to add:")
            answer3  = int(raw_input("$5 $10 $15 $20 $50 $100\n"))
            moneyAdded += answer3
            time.sleep(1)
            print ("\n$%1d has been added to your wallet" % (answer3))
            time.sleep(1)
        
        elif answer2 == "No" or answer2 == "no":
            pass
        else:
            pass

    print ("\nOpen Danger Zone case for $2?")
    
    answer1 = raw_input("Yes or No?\n")

    if answer1 == "Yes" or answer1 == "yes":
        
        wallet -= 2
        totalMoneySpent += 2
        
        time.sleep(1)

    else:
        pass

    time.sleep(2)

    print ("\nYour Receipt:")
    print("Wallet: $%1d" % (wallet))
    print("Case cost: $%1d" % (costOfCase))
    print("Total money spent: $%1d" % (totalMoneySpent))
    print("Money added: $%1d\n" % (moneyAdded))


def skinGradeOdds():
    # probabilities of certain grades: Mil-Spec, Restricted, Classified, Covert, Exceedingly Rare
    
    skinGrade = ""
        
    skinGradeProb = random.randrange(262, 10100)/100

    if skinGradeProb >= 20.0 and skinGradeProb < 100.0:
    # drops a blue grade skin
        skinGrade += "Mil-Spec"
        print (skinGrade)
        
    elif skinGradeProb >= 3.0 and skinGradeProb < 20.0:
    # drops a purple grade skin
        skinGrade += "Restricted"
        print (skinGrade)
        
    elif skinGradeProb >= 2.91 and skinGradeProb < 3.0:
    # drops a pink grade skin
        skinGrade += "Classified"
        print (skinGrade)
        
    elif skinGradeProb >= 2.70 and skinGradeProb < 2.91:
    # drops a red grade skin
        skinGrade += "Covert"
        print (skinGrade)
        
    elif skinGradeProb >= 2.62 and skinGradeProb < 2.7:
    # drops a yellow grade skin
        skinGrade += "Exceedingly Rare"
        print (skinGrade)
        
    else:
        print ("Error")


def skinGradeStatTrak():
# probabilitries of StatTrak or not

    statTrak = ""

    statTrakProb = random.randrange(0, 100)

    if statTrakProb > 10 and statTrakProb < 100:
    # drops a non-StatTrak skin grade
        statTrakYorN = "Non-StatTrak"
        print (statTrakYorN)

    elif statTrakProb >= 0 and statTrakProb <= 10:
    # drops a StatTrak skin grade
        statTrakYorN = "StatTrak"
        print (statTrakYorN)

    else:
        print ("Error")






# function calling

#walletCheckAdd()

#skinGradeOdds()

skinGradeStatTrak()










	
			
		

		
	
	





