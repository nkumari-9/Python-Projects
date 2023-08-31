'''
Author: Neha Kumari
FileName: knockKnockjokes_neha_03.py
Purpose: Program to tell knock knock jokes.
Revisions:
    00: Import shuffle from random
    01: Created the prompt_response() function
    02: Add clean() function to remove punctuations.
    03: Created check_valid_input() function.
'''
from random import shuffle
## Step 1: Created a list of jokes.
jokes = list()
## Step 2: Added 7 jokes by using append()method.
jokes.append(('Tank',"You're welcome!"))
jokes.append(('Cows say',"No! Cows say moo. Owls say hoo!"))
jokes.append(('Cash',"No thanks, I prefer Peanuts."))
jokes.append(('Etch',"Please sneeze into your elbow!"))
jokes.append(('Ya',"Yahoo! I’m happy to see you too!"))
jokes.append(('Boo',"Don't cry, it’s only a joke."))
jokes.append(('Dwayne',"Dwayne the tub before I dwown."))
# Calculated the length of jokes and shuffled it.
total_jokes=len(jokes)
shuffle(jokes)
## Step 3: Created a list of whos_there_variants.
whos_there_variants = ['whos there','who is there','who there','who dere','whos dere']
# Initialize the first prompt, first suggestion, and punctuation.
first_prompt='Knock-Knock'
suggest1="Who's there?"
punct="',.!?;\""

## Step 4: Define the functions clean(), prompt_response(), and check_valid_input().
def clean(s):
    '''
    This function takes the input of string
    Convert the string into list by removing the punctuations
    Returns the string by converting the list back to string
    '''
    return ''.join([c for c in s if c not in punct ])
def prompt_response(prompt,variants,suggest):
    '''
    This function takes the input of prompt, list of variants, and suggested value
    Calls the clean() function to remove punctuation from the input taken from the user
    Check whether the input is in variants list
    Returns True or False 
    '''
    print(prompt)
    response=input().lower()
    response_clean = clean(response)
    if response_clean in variants:
        return True
    else:
        print(f'The correct response is "{suggest}"')
        print('Try again\n')
        return False
def check_valid_input(num_jokes):
    '''
    This function takes the input of string
    Check whether the string is integer or not using try and except clause
    Returns True or False
    '''
    val=True
    try:
        num_jokes=int(num_jokes)
        if num_jokes>total_jokes or num_jokes<1:
            print(f'The number must be in range 1 to {total_jokes}')
            val=False
    except ValueError:
        print(f'The number must be in range 1 to {total_jokes}')
        val=False
    return val
        
    
print('Ready to tell a knock-knock joke!\n')
print(f'There are {total_jokes} available\n')
# Take input from user
num_jokes=input('How many jokes would you like me to tell? ')
# Call check_valid_input() function  
while not check_valid_input(num_jokes):
    num_jokes=input('How many jokes would you like me to tell? ')
print(f'\nReady to tell {num_jokes} jokes!\n')
# Slice the jokes based on user input
jokes=jokes[:int(num_jokes)]
for joke in jokes:
    second_prompt=joke[0]
    answer_variant = list()
    answer_variant.append(joke[0]+' who')
    answer_variant.append(joke[0].lower()+' who')
    suggest2= joke[0]+' who?'
    while not prompt_response(first_prompt,whos_there_variants,suggest1):
        continue
    while not prompt_response(second_prompt,answer_variant,suggest2):
        continue
    else:
        print(joke[1])
        print('\n')

print('\nThanks for playing!')
    
    

