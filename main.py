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

user_choice = int(input("0 for rock, 1 for paper, 2 for scissors\n Enter your choice\n"))
shape_list = [rock, paper, scissors]
if user_choice<3 or user_choice>=0: # for invalid numbers other than 0,1,2
    print(shape_list[user_choice])
computer_choice = random.randint(0,2)
print(shape_list[computer_choice])

if user_choice>=3 or user_choice<0: # for invalid numbers other than 0,1,2
    print("You loose, wrong choice \n")

elif user_choice == 0 and computer_choice == 2:
    print("You win")

elif user_choice == computer_choice:
    print("Draw")

elif user_choice == 2 and computer_choice ==0:
    print("You loose")

elif user_choice < computer_choice:
    print("You loose")

elif user_choice > computer_choice:
    print ("You win")









# if user_choice == 0:
#     if computer_choice == 1:
#         print(rock, "\n Computer choice")
#         print(paper,"\n")
#         print("YOU LOSE \n")
#     elif computer_choice == 2:
#         print(rock, "\n Computer choice")
#         print(scissors, "\n")
#         print("YOU WIN \n")
#     else:
#         print(rock, "\n Computer choice")
#         print(rock, "\n")
#         print("DRAW \n")
# elif user_choice == 1:
#     if computer_choice == 0:
#         print(paper, "\n Computer choice")
#         print(rock, "\n")
#         print("YOU WIN \n")
#     elif computer_choice == 2:
#         print(paper, "\n Computer choice")
#         print(scissors, "\n")
#         print("YOU LOSE \n")
#     else:
#         print(paper, "\n Computer choice")
#         print(paper, "\n")
#         print("DRAW\n")
# elif user_choice == 2:
#     if computer_choice == 0:
#         print(scissors, "\n Computer choice")
#         print(rock, "\n")
#         print("YOU LOSE \n")
#     elif computer_choice == 1:
#         print(scissors, "\n Computer choice")
#         print(paper, "\n")
#         print("YOU WIN \n")
#     else:
#         print(scissors, "\n Computer choice")
#         print(scissors, "\n")
#         print("DRAW\n")
# else:
#     print("wrong choice \n")

