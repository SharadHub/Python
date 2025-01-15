# Problem 1: Reverse Digits of a Number
# Write a program that takes an integer input from the user and reverses its digits using a while loop. For example, if the input is 12345, the output should be 54321.
"""
n = int(input("enter the number"))

revNum = 0

while(n>0):
    revNum = revNum * 10 + n % 10
    n = n//10
print(revNum)
"""

# Problem 2: Guess the Number
# Write a program where the computer randomly selects a number between 1 and 50. The user has to guess the number. The program should provide hints like "too high" or "too low" and stop once the correct number is guessed. Use a while loop to keep the game running.
"""
import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess it?")
    print("------------------------------------------------------------")
    
    secret_num = random.randint(1, 50)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_num:
                print("Too low!")
            elif guess > secret_num:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {secret_num} correctly in {attempts} attempts.")
                break
            
            if abs(guess - secret_num) <= 3:
                print("Hint: You're very close!")
        
        except ValueError:
            print("Please enter a valid number.")
        
        if attempts == 5:
            if secret_num % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thank you for playing! Goodbye.")

play_game()
"""
# Problem 3: Sum of Digits
# Write a program that calculates the sum of the digits of a number entered by the user. For example, if the user inputs 456, the program should output 15 (since 4 + 5 + 6 = 15).
"""
num = input("enter the number:")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
"""




# Problem 4: Checking for Palindrome
# Write a program that checks if a given string is a palindrome (a word that reads the same backward as forward, like "radar"). Use a while loop to compare characters from both ends of the string.
"""
str = "madam"
name = "bishal"

if(str == str[::-1]):
    print("it is palindrome\n")
else:
    print("It is not palindrome")

if(name == name[::-1]):
    print("it is palindrome\n")

else:
    print("it is not palindrome")
"""

# Problem 5: Prime Number Validation
# Write a program that checks if a number entered by the user is a prime number. Use a while loop to test divisibility by all numbers from 2 up to the square root of the number.


num = int(input("enter the number:\n"))

if(num < 2):
    print(f"{num} is not prime number")

else:
    i = 2
    is_prime = True

    while i*i <= num:
        if(num % i ==0):
             is_prime = False
             break
        i += 1
    if is_prime:
        print(f"{num} is prime number\n")
    else:
        print(f"{num} is not prime number\n")








