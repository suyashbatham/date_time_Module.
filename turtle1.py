import turtle
amul = turtle.Turtle()  # Turtle-class   # turtle-module name
amul.shape("turtle")  #where shape() is classic
amul.color()
amul.color("red")
amul.color("red","green") #line color-red  # turtle color-green


# # for changing the background picture (   picture must be in gif mode)
#bgcolor() - for changing the background color
#bgpic() - for changing the background picture
#title() - for changing the title
amul = turtle.Turtle()
wn = turtle.Screen()
wn.bgpic("pythom1.gif")  # picture name
wn.title("Suyash")
wn.bgcolor("yellow")


#turtle movement (backword and forward)
t = turtle.Turtle()  # create a turtle object
t.setheading(90) # for cursor towards  north (change the turtle  direction)
t.setheading(180) # for cursor towards  west
t.setheading(270) # for  cursor towards south
t.setheading(360) # for cursor towards east
t.forward(100) #t.fd(100) both are same(we can use negative direction also)
t.backword(100) #t.bk(100)
t.left(45) #t.lt(100)
t.right(45) #t.rt(45) where 45 is the angle

t = turtle.Turtle()
t.speed(1)  # speed of the turtle
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.forward(200)
    t.left(90)
t.endfill()

t.hideturtle() # hide the turtle


