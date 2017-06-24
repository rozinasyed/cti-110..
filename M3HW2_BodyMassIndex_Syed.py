# Body Mass Index
# 6/16/17
# CTI-110 M3HW2 - Body Mass Index
# Syed


userWeight = float(input( "please enter your weight: " ) )
userHeight = float(input( "please enter your height: " ) )
userBmi = ( userWeight * 703 ) / ( userHeight ** 2)
print ()

if userBmi < 18.0:
    print(" A person with a BMI of " + format( userBmi, ".1f") + " is underweight")

elif userBmi < 25.0:
    print( " A person with a BMI of " + format( userBmi, ".1f" ) + \
           " has an optimal weight")
else:
    print( " A person with a BMI of " + formay( userBmi, ".1f" ) + \
           " is overweight")
