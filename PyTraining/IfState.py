# First if statement 

Guess = input('Guess the number between 1 and 100: ')

# Convert the input to an integer

try:
    Guess = int(Guess)
    if Guess > 50:
            print('Too high')
    elif Guess < 50:
        print('Too low')
    else:
         print('Good guess!')

except ValueError:
     print('Input must be an integer')


