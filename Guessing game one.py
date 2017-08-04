import random
exit = ''

while exit != 'x':
    a = random.randint(1, 9)
    exit = ''
    attempts = int(1)

    while True:
        guess = input('Attempt '+str(attempts)+'. Guess any number between 1 and 9?')
        if int(guess) == int(a):
            print('Well done, you guessed correctly, the random number was ' + str(a) + ', you guessed it in '+ str(attempts) + ' attempts.')
            break
        elif int(guess) < int(a):
            print('Hint - your guess is to low')
        elif int(guess) > int(a):
            print('Hint - your guess is to high')
        attempts = attempts + 1
    exit = input('''Press 'y' to play again, or 'x' to exit.''')