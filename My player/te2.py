from tkinter import *
from tkinter import ttk, filedialog, messagebox,Tk,Frame,Menu
import pygame
import time
import p5 as p
import audio2numpy,sys
import os
from mutagen.mp3 import MP3,MutagenError
from mutagen.id3 import ID3
import threading, _thread
import base64,visual,random,test,subprocess
from PIL import Image,ImageTk


player = Tk()
player.title("My Player")
player.geometry("600x500")
player.resizable(FALSE, FALSE)
player.iconbitmap("E:\Projects\Python\Pure Python Projects\My player\icc.ico")
ttk.Separator(player, orient=HORIZONTAL)

pygame.init()  ##Initilizing pygame
pygame.mixer.init()

global flag2, flag3, n, listdir,flag7,flag8,flag9,shuff_staus,appnd,fdir
appnd=False
shuff_staus=False
listdir = []
flag3 = ""
flag7=""
flag8=""
flag9=""
flag2 = ""
label = Label(player)
scrl = Scrollbar(player, orient=VERTICAL)
list = Listbox(width=89, height=15, highlightcolor="#e6f6f7", selectmode=SINGLE, yscrollcommand=scrl.set)
lab1 = Label(player)
lab2 = Label(player)
lab3 = Label(player)
lab4 = Label(player)
lab5 = Label(player)
lab6 = Label(player)
lock=threading.Lock()

def shuffle():
    global shuff_staus

    shuff_staus=True

def pnx():
    global shuff_staus,appnd
    appnd=True
    shuff_staus=False
    list.activate(list.index(ACTIVE))

def filloc():
    global listdir
    sel=os.path.dirname(listdir[0])
    ind=0
    temsal=""
    for sal in sel:
        if sal=="/":
            temsal=temsal+str("\\")
            ind=+1
        else:
            temsal=temsal+str(sal)
            ind=+1
    subprocess.Popen(f'explorer {temsal}')

class Example(Frame):

    def __init__(self,element):
        super().__init__()

        self.initUI(element)


    def initUI(self,element):

        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label="Play", command=fply)
        self.menu.add_command(label="Play next", command=pnx)
        self.menu.add_command(label="Open file location", command=filloc)

        element.bind("<Button-3>", self.showMenu)
        self.pack()


    def showMenu(self, e):

        self.menu.post(e.x_root, e.y_root)


def fopnfo():
    global fdir
    global flag, listdir,shuff_staus,fdir
    shuff_staus=False
    listdir = []
    flag = "folder"
    fdir = filedialog.askdirectory(title="Select folder")
    i=0
    list.delete(0, END)
    for file in os.listdir(fdir):
        if file.endswith('.mp3'):
            list.insert(END, file)
            listdir.append(fdir + "/" + file)

####################Spectrum__Stuff##################################
height = 250
width = 506
ofset = 0.0
final = 0
dur = 0.02
x = 5
y = 300
z = 0
fp=''
def setup():
    global height, width
    p.size(width, height)  # size must be the first statement
    # stroke(25) # Set line drawing color to white


# The statements in draw() are executed until the
# program is stopped. Each statement is executed in
# sequence and after the last line is read, the first
# line is executed again.
def draw():
    global ofset, x, y, z,fp,fl
    if(flag7=="fsek"):
        ofset = sek
    if (flag2 == "pus"):
        pass
    if(flag8=="nxt" or flag9=="pev"):
        ofset=sek
        fp=fl

    else:
        signal, sampling_rate = audio2numpy.audio_from_file(fp, offset=ofset, duration=dur, dtype='int')
        p.background(250)
        signal = abs(signal)
        # signal = signal[..., 1]
        ofset = ofset + dur
        # print(np.size(signal[:250]))
        for i in signal:
            p.line((x, height - 5), (x, -(200 * i[1] + 50) + height - 5))
            x +=1.5
            p.line((x, height - 5), (x, -(200 * i[0]+100) + height - 5))
            x+=1.5
            p.line((x, height - 5), (x, -(200*i[1]+50)+height - 5))
            x +=1.5
            if (ofset >= final):
                pass
        time.sleep(dur)
        x = 5



def start(fpp='',offset=0.0,stop=False):
    global fp, ofset, dur,length,final,sek
    final=length
    ofset=sek
    fp=fpp
    # print(sek)
    # fp = "test.mp3"  # change to the correct path to your file accordingly
    # The statement in setup() function
    # ececute once when the program begins
    if __name__ == '__main__':
        p.run()

def sound_spectrum():
    global fl
    # print(fl)
    th=threading.Thread(target=start,args=(fl,0.0,False))
    th.daemon=True
    th.start()

##########################################End_of_Spectrum##############################

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
    currentlabel['text'] = "00:00"
    totallabel['text'] = "00:00"
    label["text"]=""
    lab1["text"]=""
    lab2["text"] = ""
    lab3["text"] = ""
    lab4["text"] = ""
    lab5["text"] = ""
    lab6["text"] = ""

def fply(*args):
    global fl,th1
    global flag,ofset,fp
    global flag2, flag3, curindx, inc, flag4,shuff_staus
    global length
    flag4 = "ply"
    ofset=0.0

    try:
        if flag == "folder":
            if flag2 == "pus":
                pygame.mixer.music.unpause()
                flag2 = ""
            else:
                inc = 0
                if shuff_staus==True:
                    try:
                        print(len(listdir))
                        sel=random.randint(0,len(listdir)-1)
                        print(sel)
                        list.activate(sel)
                    except:
                        print("exc")
                        fstp()

                fl = fdir + "/" + list.get(ACTIVE)
                audio = MP3(fl)
                length = audio.info.length
                flag3 = ""
                # try:
                #     if th1.is_alive():
                #         print("alive")
                #         th1.stop()
                #     else:
                #         print("dead")
                # except:
                #     pass

                th1 = threading.Thread(target=fpbar)  ##performing multiple task with while loop
                th1.daemon=True
                th1.start()

                curindx = list.index(ACTIVE)
                # fn = fdir + "/" + list.get(n + 1)
                pygame.mixer.music.load(fl)
                # pygame.mixer.music.queue(fn)
                try:
                    itm=[fl]
                    visual.recent(itm)
                except:
                    pass
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
            th1.demon=True
            th1.start()
            pygame.mixer.music.load(fl)
            try:
                itm = [fl]
                visual.recent(itm)
            except:
                pass
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
            c = Canvas(width=100, height=110)
            i = Image.open("art.jpg")
            i.thumbnail((90, 110))
            i.save("n.png")
            m = Image.open("n.png")
            k = ImageTk.PhotoImage(m)
            player.k=k
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
        except KeyError:
            c = Canvas(width=100, height=110)
            i = Image.open("ply.jpg")
            i.thumbnail((90, 110))
            i.save("n.png")
            m = Image.open("n.png")
            k = ImageTk.PhotoImage(m)
            player.k=k
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
        label["text"] = "Now playing: "
        text=str(list.get(ACTIVE))
        visual.scroll_text(player,text,0.165,0.88)
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

    fp=fl


def fpus():
    global flag2
    flag2 = "pus"
    pygame.mixer.music.pause()


def fvol(val):
    vol = int(val) / 100
    pygame.mixer.music.set_volume(vol)  ##takes value from 0 to 1


def fnxt():
    global curindx,listdir,flag8,sek,shuff_staus,appnd
    flag8="nxt"
    sek=0
    pbar.set(0)
    if appnd==True:
        fply()
        appnd=False
        return
    if (len(listdir)-1) ==curindx:
        if shuff_staus==True:
            return
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
    global curindx,flag9,sek
    flag9="pev"
    sek=0
    list.activate(curindx - 1)
    fply()

def fseek(event):
    global length,ts,sek,flag7
    flag7="fsek"
    sek=(length/535)*event.x
    if sek<0:
        sek=0
    elif sek>(length):
        sek=(length)
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(sek)




def fext():
    player.destroy()
    exit()

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
            pd=img.data
            with open("art.jpg", "wb") as art:
                art.write(pd)
            c = Canvas(width=100, height=110)
            i = Image.open("art.jpg")
            i.thumbnail((90, 110))
            i.save("n.png")
            m = Image.open(r"n.png")
            k = ImageTk.PhotoImage(m)
            player.k=k
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)
        except KeyError:
            c = Canvas(width=100, height=110)
            i = Image.open("ply.jpg")
            i.thumbnail((90, 110))
            i.save("n.png")
            m = Image.open(r"n.png")
            k = ImageTk.PhotoImage(m)
            player.k=k
            c.create_image(52, 57, image=k, anchor="center")
            c.place(relx=0.77, rely=0.567)

        # pygame.mixer.music.set_pos(pos)
        lab1.place(relx=0.05, rely=0.56)
        lab2.place(relx=0.05, rely=0.6)
        lab3.place(relx=0.05, rely=0.64)
        lab4.place(relx=0.05, rely=0.68)
        lab5.place(relx=0.05, rely=0.72)
        lab6.place(relx=0.75, rely=0.58)


def fpbar():
    global length
    global flag2, flag3, flag4,ts,flag7,sek,flag9,flag8
    # calculating total duration
    min, sec = divmod(round(length), 60)
    timeformat = "{:02d}:{:02d}".format(min, sec)
    totallabel["text"] = timeformat
    t = 0
    sek=0
    while t <= (length + 1):  ##pygame.mixer.music.get_busy() returns false when music is stopped

        if flag2 == "pus":
            continue

        elif flag3 == "stp":
            break

        else:

            div = 500 / round(length)
            #p = pygame.mixer.music.get_pos()##it just give how long time have been played not progressbar
            a = div * sek  ##setting cursor position in progress bar
            pbar.set(a)
            ##Calulating current duration
            min, sec = divmod(round(sek), 60)
            timeformat = "{:02d}:{:02d}".format(min, sec)
            currentlabel["text"] = timeformat
            with lock:
                time.sleep(1)
                t += 1
                sek+=1
        if flag8=="nxt" or flag9=="pev":
            flag8=""
            flag9=""
            t=0
            sek=0
            fpbar()
            break

        if pygame.mixer.music.get_busy() == FALSE:
            try:
                fnxt()
                break
            except IndexError:
                break

def rec():
    print("ki")

    print("ki")

pbar = ttk.Scale(player, length=535, from_=0, to=500)
pbar.bind("<Button-1>",fseek)
list.bind('<<ListboxSelect>>', finfo)
list.bind('<Double-1>', fply)
Example(list)
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

lis=Menu(submenu,tearoff=0)

def plyrec(itm):
    global fl
    global flag, listdir
    itm=itm[:-1]
    print(itm)
    listdir = []
    flag = "file"
    list.delete(0, END)
    fl=itm
    listdir.append(fl)
    list.insert(END, fl)


def clr():
    os.remove("temp.txt")

try:
    with open("temp.txt", 'r') as t:
        t2 = t.readlines()
        i=1
        t1=[]
        for itm in t2:
            t1.append(t2[len(t2)-i])
            i+=1
        # for itm in t1:
        #     lis.add_command(label=itm,command=lambda :plyrec(itm))
    lis.add_command(label=t1[0],command=lambda :plyrec(t1[0]))
    lis.add_command(label=t1[1], command=lambda :plyrec(t1[1]))
    lis.add_command(label=t1[2], command=lambda :plyrec(t1[2]))
    lis.add_command(label=t1[3], command=lambda :plyrec(t1[3]))
    lis.add_command(label=t1[4], command=lambda :plyrec(t1[4]))
    lis.add_command(label=t1[5], command=lambda :plyrec(t1[5]))
    lis.add_command(label=t1[6], command=lambda :plyrec(t1[6]))
    lis.add_command(label=t1[7], command=lambda :plyrec(t1[7]))
    lis.add_command(label=t1[8], command=lambda :plyrec(t1[8]))
    lis.add_command(label=t1[9], command=lambda :plyrec(t1[9]))

    lis.add_command(label="Clear all", command=clr)
except:
    lis.add_command(label="No recent media")



submenu.add_cascade(label="Recents",menu=lis,underline=0)


submenu.add_separator()
submenu.add_command(label="Exit",command=fext)

list.bind("Double Click", fply)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=submenu)
submenu.add_command(label="Shuffle all",command=shuffle)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=submenu)
submenu.add_command(label="Visualizer",command=sound_spectrum)
submenu.add_command(label="About us")

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



