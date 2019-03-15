# Rock Paper Scissors Mini Game randomly generated


import random


# just some variables

player1Score = 0
player2Score = 0
    
player1Choice = ""
player2Choice = ""

# function to start the game, Rock Paper Scissors
def startGame():
	
    startGameYorN = raw_input("Would you like to start playing Rock Paper Scissors?\n")
	
    if startGameYorN == "Yes" or startGameYorN == "yes":
    # Yes to start the game
        pass
    elif startGameYorN == "No" or startGameYorN == "no":
    # No to end the game
        exit()
    else:
    # Yes or No are only valid answers
    	startGameYorNRedo = input("Please type in a valid answer (Yes or No)")

        if startGameYorNRedo == "Yes" or startGameYorN == "yes":
		# Yes to start the game
			pass
        else:
		# No to end the game
            exit()


# randomly generated choices for Player 1 and 2 in the game, Rock Paper Scissors
def rpsRandom():

    player1Score = 0
    player2Score = 0
    
    player1Choice = ""
    player2Choice = ""

    # randomly generate a number associated with a choice to Player 1
    randomForP1 = random.randrange(1, 4)

    if randomForP1 == 1:
    # Player 1 chooses Rock!
        player1Choice += "Rock!"
        
    elif randomForP1 == 2:
    # Player 1 chooses Paper!
        player1Choice += "Paper!"

    else:
    # Player 1 chooses Scissors!
        player1Choice += "Scissors!"

    # randomly generate a number associated with a choice to Playeer 2
    randomForP2 = random.randrange(1,4)

    if randomForP2 == 1:
    # Player 2 chooses Rock!
        player2Choice += "Rock!"

    elif randomForP2 == 2:
    # Player 2 chooses Paper!
        player2Choice += "Paper!"

    else:
    # Player 2 chooses Scissors!
        player2Choice += "Scissors!"


# point system for wins
def pointSystem(player1Choice, player2Choice):

    if player1Choice == "Rock":

        if player2Choice == "Rock":
            
            print("It's a tie!")

        elif player2Choice == "Paper":
            player2Score += 1
            print("Player 2 wins!")
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))

        elif player1Choice == "Scissors":
            player1Score += 1
            print("Player 1 wins!")
            print("Player 1 score: %1d" % (player1Score))
            print("Player 2 score: %1d" % (player2Score))

        else:
            pass








# function calling

startGame()

rpsRandom()


