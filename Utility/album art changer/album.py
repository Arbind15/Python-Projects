import tkinter
from tkinter import filedialog
import os
import base64
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import Picture
from mutagen.mp3 import MP3
from mutagen.id3 import ID3,APIC
fdir = filedialog.askdirectory(title="Select folder")
imgfl=filedialog.askopenfilename(title="select album art",filetypes=[("Album Art", ".jpg .png")])
with open(imgfl, "rb") as h:
    imgdata = h.read()
i=0
for file in os.listdir(fdir):
    if file.endswith('.mp3'):
        fl=str(fdir + "/" + file)
        # print(fl)
        i=i+1
        try:
            audio = ID3(fl)
            audio.add(APIC(type=3,desc=u'Album Art',data=imgdata))
            # print(fl)
            # print(audio.getall("APIC:"))
            print(i," ",file," -Done")
            # audio.delall("data") play with this if program not work for all item, this is forcing to do so
            audio.save()
        except:
            print(i," ",file," -something went wrong")
            # if this error occur the remove all the properties by selecting all file and left click goto advance and click blue text at bottom
            #check all properties and remove then agin run