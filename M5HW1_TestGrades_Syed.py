# Test Grading Program
# 6/2617
# CTI-110 M5HW1 - Test Average and Grade
# Syed


def calcAverage( score1, score2, score3, score4, score5 ):
    average = ( score1 + score2 + score3 + score4 + score ) /5
    return average
def datermineGrade ( userScore) :
    if ( userScore < 60 ) :
        return "F"
    elif (userScore < 70 ):
     return "D"
    elif ( userScore <80 ) :
        return "C"
    elif ( userScore < 90 ) :
        return "B"
    elif (userScore < 101 ):
        return "A"
        
def askForScore():

    score1 = float (input("please enter score 1: ") )
    score2 = float (input("please enter score 2: ") )
    score3 = float (input("please enter score 3: ") )
    score4 = float (input("please enter score 4:" ) )                      
    score5 = float (input("please enter score 5: ") )

    return score1, score2, score3, score4, score5


def printTableofResults (score1, score2, score3, score4, score5 ):
    print (" Score\tLetter Grade" )

    print(str (score1 )   + "\t\t"   +  datermineGrade (score1 ),\
            str (score2)  + "\t\t"  +   datermineGrade (score2  ),\
            str (score3)  + "\t\t"  +   datermineGrade (score3  ),\
            str (score4 ) + "\t\t" +    datermineGrade(score4  ),\
            str (score5 ) + "\t\t" +    datermineGrade(score5 ), sep = "\n")
 
def  main():
    
    score1, score2, score3,score4, score5 = askForScore()
    print()
    
    printTableofResults (score1, score2, score3, score4, score5)
main()
