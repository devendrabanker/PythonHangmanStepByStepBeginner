#Goal : This is the program is to play Hangman

#Steps:
# 1. Program has to randomly select a word from a list of words
# 2. Program has to show ****(based on words length) in place of word for user to guess
# 3. User has to input leter for guessing the word
# 4. if letter is present in the word
# 4.1 Program has to replace the letter in the word and show 
# 5. if user guess the word within 8 attempts => You Win!
# 6. if letter is not present in the word
#     6.1 Program has to show hangman picture based on failed attempt count
#     6.2 Program has to provide 8 attempts
#     6.3 if user can not guess within 8 attempts then => You Loose!


import random

# 1. Program has to randomly select a word from a list of words

Words = [ "apple", "blue", "peach", "watermelon","orange", "mango", "banana"]
#           0       1       2       3               4       5       6
#RandomIndex => 0-6
RandomIndex = random.randint(0, 6)
#print(f"RandomIndex = {RandomIndex}")
#print(f"Selected Word = {Words[RandomIndex]}")
ProgramSelectedRandomWord=Words[RandomIndex] 

# 2. Program has to show ****(based on words length) in place of word for user to guess

maskedWord = "*" * len(ProgramSelectedRandomWord)
print(f"MaskedWord = {maskedWord}")

GuessedWord = maskedWord #******
# 5. if user guess the word within 8 attempts => You Win!

attemptCount = 1

while attemptCount <=8:

    print(f"Attempt Number = {attemptCount}")
    # 3. User has to input leter for guessing the word
    inputCharacter = input("Enter the letter:")
    print(f"Input letter = {inputCharacter}")

    # 4. if letter is present in the word
    # 4.1 Program has to replace the letter in the word and show 
    if inputCharacter in ProgramSelectedRandomWord:
        list_GuessedWord = list(GuessedWord)
        for index,letter in enumerate(ProgramSelectedRandomWord):
            if letter == inputCharacter:
                list_GuessedWord[index] = letter
        
        GuessedWord = "".join(list_GuessedWord)
        print(f"GuessedWord = {GuessedWord}")
        
        if GuessedWord == ProgramSelectedRandomWord:
            print("You Win!!")
            break
    else:
# 6. if letter is not present in the word
#     6.1 Program has to show hangman picture based on failed attempt count
#     6.2 Program has to provide 8 attempts
#     6.3 if user can not guess within 8 attempts then => You Loose!
        if attemptCount == 1:
            print(" +---+")
            print("     |")
            print("     |")
            print("     |")
            print("    ===")
        elif attemptCount == 2:
            print(" +---+")
            print(" O   |")
            print("     |")
            print("     |")
            print("    ===")
        elif attemptCount == 3:
            print(" +---+")
            print(" O   |")
            print(" |   |")
            print("     |")
            print("    ===")
        elif attemptCount == 4:
            print(" +---+")
            print(" O   |")
            print("/|   |")
            print("     |")
            print("    ===")
        elif attemptCount == 5:
            print(" +---+")
            print(" O   |")
            print("/|\  |")
            print("     |")
            print("    ===")
        elif attemptCount == 6:
            print(" +---+")
            print(" O   |")
            print("/|\  |")
            print("/    |")
            print("    ===")
        elif attemptCount == 7:
            print(" +---+")
            print(" O   |")
            print("/|\  |")
            print("/ \  |")
            print("    ===")
        else:
            print("You Loose!!")
        attemptCount = attemptCount + 1
    









    
# 8 attempts
# 8 tries
# 8 iterations
# 8 loops




















    # apple
    # e
    # ****e
    
    # a p p l e
    # 0 a
    # 1 p 
    # 2 p 
    # 3 l
    # 4 e
    
    # apple
    # * * * * * 
    # e
    # ****e
    
    # banana
    # ******
    # a
    # *a*a*a
