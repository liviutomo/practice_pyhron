"""
Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer
in the minimum number of guesses.

The minimum number of guesses depends upon range. And the compiler must calculate the minimum number of guessing
depends upon the range, on its own. For this, we have a formula:-

 Minimum number of guessing = log2(Upper bound – lower bound + 1)
"""

import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter upper bound:- "))
chances = round(math.log(upper - lower + 1, 2))
x = random.randint(lower, upper)
print("\n\tYou've only ",
      chances,
      " chances to guess the integer! \n")

# Initialize the counter
count = 0

while count < chances:
    count += 1

    guess = int(input("Guess a number: - "))
    if guess not in [lower, upper]:
        print(f"You have to introduce a number between {lower} and {upper}")
        continue
    if x == guess:
        print(f"Congrats! You guess the number in {count} tries")
        break
    elif x > guess:
        print("The number you have to guess is higher.")
    elif x < guess:
        print("The number you have to guess is lower.")
if count > chances:
    print(f"The number you had to guess was {x}."
          f"Better luck next time.")
