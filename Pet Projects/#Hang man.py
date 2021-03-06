#Hang man
import random

#Lists of words for the program to choose from
pack_1 = ['doubt', 'envy', 'greed', 'fury', 'sloth',
    'depression', 'disgust', 'fear', 'love', 'pity']
pack_2 = ['fly', 'ox', 'cougar', 'zebra', 'aardvark',
    'triceratops', 'crocodile', 'hippopotamus', 'dingo', 'spider']
pack_3 = ['revolutionary', 'physics', 'explicit', 'branch', 'inflation', 
    'radical', 'critical', 'monarch', 'harmony', 'sandwich']

# ASCII Art to visualise the number of lives (attempts)
hangman_life_stages = [
"""
     |===|
     O   |
    /|\  |
    /\   |
         |
    _____|
"""
,
"""
     |===|
     O   |
    /|\  |
    /    |
         |
    _____|
"""
,
"""
     |===|
     O   |
    /|\  |
         |
         |
    _____|
"""
,
"""
     |===|
     O   |
    /|   |
         |
         |
    _____|
"""
,
"""
     |===|
     O   |
     |   |
         |
         |
    _____|
"""
,
"""
     |===|
     O   |
         |
         |
         |
    _____|
"""
,
"""
     |===|
         |
         |
         |
         |
    _____|
"""
,
"""
      ===|
         |
         |
         |
         |
    _____|
"""
,
"""
         |
         |
         |
         |
         |
    _____|
"""
,
"""
          
          
          
          
          
    _____ 
"""
]

guessed_letters = set()
game_start_up = True
done = False
lives = 9

def complete_game():
    if all(letters == "_" for letters in split_word):
        print ("""Congratulations! 
        You correctly guessed the word without dying!""")
        done = True
        return correct_letters, split_word, lives, done
    elif lives == 0:
        print ("You lost!")
        done = True
        return correct_letters, split_word, lives, done


def hang_start():
    correct_letters = list("_" * len(word))
    print (hangman_life_stages[lives])
    game_start_up = False
    return correct_letters, game_start_up

def hang_game(correct_letters, lives):
    if all(letters == "_" for letters in split_word) or lives == 0:
        return complete_game()
    while hang_game:
        print ("=" * 25)
        print (correct_letters)
        guess = str.lower(input("\nEnter guess: "))
        if len(guess) == 1 and guess.isalpha(): 
            # Checks if the guess is 1 character long AND is a letter
            break
        else:
            print ("Invalid Input")
    return (check_right(split_word, guess, lives))

def check_right(split_word, guess, lives):
    if guess not in guessed_letters:
        if guess in split_word:
            for index, letter in enumerate(split_word):
                if letter == guess:      
                    correct_letters[index] = guess
                    split_word[index] = "_"
                else:
                    pass
            guessed_letters.add(guess)
            print (hangman_life_stages[lives])
            return (correct_letters, split_word, lives, done)
        else:
            lives -= 1
            print ("\nWrong!")
            guessed_letters.add(guess)
            print (hangman_life_stages[lives])
            return (correct_letters, split_word, lives, done)    
    else:
        print ("\nLetter already guessed")
        return (correct_letters, split_word, lives, done)

def word_choice(pack_choice):
    pack_choice = int(pack_choice)
    hangman_option = pack_choice
    if hangman_option == 1:
        word = random.choice(pack_1)
    elif hangman_option == 2:
        word = random.choice(pack_2)
    elif hangman_option == 3:
        word = random.choice(pack_3)
    split_word = list(word)
    return (hangman_option, split_word, word)

pack_choose = True
while pack_choose == True:
    pack_choice = input("What pack do you want to play? (1|2|3) ")
    if pack_choice == "1":
        hangman_option, split_word, word = word_choice(pack_choice)
        break
    elif pack_choice == "2":
        hangman_option, split_word, word = word_choice(pack_choice)
        break
    elif pack_choice == "3":
        hangman_option, split_word, word = word_choice(pack_choice)
        break
    else:
        print ("Invalid Input")
    
while not done:    
    if hangman_option == 1:
        if game_start_up == True:
            correct_letters, game_start_up = hang_start()
        else:
            pass
        correct_letters, split_word, lives, done = hang_game(correct_letters,lives)
    if hangman_option == 2:
        if game_start_up == True:
            correct_letters, game_start_up = hang_start()
        else:
            pass
        correct_letters, split_word, lives, done = hang_game(correct_letters,lives)
    if hangman_option == 3:
        if game_start_up == True:
            correct_letters, game_start_up = hang_start()
        else:
            pass
        correct_letters, split_word, lives, done = hang_game(correct_letters,lives)