"""
TASK 1: HANGMAN GAME
File: hangman_game.py
Description: A text-based word guessing game with 6 lives
"""

import random

def display_hangman(tries):
    """Display hangman stages"""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def hangman():
    """Main hangman game function"""
    
    # Predefined list of 5 words
    words = ["python", "coding", "intern", "program", "developer"]
    
    # Choose random word
    word = random.choice(words).upper()
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    guessed_letters = set()
    
    lives = 6
    
    print("=" * 50)
    print("🎮 WELCOME TO HANGMAN GAME!")
    print("=" * 50)
    print("Guess the word one letter at a time!")
    print(f"You have {lives} lives.\n")
    
    # Game loop
    while len(word_letters) > 0 and lives > 0:
        
        # Display hangman
        print(display_hangman(lives))
        
        # Show current status
        print(f"Lives remaining: {lives}")
        print(f"Used letters: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Show word progress
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print(f"Current word: {' '.join(word_list)}")
        
        # Get user input
        user_letter = input("\nGuess a letter: ").upper()
        
        # Validate input
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"\n✅ '{user_letter}' is in the word!")
            else:
                lives -= 1
                print(f"\n❌ '{user_letter}' is not in the word. You lose a life.")
        
        elif user_letter in guessed_letters:
            print("\n⚠️ You already guessed that letter. Try again.")
        
        else:
            print("\n❌ Invalid input. Please enter a single letter.")
        
        print("\n" + "-" * 50)
    
    # Game over
    print("\n" + "=" * 50)
    if lives == 0:
        print(display_hangman(lives))
        print(f"😢 YOU DIED! The word was: {word}")
    else:
        print(f"🎉 CONGRATULATIONS! You guessed the word: {word}")
    print("=" * 50)

if __name__ == "__main__":
    hangman()
    
    # Play again option
    while input("\nPlay again? (yes/no): ").lower().startswith('y'):
        print("\n")
        hangman()