import random
r=random.randint(1,10)
chances = 3
while(chances>0):
    guesses = int(input('Enter Your Guess : '))
    if guesses<r:
        print('Your Guess was too low')
    elif(guesses>r):
        print('Your Guess was too high')
    elif(guesses==r):
        print('Your Guess is correct')
        break
    chances = chances-1
if chances == 0:
    print('You have no more guesses. The correct guess is ' + str(r))
