import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

print("Lets play Rock Paper Scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("The number you chose is invalid, You Lose!")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print(f"Computer chose")
  print(game_images[computer_choice])

  #user display
  if user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
  elif user_choice == 2 and computer_choice == 1:
    print("You Win!")

  #computer display
  if user_choice == 2 and computer_choice == 0:
    print("You Lose!")
  elif user_choice == 0 and computer_choice == 1:
    print("You Lose!")
  elif user_choice == 1 and computer_choice == 2:
    print("You Lose!")

  #Tie
  if user_choice == computer_choice:
    print("Tie")