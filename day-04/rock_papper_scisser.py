# Rock
rock = ''''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper ='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])
# 0, 1,2
import random
computer_choice = random.randint(0,2)
# print(f"computer_chose {computer_choice}")
print("computer_chose:")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you type an invalid number. you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!") 
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw!")




