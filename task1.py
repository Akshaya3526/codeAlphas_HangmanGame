
import random

# Predefined list of 5 words
word_list = ["apple", "chair", "house", "table", "plant"]

# Randomly choose a word
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a display version of the word with underscores
display_word = ["_"] * len(secret_word)

print("🎉 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Incorrect! You have {max_attempts - incorrect_guesses} guesses left.\n")

# Game end
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
