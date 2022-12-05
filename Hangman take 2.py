import random

def random_word():
    with open("better words") as file:
        words = file.read().split("\n")
        return words[random.randint(0, len(words))]

def get_guess_from_player(lenght):
    guess = input("Please enter either a 1 letter guess, or a full word guess.\nGuess here: ")
    while len(guess) != 1 and len(guess) != lenght:
        guess = input("Please enter either a 1 letter guess, or a full word guess.\nGuess here: ")
    return guess.lower()

def check_word_guess_from_player(guess, word, clue):
    goodBad = False
    for x in range(len(guess)):
            if guess[x] == word[x]:
                clue[x] = guess[x]
                goodBad = True
    return clue, goodBad

def create_emtpy_guess(comp_guess):
    output_list = []
    for letters in comp_guess:
        output_list.append("_ ")
    return output_list

def return_list_as_string(list):
    new_string = ""
    for x in list:
        new_string += x
    return (new_string)

def check_letter_guess_from_player(guess, word, clue):
    goodBad = False
    for x in range(len(word)):
            if guess == word[x]:
                clue[x] = guess
                goodBad = True
    return clue, goodBad

def display_hangman(lives):
    if lives == 10:
        print("""    
         ___________
                """)
    if lives == 9:
        print("""
        
        |   
        |  
        |    
        |    
        |___________
                """)
    if lives == 8:
        print("""
        
        |/     
        |    
        |     
        |    
        |___________
                """)
    if lives == 7:
        print("""
        ________
        |/     
        |    
        |     
        |    
        |___________
                """)
    if lives == 6:
        print("""
        ________
        |/     |
        |  
        |     
        |    
        |___________
                """)
    if lives == 5:
        print("""
        ________
        |/     |
        |      o
        | 
        |    
        |___________
                """)
    if lives == 4:
        print("""
        ________
        |/     |
        |      o
        |      | 
        |     
        |___________
                """)
    if lives == 3:
        print("""
        ________
        |/     |
        |     o
        |     |\ 
        |    
        |___________
                """)
    if lives == 2:
        print("""
        ________
        |/     |
        |     o
        |    /|\ 
        |    
        |___________
                """)
    if lives == 1:
        print("""
        ________
        |/     |
        |     o
        |    /|\ 
        |    / 
        |___________
                """)
    if lives == 0:
        print("""
        ________
        |/     |
        |     o
        |    /|\ 
        |    / \ 
        |___________
                """)




awnser = random_word()
clue_list = create_emtpy_guess(awnser)
lives = 11
counter = 0

while lives != 0:
    print(F"The awnser is in format ",return_list_as_string(clue_list))
    player_guess = get_guess_from_player(len(awnser))
    if awnser == player_guess:
        break
    elif len(player_guess) == 1:
        clue_list, good_bad = check_letter_guess_from_player(player_guess, awnser, clue_list)
    else:
        clue_list, good_bad = check_word_guess_from_player(player_guess, awnser, clue_list)

    if good_bad is False:
        lives -= 1
    display_hangman(lives)
    print(f"\nyou have {lives} lives remaining")
    counter += 1

if lives != 0:
    input(f"Well done you saved the hangman, you had {lives} lives left and took {counter} turns to do it")
else:
    display_hangman(lives)
    input("You lose, you let the hangman die")
