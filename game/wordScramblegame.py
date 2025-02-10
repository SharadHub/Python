import random

def word_scramble():
    words = ["python", "programming", "developer", "computer", "keyboard"]
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))

    print(f"Unscramble the word: {scrambled}")

    guess = input("Your guess: ")

    if guess == word:
        print("Correct! Well done.")
    else:
        print(f"Wrong! The correct word was {word}.")

word_scramble()
