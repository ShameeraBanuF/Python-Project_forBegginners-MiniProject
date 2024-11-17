import random

def word_guessing_game():
    # List of words to choose from
    words = ["python", "developer", "coding", "hangman", "challenge", "computer", "programming"]
    word_to_guess = random.choice(words)
    guessed_letters = set()  # Track guessed letters
    attempts = 6  # Number of attempts
    
    print("Welcome to the Word Guessing Game!")
    print(f"I'm thinking of a word with {len(word_to_guess)} letters.")
    
    while attempts > 0:
        # Display the word with guessed letters and underscores for remaining letters
        display_word = [letter if letter in guessed_letters else "_" for letter in word_to_guess]
        print("Word to guess:", " ".join(display_word))
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Good job! That letter is in the word.")
            
            # Check if the player has guessed all letters
            if all(letter in guessed_letters for letter in word_to_guess):
                print("Congratulations! You've guessed the word:", word_to_guess)
                break
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print(f"Wrong guess! You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Out of attempts! The word was: {word_to_guess}")

# Run the game
word_guessing_game()
