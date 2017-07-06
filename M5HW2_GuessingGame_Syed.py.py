

# Guessing Game  
# 6/26/17
# Guessing Game  
# 7/6/17
# CTI-110 M5HW2 - Random Number Guessing Game
# Syed


import random
randomNumber = random.randrange(0,100)
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Your guess pleas: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>100:
        print("Too lower")
    elif userInput<0:
        print("Too higher")
    elif userInput>randomNumber:
        print("Too lower")
    elif userInput < randomNumber:
        print("Too higher")

print("End of program")
