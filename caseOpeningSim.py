# CSGO Danger Zone case opening simulator

import time


    

def walletCheckAdd():
        
    wallet = 10
    totalMoneySpent = 0
    costOfCase = 2

    print ("\nOpen Danger Zone case for $2?")
    
    answer1 = raw_input("Yes or No?\n")
    
    # checking wallet for money and adding funds if needed

    if answer1 == "Yes" or answer1 == "yes":
        
        wallet -= 2
        
        totalMoneySpent += 2
        
        time.sleep(0.8)
        
        print("\nWallet: $%1d" % (wallet))
        
        time.sleep(0.8)

        print("\nCase cost: $%1d" % (costOfCase))
        
        time.sleep(0.8)
        
        print ("\nWould you like to add funds?")
        answer2 =  raw_input("Yes or No?\n")
        
        time.sleep(0.8)
               
        if answer2 == "No" or answer2 == "no":
            wallet -= 2
            totalMoneySpent += 2
            pass
            
        else:
		
            if answer2 == "Yes" or answer2 == "yes":
                print ("\nEnter amount to add:")
                answer3  = int(raw_input("$5 $10 $15 $20 Custom\n"))

                if answer3 == "Custom" or answer3 == "custom":
                    answer4 = int(raw_input("Enter custom amount: "))
                    wallet += answer4
                else:
                    wallet += answer3
			
            elif answer2 == "No" or answer2 == "no":
                pass
            else:
                pass
    else:
        pass
    
    time.sleep(2)

    print ("\nYour Receipt:")
    print("Wallet: $%1d" % (wallet))
    print("Case cost: $%1d" % (costOfCase))
    print("Total money spent: $%1d\n" % (totalMoneySpent))


def skinGradeOdds():
# probabilities of certain grades: blue, purple, pink, red, yellow

    skinGrade = ""
             
    random = uniform(2.62, 100.0) #fix random number generator

    if random >= 20 and random < 100:
    # drops a blue grade skin
        skinGrade += blue
        return skinGrade

    elif random >= 3 and random < 20:
    # drops a purple grade skin
        skinGrade += purple
        return skinGrade

    elif random >= 2.91 and random < 3:
    # drops a pink grade skin
        skinGrade += pink
        return skinGrade
        
    elif random >= 2.70 and random < 2.91:
    # drops a red grade skin
        skinGrade += red
        return skinGrade

    elif random >= 2.62 and random < 2.7:
    # drops a yellow grade skin
        skinGrade += yellow
        return skinGrade


    #def skinGradeStatTrak():
    # probabilitries of StatTrak or not






# function calling
walletCheckAdd()










	
			
		

		
	
	





