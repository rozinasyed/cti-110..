
# Areas of Rectangles
# 6/16/17
# CTI-110 M3T1 - Areas of Rectangles
# Syed

rectangle1Length = float (input( "please enter the length of rectangle 1: ") )

rectangle1Width = float (input( "please enter the Width of rectangle 1: ") )

rectangle2Length = float (input( "please enter the length of rectangle 2: ") )

rectangle2Width = float (input( "please enter the Width of rectangle 2: ") )


rectangle1Area = rectangle1Length * rectangle1Width

rectangle2Area = rectangle2Length * rectangle2Width

if rectangle1Area > rectangle2Area:
    print( "\nRectangle 1 is bigger than Rectangle 2" )

elif rectangle2Area > rectangle1Area:

    print( "\nRectangle 2 is bigger than Rectangle 1" )

else:
    print( "\nBoth rectangles are equal" )
    
