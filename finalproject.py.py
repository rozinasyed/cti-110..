#Final project
#Python Quiz game
#Syed
#7.19.17
#2017SU Web, Pgm, & Db Foundation (CTI-110-1001)




x = 0
score = x
def begin():
 print("")

print("Hello \n")

name = input('WHAT IS YOUR NAME? ')
print ('\n HI THERE ' + name + '! LET''S PLAY A GAME!\n')
print ('I will ask you 10 questions and give you three choices for each question.\n\nYou select which choice is the correct answer. Eg. A, B or C\n')

print ('\n-----------------------------------------------------------\n')
    



                                                      


print ('QUESTION 1: WHAT IS THE LARGEST OCEAN IN THE WORLD?\n')
print ('A. The Indian Ocean')
print ('B. The Pacific Ocean')
print ('C. The Atlantic Ocean')
print ('')

Q1answer = "b"
Q1response= input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!...The Pacific Ocean')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')


                                                        


print ('QUESTION 2: AUSTRALIA is a ...\n')
print ('A. continent')
print ('B. island')
print ('C. very hot place')
print ('')

Q2answer = "a"
Q2response= input('Your answer : ')

if (Q2response != Q2answer):
    print ('Sorry, that is incorrect!...Right answer is AUSTRALIA is acontinent ')
else:
    print ('Well done! ' + Q2response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')



print ('QUESTION 3: How many legs does an Octopus have?\n')
print ('A. 5')
print ('B. 8')
print ('C. 3')
print ('')

Q3answer = "a"
Q3response= input('Your answer : ')

if (Q3response != Q3answer):
    print ('Sorry, that is incorrect!....Right answer is Octopus have 5 legs')
else:
    print ('Well done! ' + Q3response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                           


print ('QUESTION 4: Who is the 45th president of the United States?\n')
print ('A. Barack Obama')
print ('B. Hillary Clinton')
print ('C. Donald Trump')
print ('')

Q4answer = "c"
Q4response= input('Your answer : ')

if (Q4response != Q4answer):
    print ('Sorry, that is incorrect!...Right answer is  45th president is Donald Trump')
else:
    print ('Well done! ' + Q4response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                          


print ('QUESTION 5: Where was Bil Gates born?\n')
print ('A. Florida')
print ('B. New york')
print ('C. Washington')
print ('')

Q5answer = "c"
Q5response= input('Your answer : ')

if (Q5response != Q5answer):
    print ('Sorry, that is incorrect! ...Right answer is Washington')
else:
    print ('Well done! ' + Q5response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                           

print ('QUESTION 6: Grand Central Terminal, Park Avenue, New York is the world,s?\n')
print ('A. largest railway station')
print ('B. Highest railway station')
print ('C. longest railway station')
print ('')

Q6answer = "b"
Q6response= input('Your answer : ')

if (Q6response != Q6answer):
    print ('Sorry, that is incorrect! ...Right answer is Highest railway station')
else:
    print ('Well done! ' + Q6response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                    


print ('QUESTION 7: "True or False... The Eiffel Tower is not in France?\n')
print ('A. True')
print ('B. False')
print ('')

Q7answer = "a"
Q7response= input('Your answer : ')

if (Q7response != Q7answer):
    print ('Sorry, that is incorrect! ...Right answer is France')
else:
    print ('Well done! ' + Q7response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                


print ('QUESTION 8: "True or False... The Atlantic Ocean is the biggest ocean on Earth?\n')
print ('A. True')
print ('B. False')
print ('')

Q8answer = "b"
Q8response= input('Your answer : ')

if (Q8response != Q8answer):
    print ('Sorry, that is incorrect! ...Right answer is Pacific Ocean')
else:
    print ('Well done! ' + Q8response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')

                         

print ('QUESTION 9: "True or False...  The human skeleton is made up of less than 100 bones?\n')
print ('A. True')
print ('B. False')
print ('')

Q9answer = "b"
Q9response= input('Your answer : ')

if (Q9response != Q9answer):
    print ('Sorry, that is incorrect! ...Right answer is 206')
else:
    print = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                 

print ('QUESTION 10: "True or False...  Spiders have six legs?\n')
print ('A. False')
print ('B. True')
print ('')

Q10answer = "a"
Q10response= input('Your answer : ')

if (Q10response != Q10answer):
    print ('Sorry, that is incorrect! ...Right answer is 8')
else:
    print ('Well done! ' + Q10response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


                                

print ('Your Total score is ' + str(score) + ' out of 10' )

print("I hope so you enjoy the game")




print("DO YOU WANT PLAY AGAIN")


while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
if answer == 'y':
          begin
else:
        print ('Goodbye')
           

       
