import time
from wonderwords import RandomWord

# Setup
blanks = []
lettersChosen = []
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

lives = 6
picCounter = 0
r = RandomWord()
gameWin = False

# generate a random word
wordToGuess = r.word()
print(wordToGuess)  # (for testing - remove in final version)

lettersInGeneratedWordList = list(wordToGuess)

# Correct way to initialize blanks
blanks = ['-' for _ in wordToGuess]

while picCounter <= 6:
    print(HANGMAN_PICS[picCounter])
    print("".join(blanks))
    print(f"Number of guesses left: {lives}")

    letterToGuess = input("Guess a letter -> ").lower()

    if letterToGuess in lettersChosen:
        print(f"You already guessed '{letterToGuess}'. Try again.")
        continue

    lettersChosen.append(letterToGuess)

    if letterToGuess in lettersInGeneratedWordList:
        for idx, char in enumerate(lettersInGeneratedWordList):
            if char == letterToGuess:
                blanks[idx] = letterToGuess
    else:
        lives -= 1
        picCounter += 1

    blanksToWord = "".join(blanks)

    if blanksToWord == wordToGuess:
        print(blanksToWord)
        gameWin = True
        break

if gameWin:
    print(f"Game Over, you win!")
else:
    print(HANGMAN_PICS[-1])
    print(f"Game Over. The word was '{wordToGuess}'.")
