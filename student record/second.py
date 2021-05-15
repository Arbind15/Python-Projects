from tkinter import *
import csv

sb2 = Tk()
sb2.title("View Record")
sb2.geometry("690x800")
def fb2():
    l1=Label(text="ID:\t\tName:\t\t\t\tRoll No:\t\tMarks:\t\tPercentage(%):\t\tRemark:")
    l1.place(relx=0.01,rely=0.05)

    lb1 = Listbox(sb2,width=117,height=50)

    with open("student.csv", "r",newline="") as fstu:
        cw=csv.DictReader(fstu)
        for i in cw:
            stud=str(i["ID:"])+str("\t\t     ")+str(i["Name:"])+str("\t\t\t\t      ")+str(i["Roll:"])+str("\t\t      ")+str(i["Marks:"])+str("\t\t      ")+str(i["Percent:"])+str("\t\t      ")+str(i["Remark:"])
            print(stud)
            lb1.insert(END, stud)

    lb1.place(relx=0, rely=0.08)

fb2()

sb2.mainloop()
