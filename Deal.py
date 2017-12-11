# File: Deal.py

# Description: Program emulates a Monty Hall Problem. The player inputs the number of rounds and 
# the program outputs the percentage that they will win if they switch their guess and the percentage 
# they will win if they don't switch

# Student Name: Brian Tsai

# Student UT EID: byt76

# Course Name: CS 303E

# Unique Number: 51850

# Date Created: 2/17/17

# Date Last Modified: 2/17/17
import random
def main():
	# Player inputs the number of rounds they want to play
	rounds = eval(input("Enter the number of times you want to play: "))
	print()
	
	#Format the table 
	print (format("Prize", "<7s"), format("Guess", "<7s"), format("View", "<7s"), format("New Guess", "<7s"))

	
	switch_wins = 0 # Records the number of wins won by switching the player's initial guess 
	
	# Play the game as many times as the person inputs
	for n in range(rounds): 
		prize = random.randint(1,3) # The prize door is randomly picked from 3 doors
		guess = random.randint(1,3)	# The player's guess is randomly picked from 3 doors
		doors = list(range(1,4)) # A list of 3 doors is stored into a list
		
		# If the prize door is not the same as the guess door, then the view door will be the 
		# only door remaining. The newGuess will be the prize door because that is the only door
		# not the view or the guess. 
		if (prize!=guess): 
			doors.remove(prize) # Remove prize door from the selection
			doors.remove(guess) # Remove guess door from the selection
			view = doors.pop() # view is the only door remaining
			newGuess = prize # newGuess is set equal to the prize door 
		
		# If the prize door is the same as the guess door, view is chosen from the two remaining doors
		# and newGuess is set to the other door remaining door
		else:
			doors.remove(guess) # Remove guess door from the selection
			view = random.choice(doors) # view is selected randomly from the two remaining doors
			doors.remove(view) # Remove view door from the selection
			newGuess = doors.pop() # newGuess is set to the last door remaining

		# If the newGuess door is the same as the prize door, increase the number of wins by switching by one 
		if (newGuess == prize): 
			switch_wins += 1

		# Format the scores for printing
		print("  " + format(prize, "<4d"), "   " + format(guess, "<4d"), "  " + format(view, "<4d"), "      " + format(newGuess, "<4d"))
	
	switch_probability = switch_wins / rounds # The switch_probability is the number of wins by switch divided by rounds
	stay_probability = 1 - switch_probability # The stay_probability is the other percent
	print()
	print("Probability of winning if you switch =", format(switch_probability, "0.2f"))
	print("Probability of winning if you do not switch =", format(stay_probability, "0.2f"))	

main()			
		




