import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print('Welcome to Guess the Number Game!')
    print("You have select a number between 1 to 100. Try to guess it!")
    while not guessed:
        guess = int(input('Enter your guess number:'))
        attempts += 1
        if guess < secret_number:
            print('your guess number is low! Try agian')
        elif guess > secret_number:
            print('your guess number is high! Try agian')
        else:
            guessed = True
            print(f'Congratulations your guess number is {secret_number} in {attempts} attemps times.')

    play_again = input('Do you want to play again(yes/no)?')
    if play_again == 'yes':
        guess_the_number()
    else:
        print('Thanks for playing')

# main function
guess_the_number()