import time
import random as ran

print("""You are in a land full of dragons.
      In front of you, You see two caves. 
      In one cave, the dragon is friendly and will share his treasure with you.
      The other dragon is greedy and hungry, and will eat you on sight.""")

while True:
    print("Which cave will you go into? (1 or 2)")
    cave=ran.randint(1,2)

    choice_num=int(input())
    
    time.sleep(1)
    print("You approach the cave . . .")
    time.sleep(2)
    print("It is dark and spooky . . .")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws")
    print("and . . .")
    time.sleep(4)
    
    if choice_num == cave :
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")
    
    print("Do you want to play again? (yes or no)")

    answer=input()

    if answer.lower() == "yes" :
        continue
    if answer.lower() == "no" :
        break
    