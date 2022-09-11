"""
    Napisz program, który wczytuje plik tekstowy, a następnie wypisuje go z ponumerowanymi liniami.
    Write the program, which read text file and also write lines with the number

"""
from pip._vendor.distlib.compat import raw_input

import tkinter.filedialog
import os

file=open(tkinter.filedialog.askopenfilename(),"r")
file_name=str(file)
print("Get the name of file:",file_name)
n= 0
if file.readable():
    tekst = file.readlines()
    for line in tekst:
        n+=1
        print(str(n) +":" + line + "\n")

file.close()
