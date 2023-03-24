# Imports
import random
from hangman_words import word_list
from hangman_art import stages, logo

# Variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed = []

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Logo
print(logo)
print("- " * 24)
print()

# Loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print()
    
    # Check already guessed
    if guess in guessed:
        print(f"You've already guessed '{guess}'\n")
        continue
    else:
        guessed.append(guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(
            f"You guessed '{guess}', that's not in the word. You lose a life.\n"
        )
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.\n")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    # ASCII Art
    print(stages[lives])
