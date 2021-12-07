# Program 1: Lottery
# Create a program that asks 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9).
# Display "Winner" if all 3 input numbers matched the generated numbers.
# Display "You lose" if not.
# Display "Try Again y/n" after each game.
# If the user enter "y" the user will play again.
# If the user enter "n" the program will exit.

# Steps
# 1. Import random.
import random
# 2. Import sys.
import sys

# 3. Create a def for lotteryProgram().
def lotteryProgram():
    
    # 4. Create an empty list to store the 3 random numbers.
    randomNumberSelection = []

    # 5. Get the randomNumber1 from 0 to 9.
    randomNumber1 = random.randint(0,9)
    # 6. Add the randomNumber1 to the randomNumberSelection.
    randomNumberSelection.append(randomNumber1)

    # 7. Get the randomNumber2 from 0 to 9.
    randomNumber2 = random.randint(0,9)