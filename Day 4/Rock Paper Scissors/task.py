import random

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

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

possibilities = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("What do you choose? \nType 0 for Rock, \n1 for Paper, \n2 for Scissors.\n")
user_choice = int(user_choice)
computer_choice = random.randint(0, 2)


# function to print in blue color
def print_color(color, text):
    print(color + text + RESET)


if user_choice == computer_choice:
    print("It's a DRAW!")
elif user_choice == 0 and computer_choice == 2:
    print("You WIN!")
elif user_choice == 1 and computer_choice == 0:
    print("You WIN!")
elif user_choice == 2 and computer_choice == 1:
    print("You WIN!")
else:
    print(f"{RED}You lose!{RESET}")

print("You chose:")
if user_choice == 0:
    print_color(BLUE, rock)
elif user_choice == 1:
    print_color(BLUE, paper)
else:
    print_color(BLUE, scissors)

print("Computer chose:")
if computer_choice == 0:
    print_color(GREEN, rock)
elif computer_choice == 1:
    print_color(GREEN, paper)
else:
    print_color(GREEN, scissors)
