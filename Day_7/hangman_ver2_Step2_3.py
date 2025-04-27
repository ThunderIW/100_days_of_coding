import random

word_List=['aardvark','baboon','camel']
chosen_word_to_Guess=random.choice(word_List)
print(chosen_word_to_Guess)

placeholder=['-' for _ in   chosen_word_to_Guess]

display="".join(placeholder)
print(display)

while True:
    guess=str(input("Guess a letter:")).lower()
    for  idx, char in enumerate(chosen_word_to_Guess):
        if  char == guess:
            placeholder[idx]=char

            display="".join(placeholder)

    print(display)
    if "-" not in display:
        break








