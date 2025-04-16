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
game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
    print(game[choice])
computer_choice = random.randint(0, 2)

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == 0 and computer_choice == 2:
    print("Computer choose: ")
    print(game[computer_choice])
    print("You win!")
elif choice == 2 and computer_choice == 0:
    print("Computer choose: ")
    print(game[computer_choice])
    print("You lose!")
elif computer_choice < choice:
    print("Computer choose: ")
    print(game[computer_choice])
    print("You win!")
elif computer_choice > choice:
    print("Computer choose: ")
    print(game[computer_choice])
    print("You lose!")
elif computer_choice == choice:
    print("Computer choose: ")
    print(game[computer_choice])
    print("It's a draw")
