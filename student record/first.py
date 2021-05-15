from tkinter import *
import csv

sb1=Tk()
sb1.title("Create New Record")
sb1.geometry("500x250")


r = IntVar()
n = StringVar()
m = DoubleVar()

def fb1():
    fstu = open("student.csv", "a+",newline="")
    global id
    id=0
    fm = ['ID:', 'Name:', 'Roll:', 'Marks:', 'Percent:', 'Remark:']
    cw = csv.DictWriter(fstu, fieldnames=fm)
    cw.writeheader()
    def next():
        stu=[]
        global id
        id+=1
        p=(m.get()/900)*100
        if p<32.0:
            rem="Fail"
        elif p>=32.0:
            rem="Pass"
        s1={"ID:":id,"Name:":n.get(),"Roll:":r.get(),"Marks:":m.get(),"Percent:":p,"Remark:":rem}
        stu.append(s1)
        print(stu)
        cw.writerows(stu)

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)

    c1=Label(text="Roll Number:")
    c1.place(x=10,y=20)
    e1=Entry(textvariable=r)
    e1.place(x=100, y=20)

    c2 = Label(text="Name:")
    c2.place(x=45, y=50)
    e2 = Entry(textvariable=n)
    e2.place(x=100, y=50)

    c3 = Label(text="Marks:")
    c3.place(x=45, y=80)
    e3 = Entry(textvariable=m)
    e3.place(x=100, y=80)

    b1=Button(text="Next", command=next)
    b1.place(x=150, y=120)

    def create():
        fstu.close()

    b2 = Button(text="Creat Record", command=create)
    b2.place(x=300, y=120)

fb1()

sb1.mainloop()



