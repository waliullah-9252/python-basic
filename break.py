import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed = False
    
    print("Welcome to Guess the Number game!")
    print("I've selected a number between 1 and 100. Try to guess it!")
    
    # Start the game loop
    while not guessed:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing!")

# Start the game
guess_the_number()
