# Rock Paper Scissors Mini Game randomly generated

import time
import random


# global variables

player1Score = 0
player2Score = 0

player1Choice = ""
player2Choice = ""
    



def startGame(): # function to start the game, Rock Paper Scissors
	
    startGameYorN = input("Would you like to start playing Rock Paper Scissors?\n")
	
    if startGameYorN == "Yes" or startGameYorN == "yes":
    # Yes to start the game
        pass
    elif startGameYorN == "No" or startGameYorN == "no":
    # No to end the game
        exit()
    else:
    # Yes or No are only valid answers
    	startGameYorNRedo = input("Please type in a valid answer (Yes or No) ")

        if startGameYorNRedo == "Yes" or startGameYorN == "yes":
		# Yes to start the game
			pass
        else:
		# No to end the game
            exit()



def rpsRandom(): # randomly generated choices for Player 1 and 2 in the game, Rock Paper Scissors
    global player1Choice
    global player2Choice

    # randomly generate a number associated with a choice to Player 1
    randomForP1 = random.randrange(1, 4)

    if randomForP1 == 1:
    # Player 1 chooses Rock!
        player1Choice += "Rock"    
        
    elif randomForP1 == 2:
    # Player 1 chooses Paper!
        player1Choice += "Paper"   


    else:
    # Player 1 chooses Scissors!
        player1Choice += "Scissors"


    # randomly generate a number associated with a choice to Player 2
    randomForP2 = random.randrange(1,4)

    if randomForP2 == 1:
    # Player 2 chooses Rock!
        player2Choice += "Rock"


    elif randomForP2 == 2:
    # Player 2 chooses Paper!
        player2Choice += "Paper"

    else:
    # Player 2 chooses Scissors!
        player2Choice += "Scissors"

    time.sleep(2) 

    print("\nPlayer 1: " + player1Choice)

    time.sleep(2)

    print("Player 2: " + player2Choice)




def pointSystem(): # point system for wins

    time.sleep(2) # pause program for 2 seconds

    global player1Choice
    global player2Choice
    global player1Score
    global player2Score

    if player1Choice == "Rock":

        if player2Choice == "Rock":
            
            print("\nIt's a tie!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))

        elif player2Choice == "Paper":
            
            player2Score += 1
            print("\nPlayer 2 wins!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))

        elif player2Choice == "Scissors":
            
            player1Score += 1
            print("\nPlayer 1 wins!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))

        else:
            pass

    elif player1Choice == "Paper":

        if player2Choice == "Rock":
            
            player1Score += 1
            print("\nPlayer 1 wins!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))
        
        elif player2Choice == "Paper":
            
            print("\nIt's a tie!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))
        
        elif player2Choice == "Scissors":
            
            player2Score += 1
            print("\nPlayer 2 wins!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))
        
        else:
            pass

    elif player1Choice == "Scissors":

        if player2Choice == "Rock":
            
            player2Score += 1
            print("\nPlayer 2 wins!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))
        
        elif player2Choice == "Paper":
            
            player1Score += 1
            print("\nPlayer 1 wins!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))
        
        elif player2Choice == "Scissors":
            
            print("\nIt's a tie!")
            time.sleep(1)
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))
                
        else:
            pass

    else:
        pass







# function calling


startGame()

rpsRandom()

pointSystem()

# continue playing game or not
restartGame = input("\nDo you want to play again? Press enter to continue or type 'exit' to leave. ")

player1Choice = ""
player2Choice = ""

while restartGame == "":

    rpsRandom()

    pointSystem()

    restartGame = input("\nDo you want to play again? Press enter to continue or type 'exit' to leave. ")

    player1Choice = ""
    player2Choice = ""

else:
    pass

time.sleep(1)
print('Final Score')
time.sleep(1)
print('Player 1: %0d' % (player1Score))
print('Player 2: %0d' % (player2Score))
time.sleep(1)
print('Thanks for playing!')
time.sleep(1)
pass













