# Kilometer Converter  
# 6/26/17
# CTI-110 M5T1_KilometerConverter 
# Syed

def askUserForKilometers():
    
      userKilometers = float( input( "please enyer the distance" + \
                                     " in kilometers: ") )
      return userKilometers
    
def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    
    UserForKilometers = askUserForKilometers()
    
    convertedMiles = convertKilometersToMiles ( UserForKilometers )
    print ()
    print ( UserForKilometers, "kilometers converted to miles is ", \
            format (   convertedMiles , ".2f" ), "miles" )
main()
