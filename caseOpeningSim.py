# CSGO Danger Zone case opening simulator

import time


    

def walletCheckAdd():
        
    wallet = 10
    totalMoneySpent = 0
    costOfCase = 2

    print ("Open Danger Zone case for $2?")
    
    answer1 = raw_input("Yes or No: ")
    
    time.sleep(2)

    # checking wallet for money and adding funds if needed

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
                pass
                        

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

skinGradeOdds()










	
			
		

		
	
	





