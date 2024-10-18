import random

#Loop
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')

    # # ask: roll dice:
    #if user enters y
    #   generate 2 random nums
    #   print them
    #if user enters n
    #   print thank you message 
    #   Terminate
    #else
    #   print invalid choice