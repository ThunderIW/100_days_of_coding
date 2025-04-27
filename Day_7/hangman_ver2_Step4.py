import random

from wonderwords import RandomWord
wordList = RandomWord()
wordToGuess = wordList.word()

##word_List=['aardvark','baboon','camel']
chosen_word_to_Guess=wordToGuess
print(chosen_word_to_Guess)

placeholder=['-' for _ in   chosen_word_to_Guess]

display="".join(placeholder)


guesses_left=6
hangman_pic=0;
game_over=False
HANGMAN_PICS = [r'''
  +---+
      |
      |
      |
     ===''', r'''
  +---+
  O   |
      |
      |
     ===''', r'''
  +---+
  O   |
  |   |
      |
     ===''', r'''
  +---+
  O   |
 /|   |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''', r'''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']


while not game_over:
    print(HANGMAN_PICS[hangman_pic])
    print(f"*******************{guesses_left}/6 LIVES LEFT*******************")
    print(display)
    guess=str(input("Guess a letter:")).lower()
    if guess in chosen_word_to_Guess:
        for  idx, char in enumerate(chosen_word_to_Guess):
            if  char == guess:
                placeholder[idx]=char

                display="".join(placeholder)


    elif guess not in chosen_word_to_Guess:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        guesses_left-=1
        hangman_pic+=1

    print(display)

    if "-" not in display:
        print(f"*******************IT WAS {chosen_word_to_Guess}! which you  guessed correctly YOU WIN *******************")
        game_over=True


    if guesses_left==0:
        print(f"*******************The  word that was selected {chosen_word_to_Guess}! YOU LOSE *******************")
        game_over=True









