from tkinter import *
from Student import Student
from first import fb1
from second import fb2
from third import fb3
stu=Tk()
stu.title("Student")
stu.geometry("500x500")



l1=Label(text="Welcome to student record.", fg="dark green", bg="gray",font=[10])
l1.pack()
l2=Label(text="Please make choice:",font=[5])
l2.place(x=0,y=50)
b1=Button(text="New Record", command=fb1)
b1.place(x=0,y=90)
b2=Button(text="View Record", command=fb2)
b2.place(x=200,y=90)
b3=Button(text="Edit Record", command=fb3)
b3.place(x=400,y=90)

stu.mainloop()
