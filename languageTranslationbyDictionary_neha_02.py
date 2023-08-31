'''
Author: Neha Kumari
FileName: languageTranslationbyDictionary_neha_02.py
Purpose: Program to translate colors from English to other languages using dictionary.
Revisions:
    00: Add the keys with empty dictionary and than update the dictionary in different languages.
    01: Announce and get the input from the user and check whether the word exists in dictionary and translate the word.
    02: Created a while loop to run until the user enters nothing.

'''
### STEP 1: Initialized the dictionary named as colors for red, green, yellow and blue colors.
colors={}
colors['red']={}
colors['red'].update({'french':'rouge'})
colors['red'].update({'spanish':'rojo'})
colors['red'].update({'german':'rot'})
colors['green']={}
colors['green'].update({'french':'vert','spanish':'verde','german':'grun'})
colors['yellow']={}
colors['yellow'].update({'french':'jaune','spanish':'amarillo','german':'gelb'})
colors['blue']={}
colors['blue'].update({'french':'bleu','spanish':'azul','german':'blau'})
print('Language Translator\n')
word=True
### STEP 2: Create a while Loop to check whether the word entered is null or not.
while word:
    print('\nAvailable English words are:',end=' ')
    for k in colors.keys():
        print(k,end='; ')
    print('\n')
    #announce and take input from user
    word=input('Please enter a color in English: ').lower()
### STEP 3: Check if the word entered exists in dictionary 'colors'.
    if(word in colors.keys()):
        lang=True
        while(lang):
            print('\nAvailable language translations are:',end=' ')
            for k in colors[word].keys():
                print(k,end='; ')
            print('\n')
            lang=input('Please enter a language from the list: ').lower()
### STEP 4: Check if the language entered exists in dictionary 'colors'.
            if lang not in colors[word].keys():
                #lang=True
                print(f'The {lang} translation of {word} not found in dictionary')
                ## Add a new word in new language for the existing colors to the dictionary.
                print(f'Would you like to add {lang} translation of {word} to the dictionary? <y>es or <n>o ',end='')
                chk_input = input().lower()
                if chk_input=='n':
                    lang=True
                elif chk_input=='y':
                    print(f'What is the {lang} translation of the word {word}')
                    lang_trans=input().lower()
                    temp={}
                    temp[lang]=lang_trans
                    colors[word].update(temp)
                    #print(colors)
                    break
            else:
                print(f'\nThe word "{word}" in {lang} is "{colors[word][lang]}"')
                break
                
### STEP 4: Check if the word entered exists in dictionary 'colors' and if not add the new color in the dictionary.    
    elif(word not in colors.keys() and word !=''):
        print(f'The word "{word}" was not found in English dictionary')
        print(f'Would you like to add {word} to the dictionary? <y>es or <n>o ',end='')
        chk_input = input().lower()
        if chk_input=='n':
            continue
        elif chk_input=='y':
             print(f'What language you would like to translate {word} in? <S>panish or <F>rench or <G>erman ',end='')
             chk_lang = input().lower()
             if chk_lang=='s':
                 print(f"What is the Spanish word for '{word}'? ",end='')
                 spanish_tran = input().lower()
                 colors[word]={}
                 temp={}
                 temp['spanish']=spanish_tran
                 colors[word].update(temp)

             elif chk_lang=='f':
                 print(f"What is the French word for '{word}'? ",end='')
                 french_tran = input().lower()
                 colors[word]={}
                 temp={}
                 temp['french']=french_tran
                 colors[word].update(temp)
                 
             elif chk_lang=='g':
                 print(f"What is the German word for '{word}'? ",end='')
                 german_tran = input().lower()
                 colors[word]={}
                 temp={}
                 temp['german']=german_tran
                 colors[word].update(temp)
             elif chk_lang not in ('s','f','g'):
                print("Not a valid language selection")
            
            
    else:
        break
    
print('Exiting ...')
