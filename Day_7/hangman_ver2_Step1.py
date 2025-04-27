import random

word_List=['aardvark','baboon','camel']
chosen_word_to_Guess=random.choice(word_List)
print(chosen_word_to_Guess)

guess=str(input("Guess a letter:")).lower()
for  idx, char in enumerate(chosen_word_to_Guess):
    if  char == guess:
        print(char,"Right")
    else:
        print(char,"Wrong")



