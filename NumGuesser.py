import random

hard = 5
easy = 10
print("Welcome to the number guessing game!\nI'm thinking fo a number between 0 and 100")

def select_level():
  diff = " "
  while diff != "easy" and diff != "hard":
    diff = input("Choose a difficulty. Type: 'easy' or 'hard': ")
  if diff == "easy":
    return(easy)
  if diff == "hard":
    return(hard)

def game():
  answer = random.randint(0,100)
  numb_guesses = select_level()
  user_guess = int(input("Make a guess: "))
  while numb_guesses != 1:
    if user_guess > answer:
      print("Too high.")
    elif user_guess < answer:
      print("Too low.")
    else:
      print("Thats correct! You win.")
      return
    numb_guesses -= 1
    print("You have",numb_guesses,"guesses remaining to guess the number.")
    user_guess = int(input("guess a number: "))
  if numb_guesses == 1:
    print(f"You have no remaining guesses. answer:{answer}")

game()
