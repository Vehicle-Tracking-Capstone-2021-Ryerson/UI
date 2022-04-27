#Import the required libraries
from multiprocessing.connection import wait
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time
import helpers

	
def speed(speed):
	#Create an instance of tkinter frame
    root1 = tk.Tk()
    root1.title("Speeding")
    root1.geometry("450x200")
        
    var = helpers.getLastGPSPoint()   
    
    a = Label(root1, text = "WARNING Speed Detection, Please Slow Down\nMessage will disppear once appropate speed", anchor = CENTER)
    a.pack(expand = True)
    
    
    print(speed)
    #      OBD        GPD
    if (speed < (var["speed"])): 
    	root1.destroy()
    root1.mainloop()
    
  
