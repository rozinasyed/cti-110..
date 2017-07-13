

# Random Number File Writer
# 7/12/17
# CTI-110 M6HW1 - Random Number File Writer
# Syed
#





import random

random_numbers = open('numbers.txt', 'w')

def main():

    writeFunction(getRandom())

def getRandom():
    qty_numbers = int(input('How many random numbers should be writer to the file? '))

    nums = []
    for count in range (qty_numbers):
        nums.append(random.randint(1,500))
    return nums

def writeFunction(a_list):
    random_nums = '\n'.join([str(x) for x in a_list])
    random_numbers.write(random_nums)
    random_numbers.close()
    print('Your list of random numbers have been writer to the file named')
    print('numbers.txt')

main()
