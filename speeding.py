#Import the required libraries
from multiprocessing.connection import wait
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time

def speed():
    #Create an instance of tkinter frame
    root = tk.Tk()
    root.title("Speeding")
    root.geometry("400x200")
    
    s = Style()
    s.configure('My.TFrame', background='red')
    mail1 = Frame(root, style='My.TFrame')
    mail1.place(height=500, width=500, x=0, y=0)
    
    def Close():
        root.destroy()
    
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl2.config(text = "Provided Input: "+inp)
        if (inp == "speed"):
            root.destroy()
    
    a = Label(root, text = "WARNING Speed Detection, Please Slow Down\nMessage will disppear once appropate speed", anchor = CENTER)
    #a2 = Label (root, text = "Message will disppear once appropate speed", anchor = CENTER)
 
    # TextBox Creation
    inputtxt = tk.Text(root, height = 1, width = 20)
    inputtxt.grid(row=1, column=0, padx=70, pady=6)
      
    # Button Creation
    printButton = tk.Button(root, text = "Enter", command = printInput)
    printButton.grid(row=3, column=0, padx=70, pady=6)
    
    mail1.config()
    a.grid(row=0, column=0, padx=70, pady=20)
    #a2.grid(row=1, column=0, padx=95, pady=10)
    
    lbl2 = tk.Label(root, text = "")
    lbl2.grid(row=2, column=0, padx=70, pady=6)
    
    root.mainloop()