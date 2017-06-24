# Age Classifier  
# 6/16/17
# CTI-110 M3HW1 - Age Classifier
# Syed


userAge = int( input("please enter your age:" ) )

if userAge <=1:
    print("You are an infant")
elif userAge < 13:
     print( "You are a child")
elif userAge < 20:
    print( "You are a teenager")
elif userAge >= 20:
    print( "you are an adult" )
