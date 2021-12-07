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
    # 8. Add the randomNumber2 to the randomNumberSelection.
    randomNumberSelection.append(randomNumber2)

    # 9. Get the randomNumber3 from 0 to 9.
    randomNumber3 = random.randint(0,9)
    # 10. Add the randomNumber3 to the randomNumberSelection.
    randomNumberSelection.append(randomNumber3)

    # 11. Create an empty list to store the 3 numbers that will be inputted by the user.
    userInputSelection = []

    # 12. Ask the user for the userInputNumber1 from 0 to 9.
    userInputNumber1 = int(input("Please enter the first number from 0 to 9: "))
    # 13. Create a loop to test if the userInputNumber1 is in the userInputSelection already or if it is less than 0 or if it is greater than 9.
    while userInputNumber1 in userInputSelection or userInputNumber1<0 or userInputNumber1>9:
        # 14. If any of the conditions is true, then the userInputNumber1 is invalid. Display a message to the user stating that the number entered is invalid and try again.
        print("Invalid number. Please try again.")
        # 15. Ask the user again for the userInputNumber1 from 0 to 9.
        userInputNumber1 = int(input("Please enter the first number from 0 to 9: "))
    else:
        # 16. If the user entered a valid number, then add the userInputNumber1 to the userInputSelection.
        userInputSelection.append(userInputNumber1)
    
    # 17. Ask the user for the userInputNumber2 from 0 to 9.
    userInputNumber2 = int(input("Please enter the second number from 0 to 9: "))
    # 18. Create a loop to test if the userInputNumber2 is in the userInputSelection already or if it is less than 0 or if it is greater than 9.
    while userInputNumber2 in userInputSelection or userInputNumber2<0 or userInputNumber2>9:






