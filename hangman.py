#!/usr/bin/env python

import getpass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_word():
    secret_word = None
    while not secret_word:
        secret_word = getpass.getpass("Enter a word to start the game: ")
        if len(secret_word) <= 2:
            print("Play again with a more difficult word!")
            quit()
    return secret_word

def is_the_letter_in_secret_word(letters_used, one_letter_guess, secret_word):
    secret_word = [x for x in secret_word]
    response = []
    if one_letter_guess in secret_word:
        for letter in secret_word:
            if letter in letters_used:
                response.append(letter)
            else:
                response.append('_')
        return ''.join(response)
    else:
        print(bcolors.FAIL + "The letter did not appear in the word, try again!" + bcolors.ENDC)
        
def guessing(secret_word, hangman, welldone):
    guess = None
    response = None
    letters_used = []
    count = 0
    while (response != secret_word) and (count <= 6):
        guess = raw_input("Type the letter or the word: ")
        if guess in letters_used:
            print(bcolors.FAIL + "You have already tried that letter, tut tut!" + bcolors.ENDC)
            count += 1
            print("{}{}{}").format(bcolors.FAIL, hangman[count], bcolors.ENDC)
            print("You have already tried these: {}").format(letters_used)
            continue
        else:
            letters_used.append(guess)
        if len(guess) <= 1:
            response = is_the_letter_in_secret_word(letters_used, guess, secret_word)
            if response == secret_word:
                print(bcolors.OKGREEN + secret_word + bcolors.ENDC)
                print(bcolors.OKGREEN + "{}" + bcolors.ENDC).format(welldone)
                quit()
            elif response:
                print(bcolors.OKGREEN + "This is what you have so far -> {}" + bcolors.ENDC).format(response)
                last = response
            else:
                count += 1
                print("{}{}{}").format(bcolors.FAIL, hangman[count], bcolors.ENDC)
                print("You have already said these: {}").format(letters_used)
                if last:
                    print(bcolors.OKGREEN + "This is what you have so far -> {}" + bcolors.ENDC).format(last)
        elif guess == secret_word:
            print(bcolors.OKGREEN + "{}" + bcolors.ENDC).format(welldone)
            quit()
        else:
            count += 1
            print("{}{}{}").format(bcolors.FAIL, hangman[count], bcolors.ENDC)
            print(bcolors.FAIL + "Wrong word!" + bcolors.ENDC)
            print("You have already said these: {}").format(letters_used)

def main():

    welldone = """
 __      __         .__   .__    ________                            _____.___.               ._.
/  \    /  \  ____  |  |  |  |   \______ \    ____    ____    ____   \__  |   |  ____   __ __ | |
\   \/\/   /_/ __ \ |  |  |  |    |    |  \  /  _ \  /    \ _/ __ \   /   |   | /  _ \ |  |  \| |
 \        / \  ___/ |  |__|  |__  |    `   \(  <_> )|   |  \\  ___/   \____   |(  <_> )|  |  / \|
  \__/\  /   \___  >|____/|____/ /_______  / \____/ |___|  / \___  >  / ______| \____/ |____/  __
       \/        \/                      \/              \/      \/   \/                       \/
"""

    hangman = (
"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")
    secret_word = get_word()
    print("Pass the device to the guessers!")
    print("The word is {} chracters").format(len(secret_word))
    print("_"*len(secret_word))
    guessing(secret_word, hangman, welldone)

if __name__ == "__main__":

    main()