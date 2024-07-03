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


choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper,2 for Scissors\n->"))
Computer_choice = random.randint(0,2)


if choice == 0 and Computer_choice == 2 :
    print("You chose")
    print(rock)

    print('Computer chose')
    print(scissors)

    print("You Win")
elif choice == 0 and Computer_choice == 1 :
    print("You chose")
    print(rock)

    print('Computer chose')
    print(paper)

    print('You Lose')

elif choice == 1 and Computer_choice == 1 :
    print("You chose")
    print(paper)

    print("Computer chose")
    print(paper)

    print("It's a tie")


elif choice == 1 and Computer_choice == 2 :
    print("You chose")
    print(paper)

    print('Computer chose')
    print(scissors)
    print("You Lose")


elif choice == 1 and Computer_choice == 0 :
    print("You chose")
    print(paper)

    print('Computer chose')
    print(rock)


    print('You lose')


elif choice == 2 and Computer_choice == 1 :
    print("You chose")
    print(scissors)

    print('Computer chose')
    print(paper)

    print('You Win')

elif choice == 2 and Computer_choice == 2 :
    print("You chose")
    print(scissors)

    print('Computer chose')
    print(scissors)

    print("It's a tie")

elif choice == 2 and Computer_choice == 0:
    print("You chose")
    print(scissors)

    print('Computer chose')
    print(rock)

    print('You lose')

else:
    print("You Type invalid number, you lose ")



