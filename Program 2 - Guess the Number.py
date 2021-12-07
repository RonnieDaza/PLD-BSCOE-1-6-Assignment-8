# Program 2: Guess the Number
# Generate 1 random number (0-100).
# Ask the user to guess the number.
# Display "Greater than" if the inputted number is greater than the random number.
# Display "Less than" if the inputted number is less than the random number.
# Repeat asking the user until the random number has been guessed correctly.

# Steps
# 1. Import random.
import random

# 2. Get a random number from 0 to 100.
randomNumber = random.randint(0,100)

# 3. Ask the user to guess the random number from 0 to 100.
userInput = int(input("Please guess the random number from 0 to 100: "))

# 4. Create a loop to test if the userInput does not match the randomNumber.
while userInput != randomNumber: