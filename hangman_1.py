import random

word_number=random.randint(2,5)
find_word=[]
blink='_'*word_number
num=0

for _ in range(word_number):
    word=chr(random.randint(97,122))
    find_word.append(word)

guess_word=''.join(find_word)

MAN_list=["""
 +---+
     |
     |
     |
    ===""","""
 +---+
 O   |
     |
     |
    ===""","""
 +---+
 O   |
 |   |
     |
    ===""","""
 +---+
 O   |
/|   |
     |
    ===""","""
 +---+
 O   |
/|\  |
     |
    ===""","""
 +---+
 O   |
/|\  |
/    |
    ===""","""
 +---+
 O   |
/|\  |
/ \  |
    ==="""]

while True:
    print("H A N G M A N")
    print(MAN_list[num])
    print("Missed letters: ")
    print(blink)
    print("Guess a letter")

    for chance in range(6):
        user_input=input()
        if user_input in guess_word:
            print(MAN_list[num])
            
        else:
            num+=1
            print(MAN_list[num]) 
                  
    
    
    Print("Do you want to play again? (yes or no)")
    answer=input()
    if answer is "yes":
        continue
    if answer is "no":
        break