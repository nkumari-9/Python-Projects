'''
Author: Neha Kumari
FileName: guessingGame_neha_02.py
Purpose: Guess a secret number from the range of numbers.
Revisions:
    00: Import math and random library.
    01: Announce and get the numbers input from the user
    02: Compute the number of guesses allowed based on math.log2() function.

'''
### STEP 1: Import math and random library
import math
import random
### STEP 2: Announce, prompt, & get response
print('Guess the Secret Number\n')
# announce
print('Enter the maximum number in the range:')
nMax=int(input())
print(f'\nTry to guess a secret number from 1 to {nMax} (inclusive).\n')
nGuesses=int(math.log2(nMax)+1)
#get secret number
ra_range=random.randrange(1,nMax)
### STEP 3: Check whether the guessed number is greater than, less than or equal to the secret number.
for i in range(nGuesses,0,-1):
    if i>1:
        print(f'You have {i} guesses available.')
    else:
        print(f'You have {i} guess available.')
    print('Enter your guess: ',end='')
    a=int(input())
    if ra_range>a:
        print(f'The secret number is greater than {a} .')
    elif ra_range<a:
        print('The secret number is less than',a,'.')
    else:
        print('You have guessed it correct!!')
        break
else:
    print(f'You are out of guesses. The secret number is {ra_range}.')



