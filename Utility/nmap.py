def nepal_map():
    import turtle
    t=turtle.Turtle()
    turtle.title("Jai Nepal")
    turtle.bgcolor("gray")
    t.hideturtle()
    t.speed(0)
    t.pensize(5)
    t.pencolor("dark blue")
    t.begin_fill()
    t.fillcolor("red")
    t.forward(100)
    t.left(135)
    t.forward(100)
    t.right(135)
    t.forward(50)
    t.left(135)
    t.forward(115)
    t.right(225)
    t.forward(250)
    t.end_fill()
    t.pensize(0)
    t.pencolor("black")
    t.up()
    t.home()


    t.goto(40,90)
    t.begin_fill()
    t.fillcolor("white")
    for i in range(0,12):
        t.left(30)
        t.forward(4)
        t.left(120)
        t.forward(4)
        t.right(120)
    t.end_fill()
    t.up()
    t.home()
    t.goto(42,29)
    t.up()
    t.begin_fill()
    t.fillcolor("white")
    for i in range(0,7):
        t.left(30)
        t.forward(3)
        t.left(120)
        t.forward(3)
        t.right(120)
    for i in range(0,3):
        t.forward(6)
        t.right(45)
    t.right(180)
    for i in range(0,2):
        t.forward(5)
        t.left(30)
    for i in range(0,3):
        t.forward(10)
        t.left(30)

    for i in range(0,5):
        t.forward(3)
        t.left(5)
    for i in range(0,3):
        t.forward(2)
        t.left(30)
    t.left(90)
    for i in range(0,2):
        t.forward(5)
        t.right(30)
    # t.forward(2)
    t.end_fill()





    turtle.done()
nepal_map()
# from tkinter import *
# sc=Tk()
# l=Label(text="ABC")
# l.pack()
# x=Entry()
# x.place(x=200,y=300)


