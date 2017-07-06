# Feet to Inches  
# 6/26/17
# CTI-110 M5T2_FeetToInches 
# Syed


def feetToInches( userFeet ) :

    inches = (userFeet / 1 ) * 12
    return inches
def main ():
    userFeet = float(input("please enter the number of feet: "  ) )
    print ()
    inches = feetToInches ( userFeet )
    print ( userFeet, "feet converted to inches is " , format( inches, " .2f" ), "inches")
    
main()
