#Problem 13: Rolling the Dice
#Write a function that simulates rolling a 
#6­sided die by generating a random integer
#from 1 to 6. Each number should have equal
#likelihood of being returned. Extra credit:
#Add an argument to your function, n, that
#lets a programmer choose n, the highest
#number on the n­sided die.

import random

def rolling_dice(n):
    # printing your random number
    print("Your random dice number is: "+ str(random.randrange(1,n)))

def main():
    print("This is the game rolling the dice. First: ")
    dice_sides = int(input("How many sides is your dice? "))

    playing = input("would you like to play rolling the dice? (Y/N) ")

    while playing == "Y":
        rolling_dice(dice_sides)
        playing = input("would you like to play again rolling the dice? (Y/N) ")

if __name__ == "__main__":
    main()