from tkinter import *
cal=Tk()
cal.geometry("166x225")
cal.title("Calculator")

a=0
b=0
i=0
eq=""
sum=0
min=0
mul=1
div=1
mod=1

def fbc():
    global a
    a=0
    global b
    b=0
    global i
    i=0
    global sum
    sum=0
    global min
    min=0
    global mul
    mul=1
    global div
    div=1
    global mod
    mod=1
    global eq
    eq=""

    def cl():
        l = Label(text="                                                                          ")
        l.place(x=0, y=65)
        l1 = Label(text="                                                                           ")
        l1.place(x=0, y=40)
    cl()


def cl():
    l=Label(text="                                                                                 ")
    l.place(x=0,y=65)

def fb1():
    global a
    a=(a*10)+1
    l = Label(text=a)
    l.place(x=10, y=65)

def fb2():
    global a
    a=(a*10)+2
    l = Label(text=a)
    l.place(x=10, y=65)

def fb3():
    global a
    a=(a*10)+3
    l = Label(text=a)
    l.place(x=10, y=65)

def fb4():
    global a
    a=(a*10)+4
    l = Label(text=a)
    l.place(x=10, y=65)

def fb5():
    global a
    a=(a*10)+5
    l = Label(text=a)
    l.place(x=10, y=65)

def fb6():
    global a
    a=(a*10)+6
    l = Label(text=a)
    l.place(x=10, y=65)

def fb7():
    global a
    a=(a*10)+7
    l = Label(text=a)
    l.place(x=10, y=65)

def fb8():
    global a
    a=(a*10)+8
    l = Label(text=a)
    l.place(x=10, y=65)

def fb9():
    global a
    a=(a*10)+9
    l = Label(text=a)
    l.place(x=10, y=65)

def fb0():
    global a
    a=(a*10)+0
    l = Label(text=a)
    l.place(x=10, y=65)

def fbp():
    global a
    global sum
    global eq
    eq="p"
    sum=sum+a
    a=0
    pl = Label(text=sum)
    pl.place(x=10, y=40)
    cl()

def fbm():
    global a
    global min
    global i
    global eq
    eq="m"
    if(i==0):
        min=a
    elif(i>0):
        min=min-a
    pl = Label(text=min)
    pl.place(x=10, y=40)
    a=0
    i=i+1
    cl()

def fbmm():
    global a
    global mul
    global eq
    eq="mm"
    mul=mul*a
    pl = Label(text=mul)
    pl.place(x=10, y=40)
    a=0
    cl()

def fbd():
    global a
    global i
    global div
    global eq
    eq="d"
    if(i==0):
        b=1
        div=a
    elif(i>0):
        b=a
    div=div/b
    a=0
    pl = Label(text=div)
    pl.place(x=10, y=40)
    i=i+1
    cl()

def fbmo():
    global a
    global i
    global mod
    global eq
    eq="mo"
    if(i==0):
        mod=a
        pl = Label(text=mod)
        pl.place(x=10, y=40)
    elif(i>0):
        b=a
        mod=mod%b
        pl = Label(text=mod)
        pl.place(x=10, y=40)
    a=0
    i=i+1
    cl()

def fbdo():
    global a
    a=float(a+.0)
    l = Label(text=a)
    l.place(x=10, y=65)


def fbeq():
    global eq
    if(eq=="p"):
        fbp()
    elif(eq=="m"):
        fbm()
    elif(eq=="mm"):
        fbmm()
    elif(eq=="d"):
        fbd()
    elif(eq=="mo"):
        fbmo()

b1=Button(text="1",command=fb1)
b1.place(x=10,y=100)

b2=Button(text="2",command=fb2)
b2.place(x=40,y=100)

b3=Button(text="3",command=fb3)
b3.place(x=70,y=100)

b4=Button(text="4",command=fb4)
b4.place(x=10,y=130)

b5=Button(text="5",command=fb5)
b5.place(x=40,y=130)

b6=Button(text="6",command=fb6)
b6.place(x=70,y=130)

b7=Button(text="7",command=fb7)
b7.place(x=10,y=160)

b8=Button(text="8",command=fb8)
b8.place(x=40,y=160)

b9=Button(text="9",command=fb9)
b9.place(x=70,y=160)

pb=Button(text="+",width=2,command=fbp)
pb.place(x=100,y=100)

pm=Button(text="-", width=2,command=fbm)
pm.place(x=100,y=130)

pmm=Button(text="X", width=2,command=fbmm)
pmm.place(x=100,y=160)

pc=Button(text="C",width=2,command=fbc)
pc.place(x=130,y=100)

pmo=Button(text="%", width=2,command=fbmo)
pmo.place(x=130,y=130)

pb=Button(text="/", width=2,command=fbd)
pb.place(x=130,y=160)

pe=Button(text="=",width=10,command=fbeq)
pe.place(x=73,y=190)

pdo=Button(text=".",width=2,command=fbdo)
pdo.place(x=10,y=190)

p0=Button(text="0",width=2,command=fb0)
p0.place(x=40,y=190)




cal.mainloop()