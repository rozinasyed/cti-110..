# Pennies for Pay
# 6/23/2017
# CTI-110 M4HW2 - Pennies for Pay 
# Syed

numberofDaysWorked = int( input(" please enter how many days you worked:" ) )
totalNumberofpennies = 0

print( "Day\tSalary\n\t")
for currentDay in range( numberofDaysWorked ):
       penniesForTheDay = 2 ** currentDay
       totalNumberofpennies += penniesForTheDay
       print( currentDay + 1, "\t" , penniesForTheDay )
totalPay = totalNumberofpennies * 0.01
print( "\nTotal pay: $", totalPay, sep = " ")
     
    
