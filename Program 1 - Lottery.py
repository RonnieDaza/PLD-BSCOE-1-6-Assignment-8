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
        # 19. If any of the conditions is true, then the userInputNumber2 is invalid. Display a message to the user stating that the number entered is invalid and try again.
        print("Invalid number. Please try again.")
        # 20. Ask the user again for the userInputNumber2 from 0 to 9.
        userInputNumber2 = int(input("Please enter the second number from 0 to 9: "))
    else:
        # 21. If the user entered a valid number, then add the userInputNumber2 to the userInputSelection.
        userInputSelection.append(userInputNumber2)
    
    # 22. Ask the user for the userInputNumber3 from 0 to 9.      
    userInputNumber3 = int(input("Please enter the third number from 0 to 9: "))
    # 23. Create a loop to test if the userInputNumber3 is in the userInputSelection already or if it is less than 0 or if it is greater than 9.
    while userInputNumber3 in userInputSelection or userInputNumber3<0 or userInputNumber3>9:
        # 24. If any of the conditions is true, then the userInputNumber3 is invalid. Display a message to the user stating that the number entered is invalid and try again.
        print ("Invalid number. Please try again.")
        # 25. Ask the user again for the userInputNumber3 from 0 to 9.
        userInputNumber3 = int(input("Please enter the third number from 0 to 9: "))
    else:
        # 26. If the user entered a valid number, then add the userInputNumber3 to the userInputSelection.
        userInputSelection.append(userInputNumber3)
    
    # 27. If the numbers in userInputSelection list matches the numbers in randomNumberSelection list, then the user wins. 
    if sorted(userInputSelection) == sorted(randomNumberSelection):
        # 28. Print a message stating that "Winner!" to the user.
        print("Winner!")
        # 29. Display the random numbers from the randomNumberSelection list.
        print(f"The lottery numbers are: {randomNumberSelection}.")
        # 30. Display the numbers entered by the user from the userInputSelection list.
        print(f"The numbers you entered are: {userInputSelection}.")
    else:
        # 31. If the numbers in userInputSelection list does not match the numbers in randomNumberSelection list, then the user loses.
        # 32. Print a message stating that "You lose." to the user.
        print("You lose.")
        # 33. Display the random numbers from the randomNumberSelection list.
        print(f"The lottery numbers are: {randomNumberSelection}.")
        # 34. Display the numbers entered by the user from the userInputSelection list.
        print(f"The numbers you entered are: {userInputSelection}.")
    
    # 35. Count the numbers entered by the user that matches the random numbers.
    # 36. Set the counter variable to 0.
    counter = 0
    # 37. Create a for loop to test if the numbers in the userInputSelection list matches with the numbers in the randomNumberSelection list.
    for number in userInputSelection:
        # 38. If the numbers in the userInputSelection list matches with the numbers in the randomNumberSelection list, then the counter variable will go up by 1.
        if number in randomNumberSelection:
            counter = counter+1
    
    # 39. The numbers in the userInputSelection list that matches with the numbers in the randomNumberSelection list are the numbers that are correctly guessed by the user. Print a message that displays it.
    print("You guessed " + str(counter) + " number(s) right.")

# 40. For us to use the whole program, we need to call the lotteryProgram().
lotteryProgram()

# 41. Create a def for winOrLose().
def winOrLose():
    # 42. Let the user enter "y" to continue or enter "n" to end the program.
    yesOrNo = input("Try again? Type 'y' if you want to try again or type 'n' if you want to close the program: ")
    # 43. If the user input is "y" then call the lotteryProgram() to start the program again.
    if yesOrNo == "y":
        lotteryProgram()
    else:
        # 44. If the user input is "n" then display the concluding message. End the program.
        print("Thank you for using this program.")
        sys.exit

# 45. For us to ask if the user will continue or not, we need to call the def winOrLose().
winOrLose()