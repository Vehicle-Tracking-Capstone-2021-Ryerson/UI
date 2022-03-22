#Import the required libraries
from multiprocessing.connection import wait
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time

def accident():
    #Create an instance of tkinter frame
    root= tk.Tk()
    root.title("Accident Detection")
    root.geometry("400x200")
    
    s = Style()
    s.configure('My.TFrame', background='red')
    mail1 = Frame(root, style='My.TFrame')
    mail1.place(height=500, width=500, x=0, y=0)
    
    def printinput():
        lbl2.config(text = "BUTTON WORK FOR TESTING - Clicking button will close window")
        root.destroy()
    
    a = Label(root, text = "Warning Accident Dectected", anchor = CENTER)
    a2 = Label (root, text = "If This is a flase alarm please click ignore", anchor = CENTER)
    printButton = tk.Button(root, text = "Ignore Alarm", command = printinput)
    
    
    mail1.config()
    a.grid(row=0, column=0, padx=95, pady=20)
    a2.grid(row=1, column=0, padx=95, pady=10)
    printButton.grid(row=2, column=0, padx=95, pady=10)
    
    lbl2 = tk.Label(root, text = "")
    lbl2.grid()
    
    root.mainloop()


