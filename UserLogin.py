import tkinter as tk
from tkinter import *
import mainpage
import time
import helpers
import socket

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('500x250')

lbl = tk.Label(frame, text = "Please Enter you User-NAME and User-PIN")
lbl.pack(expand = True,pady =20)

def Close():
    frame.destroy()

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    time.sleep(1)
    inp2 = inputtxt2.get(1.0, "end-1c")
    #if((inp == "loveriel" and inp2 == "test") or (inp == "dan" and inp2 == "test") or (inp == "miguel" and inp2 == "test") or (inp == "david" and inp2 == "test") or (inp == "1" and inp2 == "1")):
    s = helpers.initConn(inp, inp2)
    lbl2.config(text = "Provided Input: Success")
    time.sleep(1)
    Close()
    mainpage.main(s)
    #else:
    	#lbl2.config(text = "User PIN or User NAME not valid. Please enter a valid PIN & NAME")

# TextBox Creation
lbl3 = tk.Label(frame, text = "Please Enter User-NAME", anchor = NW)
lbl3.pack(expand = True,pady =1)
inputtxt = tk.Text(frame, height = 1, width = 20)  
inputtxt.pack(expand = True)
lbl4 = tk.Label(frame, text = "Please Enter User-PIN", anchor = NW)
lbl4.pack(expand = True,pady =1)
inputtxt2 = tk.Text(frame, height = 1, width = 20)
inputtxt2.pack(expand = True)
  
# Button Creation
printButton = tk.Button(frame, text = "Enter", command = printInput)
printButton.pack(expand = True ,pady = 10)

lbl2 = tk.Label(frame, text = "")
lbl2.pack()
# Label Creation
frame.mainloop()
