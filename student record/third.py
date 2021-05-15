from tkinter import *
import csv
import funk
import os

def fb3():
    sb3 = Tk()
    sb3.title("Edit Record")
    sb3.geometry("500x500")

    l1=Label(text="Make choice:",font=[2])
    l1.place(relx=0.05,rely=0.10)

    def ffb1():
        global oldr
        oldr=IntVar()
        global newr
        newr=IntVar()
        l2=Label(text="Old Roll Number:")
        el2=Entry(textvariable=oldr)
        l3=Label(text="New Roll Number:")
        el3=Entry(textvariable=newr)
        l2.place(relx=0.05,rely=0.30)
        l3.place(relx=0.05, rely=0.40)
        el2.place(relx=0.3, rely=0.30)
        el3.place(relx=0.3, rely=0.40)

        def fbl1():
            global oldr
            global newr
            j="f"
            with open("student.csv","r+",newline="") as fstu:
                cr=csv.DictReader(fstu)
                fm = ['ID:', 'Name:', 'Roll:', 'Marks:', 'Percent:', 'Remark:']
                cw=csv.DictWriter(fstu,fieldnames=fm)
                for stu in cr:
                    if (int(stu['Roll:']) == oldr.get()):
                        print(stu['Roll:'])
                        (stu['Roll:'])=newr.get()
                        print(stu['Roll:'])
                        s1=[]
                        dic={'ID:':stu['ID:'],'Name:':stu['Name:'],'Roll:':stu['Roll:'],'Marks:':stu['Marks:'],'Percent:':stu['Percent:'],'Remark:':stu['Remark:']}
                        s1.append(dic)
                        funk.copydic("temp.csv",dic)
                        j="p"
                    elif (int(stu['Roll:']))!=oldr.get():
                        funk.copydic("temp.csv", stu)
                funk.copyfile("temp.csv","student.csv")
                os.remove("temp.csv")
                el3.delete(0,END)
                el2.delete(0,END)
            if(j=="p"):
                le = Label(text="Changed sucessfully!!!")
                le.place(relx=0.3, rely=0.7)
            else:
                le = Label(text="No Match Found!!!")
                le.place(relx=0.3, rely=0.7)




        bl1 = Button(text="Done", command=fbl1)
        bl1.place(relx=0.32,rely=0.50)

    def ffb2():
        global oldn
        oldn = StringVar()
        global newn
        newn = StringVar()
        l2 = Label(text="Old Name:")
        el2 = Entry(textvariable=oldn)
        l3 = Label(text="New Name:")
        el3 = Entry(textvariable=newn)
        l2.place(relx=0.06, rely=0.30)
        l3.place(relx=0.05, rely=0.40)
        el2.place(relx=0.18, rely=0.30)
        el3.place(relx=0.18, rely=0.40)

        def fbl2():
            global oldn
            global newn
            j = "f"
            with open("student.csv", "r+", newline="") as fstu:
                cr = csv.DictReader(fstu)
                fm = ['ID:', 'Name:', 'Roll:', 'Marks:', 'Percent:', 'Remark:']
                cw = csv.DictWriter(fstu, fieldnames=fm)
                for stu in cr:
                    if (str(stu['Name:']) == oldn.get()):
                        print(stu['Name:'])
                        (stu['Name:']) = newn.get()
                        print(stu['Name:'])
                        s1 = []
                        dic = {'ID:': stu['ID:'], 'Name:': stu['Name:'], 'Roll:': stu['Roll:'], 'Marks:': stu['Marks:'],
                               'Percent:': stu['Percent:'], 'Remark:': stu['Remark:']}
                        s1.append(dic)
                        funk.copydic("temp.csv", dic)
                        j = "p"
                    elif (str(stu['Name:'])) != oldn.get():
                        funk.copydic("temp.csv", stu)
                funk.copyfile("temp.csv", "student.csv")
                os.remove("temp.csv")
                el3.delete(0, END)
                el2.delete(0, END)
            if (j == "p"):
                le = Label(text="Changed sucessfully!!!")
                le.place(relx=0.3, rely=0.7)
            else:
                le = Label(text="No Match Found!!!")
                le.place(relx=0.3, rely=0.7)

        bl1 = Button(text="Done", command=fbl2)
        bl1.place(relx=0.32, rely=0.50)


    def ffb3():
        global newm
        newm = DoubleVar()
        global rem
        rem = IntVar()
        global flag
        flag="False"

        r = Label(text="Enter Roll No:")
        re = Entry(textvariable=rem)
        r.place(relx=0.05, rely=0.30)
        re.place(relx=0.2, rely=0.30)
        def fre():
            global rem
            global flag
            with open("student.csv","r",newline="") as fst:
                cr=csv.DictReader(fst)
                for stu in cr:
                    if int(stu['Roll:'])==rem.get():
                        omar=stu['Marks:']
                        st="Old Marks is:   "+str(omar)
                        el2 = Label(text=st)
                        el2.place(relx=0.05, rely=0.35)
                        l3 = Label(text="Enter new Marks:")
                        el3 = Entry(textvariable=newm)
                        l3.place(relx=0.01, rely=0.40)
                        el3.place(relx=0.2, rely=0.40)
                        bl1.destroy()
                        flag="True"

                        def fbl4():
                            with open("student.csv", "r", newline="") as fst:
                                cr = csv.DictReader(fst)
                                for stu in cr:
                                    if int(stu['Roll:']) == rem.get():
                                        (stu['Marks:']) = newm.get()
                                        print(stu['Marks:'])
                                        s1 = []
                                        p = (newm.get() / 900) * 100

                                        if p < 32.0:
                                            rema = "Fail"
                                        elif p >= 32.0:
                                            rema = "Pass"

                                        dic = {'ID:': stu['ID:'], 'Name:': stu['Name:'], 'Roll:': stu['Roll:'],
                                               'Marks:': stu['Marks:'],
                                               'Percent:': p, 'Remark:': rema}
                                        s1.append(dic)
                                        funk.copydic("temp.csv", dic)
                                        el3.delete(0, END)
                                    elif int(stu['Roll:']) != rem.get():
                                        funk.copydic("temp.csv", stu)
                                        l4 = Label(text="Changed Sucessfully!!!")
                                        l4.place(relx=0.25, rely=0.60)
                                funk.copyfile("temp.csv","student.csv")
                                os.remove("temp.csv")



                        bl2 = Button(text="Done", command=fbl4)
                        bl2.place(relx=0.32, rely=0.50)






            if flag == "False":
                l = Label(text="No Match Found!!!")
                l.place(relx=0.25, rely=0.60)

        bl1 = Button(text="Search", command=fre)
        bl1.place(relx=0.32, rely=0.50)



    def ffb4():
        global teb3
        teb3=IntVar()
        # sc=Tk()
        # sc.mainloop()
        b1.destroy()
        b3.destroy()
        b2.destroy()
        b4.destroy()
        l1.destroy()
        l2=Label(text="Delete Record:",font=[1])
        l2.place(relx=0.05,rely=0.15)
        l3 = Label(text="Enter Roll Number:")
        l3.place(relx=0.05, rely=0.25)
        e3 = Entry(textvariable=teb3)
        e3.place(relx=0.27, rely=0.25)

        def fb5():

            global teb3
            j = "f"
            with open("student.csv", "r+", newline="") as fstu:
                cr = csv.DictReader(fstu)
                fm = ['ID:', 'Name:', 'Roll:', 'Marks:', 'Percent:', 'Remark:']
                cw = csv.DictWriter(fstu, fieldnames=fm)
                for stu in cr:
                    if (int(stu['Roll:']) )==teb3.get():
                        print(stu['Roll:'])
                        j = "p"
                    elif (int(stu['Roll:'])) != teb3.get():
                        funk.copydic("temp.csv", stu)
                funk.copyfile("temp.csv", "student.csv")
                os.remove("temp.csv")
            if (j == "p"):
                le = Label(text="Deleted sucessfully!!!")
                le.place(relx=0.3, rely=0.7)
            else:
                le = Label(text="No Match Found!!!")
                le.place(relx=0.3, rely=0.7)

        b5=Button(text="Delete",command=fb5)
        b5.place(relx=0.35,rely=0.4)



    b1=Button(text="Edit Roll Number",command=ffb1)
    b2 = Button(text="Edit Name",command=ffb2)
    b3 = Button(text="Edit Mark",command=ffb3)
    b4 = Button(text="Delete Record", command=ffb4)
    b1.place(relx=0.05,rely=0.20)
    b2.place(relx=0.3, rely=0.20)
    b3.place(relx=0.5, rely=0.20)
    b4.place(relx=0.7, rely=0.20)
    sb3.mainloop()



fb3()
