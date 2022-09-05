import random
import os
clearing = os.system("cls")
computer_number = (random.randint(1, 100))
score = 1
user_number = input("Guess a number 1-100   ")
user_number = int(user_number)

while user_number != computer_number:
  if user_number < computer_number:
    print("Higher")
    score += 1
    user_number = input("Guess again--->")
    user_number = int(user_number)
    clearing

  if user_number > computer_number:
    print("Lower")
    score += 1
    user_number = input("Guess again--->")
    user_number = int(user_number)
    clearing

else:
    print("Congradulations!!!" + " It took you ", score, " guesses.")
