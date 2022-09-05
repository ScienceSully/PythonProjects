import random
computer_score = 0
user_score = 0
winner = ""

you = "You win!"
me = "I win!"

keep_playing = input("Do you want to play a game? Y/N")

while keep_playing == "Y":
  computer_number = random.randint(1,3)
  if computer_number == 1:
    computer_choice = "Rock"
  if computer_number == 2:
    computer_choice = "Paper"
  if computer_number == 3:
    computer_choice = "Scissors"  
  user_choice = input("Rock, Paper, Scissors. Shoot!")
  
  if computer_choice == "Rock" and user_choice == "Scissors":
    print(me)
    computer_score += 1
    
  if computer_choice == "Rock" and user_choice == "Paper":
    print(you)
    user_score += 1
    
  if computer_choice == "Rock" and user_choice == "Rock":
    print("Tie")
    
  if computer_choice == "Paper" and user_choice == "Scissors":
    print(you)
    user_score += 1
    
  if computer_choice == "Paper" and user_choice == "Rock":
    print(me)
    computer_score += 1
    
  if computer_choice == "Paper" and user_choice == "Paper":
    print("Tie")
    
  if computer_choice == "Scissors" and user_choice == "Scissors":
    print("Tie")
    
  if computer_choice == "Scissors" and user_choice == "Rock":
    print(you)
    user_score += 1
    
  if computer_choice == "Scissors" and user_choice == "Paper":
    print(me)
    computer_score += 1
  
  print("I picked", computer_choice)
  print("Computer: {0}".format(computer_score), "You: {0}".format(user_score))
  keep_playing = input("Do you want to keep playing? Y/N")
print("Goodbye :)")
