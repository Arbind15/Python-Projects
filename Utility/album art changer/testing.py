import tkinter
from tkinter import filedialog
import os
import base64
from mutagen.oggvorbis import OggVorbis
from mutagen.flac import Picture
from mutagen.mp3 import MP3
from mutagen.id3 import ID3,APIC
fdir = filedialog.askopenfilename(title="Select file")
imgfl=filedialog.askopenfilename(title="select album art",filetypes=[("Album Art", ".jpg")])
with open(imgfl, "rb") as h:
    imgdata = h.read()
i=0

i=i+1

audio = ID3(fdir)
audio.add(APIC(type=3,desc=u'Album Art',data=imgdata))
# print(fl)
# print(audio.getall("APIC:"))
# print(i," ",fdir," -Done")
# audio.save()
audio.delall("data")
audio.save()
