# Number Guessing Game
# Author: Babu (for Shiv Ranajn)
import random

def play_game():
    low, high = 1, 100
    secret = random.randint(low, high)
    attempts = 0

    print(f"Hey Shiv Ranajn — I'm thinking of a number between {low} and {high}.")
    print("Try to guess it! Type 'quit' to exit.")

    while True:
        guess = input("Your guess: ").strip()
        if guess.lower() == 'quit':
            print(f"Bye Shiv Ranajn — the number was {secret}.")
            break

        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low. Try again.")
        elif guess > secret:
            print("Too high. Try again.")
        else:
            print(f"Nice! You guessed it in {attempts} attempts. Well played, Shiv Ranajn!")
            # Ask to play again
            again = input("Play again? (y/n): ").strip().lower()
            if again == 'y':
                play_game()
            else:
                print("Thanks for playing — bye!")
            break

if __name__ == "__main__":
    play_game()
