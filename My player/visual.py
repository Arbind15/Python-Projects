from tkinter import *
import time,threading,pygame
global th1

class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

        # function using _stop function

    def stop(self):
        self._stop.set()

def scroll_text(win,text,x,y):
    l=Label(win)
    def th():
        lis=text[0:49]
        l['text'] = lis
        time.sleep(2)

        for i in range(len(text)):
            i+=49

            if len(text)>=50:
                try:
                    lis=lis+text[i]
                    l['text'] = lis
                    time.sleep(0.25)
                    lis=lis[1:]
                except:
                    pass

            if pygame.mixer.music.get_busy() == False:
                l.destroy()
                break

        # if th1.is_alive():
        #     for thrd in threading.enumerate():
        #         print(str(thrd))
        #
        i=0
        time.sleep(0.4)
        th()

    th1=MyThread(target=th)
    th1.daemon=True
    th1.start()
    l.place(relx=x,rely=y)

# text="Arbind Kumar Mehta Gautampur-2, Sunsari (NEPAL)"
# scroll_text(sc,text,0.1,0.1)

def recent(itm):
    flag=""
    try:
        with open("temp.txt", 'r') as f:
            te=f.readlines()
        with open("temp.txt", 'a') as file:
            for item in itm:
                for item2 in te:
                    item2=item2[:-1]
                    if str(item2)==str(item):
                        flag="match"
                if flag!="match":
                    file.write(item + "\n")
    except:
        with open("temp.txt", 'a') as file:
            for item in itm:
                file.write(item + "\n")


# itm=["Arbind","Mehta","Shiva"]
# recent(itm)