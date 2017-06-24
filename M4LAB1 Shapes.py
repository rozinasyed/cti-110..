


#Shapes  
#CTI 110 M4LAB1: Shapes
#6/23/17
#Syed

import turtle


win = turtle.Screen()
 
win.bgcolor("green")
t = turtle.Turtle()

t.pensize(1)        
t.pencolor("red")

t.shape("turtle")
t.speed(2)


for i in range(3):

    
     t.forward(100)
     t.left(120)


for i in range(3):
     for i in (1,2):
      t.forward(100)
      t.left(90)





for i in range(3):

    
     t.forward(100)
     t.left(120)


for i in range(2):
    
      t.forward(100)
      t.left(90)


win.mainloop()
