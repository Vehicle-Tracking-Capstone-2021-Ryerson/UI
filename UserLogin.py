import tkinter as tk
from tkinter import *
#from mainpage import *

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
label1 = tk.Label(frame, text = "                                ")
label2 = tk.Label(frame, text = "                                ")
lbl = tk.Label(frame, text = "Please Enter you User PIN")
label1.pack()
label1.pack()
lbl.pack()
label2.pack()

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    if(inp == "password"):
        lbl2.config(text = "Provided Input: Success")
        #mainpage()
    else:
        lbl2.config(text = "User PIN not valid. Please enter a valid PIN")

# TextBox Creation
inputtxt = tk.Text(frame, height = 1, width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame, text = "Enter", command = printInput)
printButton.pack()

lbl2 = tk.Label(frame, text = "")
lbl2.pack()
# Label Creation
frame.mainloop()