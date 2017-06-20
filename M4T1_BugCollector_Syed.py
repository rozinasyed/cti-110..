totalDays = 5
totalNumber0fBugs = 0

for currentDay in range(1, totalDays + 1 ):
    bugsCollected = int(input( "How many bugs were collected on day " + \
                               str( currentDay ) + ":" ) )
    totalNumber0fBugs +=bugsCollected
print()
print( "the total number of bugs collected for all", totalDays, "days is",\
       totalNumber0fBugs )

     
