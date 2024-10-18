import random

answer = random.randint(1, 100)

while True:
    try:
        choice = int(input('Guess a number between 1 and 100: '))
        
        # if choice not
        if choice < answer:
            print('To low nerd')
        elif choice > answer:
            print('To high homie')
        elif choice == answer:
            print('Hellz ya, you got me')
            break
        else:
            print('numbers 1 and 100 silly goose')
    except ValueError:
        print('please enter a valid number .... bitch')