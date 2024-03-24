"""

Hangman Wiki:

The origins of Hangman are obscure meaning not discovered, but it seems to have arisen in Victorian times, 
 says Tony Augarde, author of The Oxford Guide to Word Games. The game is mentioned in Alice Bertha Gomme’s 
Traditional Games in 1894 under the name Birds, Beasts and Fishes. The rules are simple; a player writes down the 
first and last letters of a word and another player guesses the letters in between. In other sources, [where?] the 
game is called Gallows, The Game of Hanging, or Hanger.

Implementation:

This is a simple Hangman game using Python programming language. Beginners can use this as a small project to boost 
their programming skills and understanding logic.

The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this 
ability, so line 1 in program imports it. The Game: Here, a random word (a fruit name) is picked up from our 
collection and the player gets limited chances to win the game. When a letter in that word is guessed correctly, 
that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all 
the chances are over. For convenience, we have given length of word + 2 chances. For example, word to be guessed is 
mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

"""

import random


class Hangman:
    def __init__(self):
        self.max_attempts = 6
        self.current_attempts = 0
        self.secret_word = Word().get_word()
        self.guessed_letters = []

    def display_word(self):
        displayed_word = ''
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += '_'
        return displayed_word

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You've already guessed this letter.")
            return

        self.guessed_letters.append(letter)

        if letter not in self.secret_word:
            self.current_attempts += 1
            print("Incorrect guess.")

        print("Word:", self.display_word())
        print(f"Attempts left: {self.max_attempts - self.current_attempts}")

        if self.check_win():
            print("Congratulations! You've guessed the word.")
        elif self.current_attempts == self.max_attempts:
            print("Sorry, you're out of attempts. The word was:", self.secret_word)

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)


class Word:
    def __init__(self):
        self.words = ["hangman", "python", "computer", "programming", "language", "artificial", "intelligence"]

    def get_word(self):
        return random.choice(self.words)


def main():
    game = Hangman()
    print("Welcome to Hangman!")
    print("Word:", game.display_word())

    while not game.check_win() and game.current_attempts < game.max_attempts:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            game.guess_letter(guess)
        else:
            print("Please enter a single letter.")


if __name__ == "__main__":
    main()

