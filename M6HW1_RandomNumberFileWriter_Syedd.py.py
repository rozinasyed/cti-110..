

# Random Number File Writer
# 7/12/17
# CTI-110 M6HW1 - Random Number File Writer
# Syed
#



import random

randfile = open("Randomnm.txt", "w" )

for i in range(int(input('How many to generate?: '))):
    line = str(random.randint(1, 500))
    randfile.write(line)
    print(line)

randfile.close()
