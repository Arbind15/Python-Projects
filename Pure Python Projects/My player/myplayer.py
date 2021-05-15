from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pygame
import time
import os
from mutagen.mp3 import MP3,MutagenError
from mutagen.id3 import ID3
import threading
import base64
from PIL import ImageTk,Image


player = Tk()
player.title("My Player")
player.geometry("600x500")
player.resizable(FALSE, FALSE)
player.iconbitmap("D:\Documents\Python\My player\img\icc.ico")
ttk.Separator(player, orient=HORIZONTAL)

pygame.init()  ##Initilizing pygame
pygame.mixer.init()

global flag2, flag3, n, listdir
listdir = []
flag3 = ""
flag2 = ""
label = Label(player)
scrl = Scrollbar(player, orient=VERTICAL)
list = Listbox(width=89, height=15, highlightcolor="#e6f6f7", selectmode=SINGLE, yscrollcommand=scrl.set)
c = Canvas(width=100, height=110, bg="#faf1d9")
lab1 = Label(player)
lab2 = Label(player)
lab3 = Label(player)
lab4 = Label(player)
lab5 = Label(player)
lab6 = Label(player)


def fopnfo():
    global fdir
    global flag, listdir
    listdir = []
    flag = "folder"
    fdir = filedialog.askdirectory(title="Select folder")
    i=0
    list.delete(0, END)
    for file in os.listdir(fdir):
        if file.endswith('.mp3'):
            list.insert(END, file)
            listdir.append(fdir + "/" + file)



def fopnf():
    global fl
    global flag, listdir
    listdir = []
    flag = "file"
    list.delete(0, END)
    fdir = filedialog.askopenfile(title="Select file", filetypes=(("Music files", "*.mp3"), ("all files", "*.*")))
    a1 = str(fdir).split("=")  ##This return list so a1 is list
    a2 = a1[1].split(".mp3")
    fl = a2[0][1:] + ".mp3"
    listdir.append(fl)
    list.insert(END, os.path.basename(fl))


def fpus():
    global flag2
    flag2 = "pus"
    pygame.mixer.music.pause()



def fply(*args):
    global fl
    global flag
    global flag2, flag3, curindx, inc, flag4
    global length
    flag4 = "ply"
    try:
        if flag == "folder":
            if flag2 == "pus":
                pygame.mixer.music.unpause()
                flag2 = ""
            else:
                inc = 0
                fl = fdir + "/" + list.get(ACTIVE)
                audio = MP3(fl)
                length = audio.info.length
                flag3 = ""
                th1 = threading.Thread(target=fpbar)  ##performing multiple task with while loop
                th1.start()
                curindx = list.index(ACTIVE)
                # fn = fdir + "/" + list.get(n + 1)
                pygame.mixer.music.load(fl)
                # pygame.mixer.music.queue(fn)
                pygame.mixer.music.play()

        elif flag2 == "pus":
            pygame.mixer.music.unpause()
            flag2 = ""
        else:
            inc = 0
            audio = MP3(fl)
            length = audio.info.length
            flag3 = ""
            th1 = threading.Thread(target=fpbar)  ##performing multiple task with while loop
            th1.start()
            pygame.mixer.music.load(fl)
            pygame.mixer.music.play()

        ############################
        lab1["text"] = "Details:"
        n = curindx
        aud = ID3(listdir[n])
        list.see(curindx)

        try:
            lab2["text"] = "Title: " + str(aud["TIT2"])
        except KeyError:
            lab2["text"] = "Title: -"
        try:
            lab3["text"] = "Singer: " + str(aud["TPE1"])
        except KeyError:
            lab3["text"] = "Singer: -"
        try:
            lab4["text"] = "Album: " + str(aud["TALB"])
        except KeyError:
            lab4["text"] = "Album: -"
        try:
            lab5["text"] = "Date: " + str(aud["TDRC"])
        except KeyError:
            lab5["text"] = "Date: -"
        try:
            img = (aud["APIC:"])
            pd = img.data
            with open("art.jpg", "wb") as art:
                art.write(pd)
            i = Image.open("art.jpg")
            i.thumbnail((90, 110))
            i.save("n.jpg")
            m = Image.open("n.jpg")
            k = ImageTk.PhotoImage(m)
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
            # os.remove("art.jpg")
            # os.remove("n.jpg")
        except KeyError:
            i = Image.open("ply.jpg")
            i.thumbnail((90, 110))
            i.save("n1.jpg")
            m = Image.open("n1.jpg")
            k = ImageTk.PhotoImage(m)
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
            #os.remove("n.jpg")

        label["text"] = "Now playing: " + list.get(ACTIVE)
    except FileNotFoundError:
        messagebox.showerror(message="Unsupported Format")
    except NameError:
        messagebox.showerror(message="Unsupported Format")
    except pygame.error:
        pygame.mixer.music.stop()
        messagebox.showerror(message="Unsupported Format")
    except MutagenError:
        pygame.mixer.music.stop()
        messagebox.showerror(message="Unsupported Format")
    except:
        pygame.mixer.music.stop()
        messagebox.showerror(message="Sorry, something went wrong.")





def fstp():
    global flag2
    global flag
    global flag3, fl
    pygame.mixer.music.stop()
    list.delete(0, END)
    flag2 = ""
    flag = ""
    flag3 = "stp"
    fl = ""
    pbar.set(0)
    c.destroy()
    currentlabel['text'] = "00:00"
    totallabel['text'] = "00:00"
    label["text"]=""
    lab1["text"]=""
    lab2["text"] = ""
    lab3["text"] = ""
    lab4["text"] = ""
    lab5["text"] = ""
    lab6["text"] = ""

def fpus():
    global flag2
    flag2 = "pus"
    pygame.mixer.music.pause()


def fvol(val):
    vol = int(val) / 100
    pygame.mixer.music.set_volume(vol)  ##takes value from 0 to 1


def fnxt():
    global curindx,listdir
    if (len(listdir)-1) ==curindx:
        list.activate(0)
        list.see(0)
        pygame.mixer.music.stop()
        pbar.set(0)
        currentlabel['text'] = "00:00"
        totallabel['text'] = "00:00"
        label["text"]=""
    else:
        list.activate(curindx + 1)  # making next selection
        fply()


def fpev():
    global curindx
    list.activate(curindx - 1)
    fply()

def fext():
    player.destroy()

def finfo(*args):
    global listfdir
    # b=pbar.get()
    # pos=b/60
    indx = list.curselection()

    if indx == ():
        lab1["text"] = "No file is added.Goto File to add file"
    else:
        lab1["text"] = "Details:"
        n = indx[0]
        aud = ID3(listdir[n])

        try:
            lab2["text"] = "Title: " + str(aud["TIT2"])
        except KeyError:
            lab2["text"] = "Title: -"
        try:
            lab3["text"] = "Singer: " + str(aud["TPE1"])
        except KeyError:
            lab3["text"] = "Singer: -"
        try:
            lab4["text"] = "Album: " + str(aud["TALB"])
        except KeyError:
            lab4["text"] = "Album: -"
        try:
            lab5["text"] = "Date: " + str(aud["TDRC"])
        except KeyError:
            lab5["text"] = "Date: -"
        try:
            img = (aud["APIC:"])
            pd = img.data
            with open("art.jpg", "wb") as art:
                art.write(pd)
            i = Image.open("art.jpg")
            i.thumbnail((90, 110))
            i.save("n.jpg")
            m = Image.open("n.jpg")
            k = ImageTk.PhotoImage(m)
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
            # os.remove("art.jpg")
            # os.remove("n.jpg")
        except KeyError:
            i = Image.open("ply.jpg")
            i.thumbnail((90, 110))
            i.save("n1.jpg")
            m = Image.open("n1.jpg")
            k = ImageTk.PhotoImage(m)
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
            #os.remove("n.jpg")

        lab1.place(relx=0.05, rely=0.56)
        lab2.place(relx=0.05, rely=0.6)
        lab3.place(relx=0.05, rely=0.64)
        lab4.place(relx=0.05, rely=0.68)
        lab5.place(relx=0.05, rely=0.72)
        lab6.place(relx=0.75, rely=0.58)


def fpbar():
    global length
    global flag2, flag3, flag4
    # calculating total duration
    min, sec = divmod(round(length), 60)
    timeformat = "{:02d}:{:02d}".format(min, sec)
    totallabel["text"] = timeformat
    t = 0
    while t <= (length + 1):  ##pygame.mixer.music.get_busy() returns false when music is stopped

        if flag2 == "pus":
            continue

        elif flag3 == "stp":
            break

        else:
            div = 500 / round(length)
            p = pygame.mixer.music.get_pos()
            ts = round(p / 1000)
            a = div * ts  ##setting cursor position in progress bar
            pbar.set(a)
            ##Calulating current duration
            min, sec = divmod(ts, 60)
            timeformat = "{:02d}:{:02d}".format(min, sec)
            currentlabel["text"] = timeformat
            time.sleep(1)
            t += 1

        if pygame.mixer.music.get_busy() == FALSE:
            try:
                fnxt()
                break
            except IndexError:
                break


pbar = ttk.Scale(player, length=535, from_=0, to=500)
list.bind('<<ListboxSelect>>', finfo)
list.bind('<Double-1>', fply)
currentlabel = Label(player, text="00:00")
currentlabel.place(relx=0.04, rely=0.85)
totallabel = Label(player, text="00:00")
totallabel.place(relx=0.9, rely=0.85)
pbar.place(relx=0.05, rely=0.8)
scale = Scale(player, from_=0, to=100, orient=HORIZONTAL, command=fvol)
scale.set(30)
scale.place(relx=0.8, rely=0.89)
menubar = Menu(player)
player.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open file", command=fopnf)
submenu.add_command(label="Open folder", command=fopnfo)
submenu.add_command(label="Exit",command=fext)

list.bind("Double Click", fply)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About us")
b1 = Button(player, text="play", command=fply)
b2 = Button(player, text="stop", command=fstp)
b5 = Button(player, text="Next", command=fnxt)
b7 = Button(player, text="Previous", command=fpev)
b3 = Button(player, text="Pause", command=fpus)

b1.place(relx=0.01, rely=0.92)
scrl.place(relx=0.94, rely=0.05, height=243)
scrl.config(command=list.yview)
list.place(relx=0.05, rely=0.05)
b2.place(relx=0.25, rely=0.92)
b5.place(relx=0.313, rely=0.92)
b7.place(relx=0.15, rely=0.92)
b3.place(relx=0.074, rely=0.92)
label.place(relx=0.04, rely=0.88)
player.mainloop()