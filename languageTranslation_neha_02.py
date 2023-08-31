'''
Author: Neha Kumari
FileName: languageTranslation_neha_02.py
Purpose: Program to translate words from English to French and vice-versa.
Revisions:
    00: Create two lists of english and french words.
    01: Announce and get the input from the user and check whether the word exists in english or french list and translate the word.
    02: Created a while loop to run until the user enters nothing.

'''
### STEP 1: Initialized english and french words lists.
english = ['chicken','salt','apple','earth','bean','water','milk']
french = ['poulet','sel','pomme','terre','haricot','eau','lait']
#announce and take input from user
print('Program to translate words from English to French and vice-versa\n')
word = input('Enter an English or French word to translate: ').lower()
### STEP 2: Create a while Loop to check whether the word entered is null or not.
while word:
### STEP 3: Check if the word entered exists in english or french list.
    if word in english:
        french_word=french[english.index(word)]
        print(f"The English word '{word}' is '{french_word}' in French\n")
        word = input('Enter an English or French word to translate: ').lower()
    elif word in french:
        english_word=english[french.index(word)]
        print(f"The French word '{word}' is '{english_word}' in English\n")
        word = input('Enter an English or French word to translate: ').lower()
### STEP 4: If the word does not exist in both the list, then ask user whether they want to add the word in the list.
    else:
        print(f"The word '{word}' was not found in English or French word lists")
        print(f'Would you like to add {word} to the lists? <y>es or <n>o ',end='')
        chk_input = input().lower()
        if chk_input=='n':
            word = input('\nEnter an English or French word to translate: ').lower()
        elif chk_input=='y':
             print(f'What language is {word} in? <E>nglish or <F>rench ',end='')
             chk_lang = input().lower()
             if chk_lang=='e':
                 english.append(word)
                 print(f"What is the French word for '{word}'? ",end='')
                 french_tran = input().lower()
                 french.append(french_tran)
                 word = input('\nEnter an English or French word to translate: ').lower()
             elif chk_lang=='f':
                 french.append(word)
                 print(f"What is the English word for '{word}'? ",end='')
                 english_tran = input().lower()
                 english.append(english_tran)
                 word = input('\nEnter an English or French word to translate: ').lower()
             
                 
print('Exiting ...')
