from tkinter import *
from unicodedata import is_normalized  
from PIL import ImageTk,Image
from matplotlib.font_manager import is_opentype_cff_font
import time

root = Tk()  
root.title("main page") #the title of the window

canvas = Canvas(root, width = 800, height = 500) #the overall size of the window
canvas1 = Label(root, text="Welcome User: Riel") #included a text at the bottom of the window
canvas.pack() #we are uploading it to the window
canvas1.pack() #we are uploading it to the window 

carimage = Image.open("car.png") #getting the image car
car1 = carimage.rotate(270, expand=True) #we care rotating it and fitting the whole IMAGE
#This will display your image at 1/3 the size:
                        #   (x porition      y position)   , resampling filter
car = car1.resize((int(car1.size[0]/3),int(car1.size[1]/3)), 0) #resizing the image
img = ImageTk.PhotoImage(car) #we are uploading the image
canvas.create_image(550, 100, anchor=NW, image=img) #this is the iamge position   

#top     
waveA1 = Image.open("images/wave.png")
waveA2 = waveA1.rotate(270, expand = True)
waveA3 = waveA2.resize((int(waveA2.size[0]/3),int(waveA2.size[1]/3)), 0)
img2 = ImageTk.PhotoImage(waveA3)
canvas.create_image(582, 60, anchor = NW, image = img2)

#back
waveB1 = Image.open("images/wave.png")
waveB2 = waveB1.rotate(450, expand = True)
waveB3 = waveB2.resize((int(waveB2.size[0]/3),int(waveB2.size[1]/3)), 0)
img3 = ImageTk.PhotoImage(waveB3)
canvas.create_image(582, 365, anchor = NW, image = img3)

#left
waveC1 = Image.open("images/wave.png")
waveC2 = waveC1.rotate(0, expand = True)
waveC3 = waveC2.resize((int(waveC2.size[0]/3),int(waveC2.size[1]/3)), 0)
img4 = ImageTk.PhotoImage(waveC3)
canvas.create_image(510, 210, anchor = NW, image = img4)

#right
waveD1 = Image.open("images/wave.png")
waveD2 = waveD1.rotate(180, expand = True)
waveD3 = waveD2.resize((int(waveD2.size[0]/3),int(waveD2.size[1]/3)), 0)
img5 = ImageTk.PhotoImage(waveD3)
canvas.create_image(665, 210, anchor = NW, image = img5)  

show = True

def on_click1top():
   global show
   # Determine if the image is hidden or not
   if (show == True):#if the show == true then run the programm
      while(show == True):
          canvas.itemconfig(2, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
          time.sleep(2)
          canvas.itemconfig(2, state='normal')
          time.sleep(2)
      show = False
   else:#if the show == fale then run the program
      canvas.itemconfig(2, state='normal')
      show = True

def on_click2back():
   global show
   # Determine if the image is hidden or not
   if show:#if the show == true then run the programm
      canvas.itemconfig(3, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
      time.sleep(2)
      show = False
   else:#if the show == fale then run the program
      canvas.itemconfig(3, state='normal')
      show = True

def on_click3left():
   global show
   # Determine if the image is hidden or not
   if show:#if the show == true then run the programm
      canvas.itemconfig(4, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
      show = False
   else:#if the show == fale then run the program
      canvas.itemconfig(4, state='normal')
      show = True

def on_click4right():
   global show
   # Determine if the image is hidden or not
   if show:#if the show == true then run the programm
      canvas.itemconfig(5, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
      show = False
   else:#if the show == fale then run the program
      canvas.itemconfig(5, state='normal')
      show = True      

# Butt1 = Button(root, text="Show/Hide top", command=on_click1top)
# Butt1.pack()
# Butt2 = Button(root, text="Show/Hide back", command=on_click2back)
# Butt2.pack()
# Butt3 = Button(root, text="Show/Hide right", command=on_click3left)
# Butt3.pack()
# Butt4 = Button(root, text="Show/Hide left", command=on_click4right)
# Butt4.pack()

Butt1 = Button(root, text="Show/Hide top - range 1", command=on_click1top)
Butt1.pack()
Butt2 = Button(root, text="Show/Hide back - range 1", command=on_click2back)
Butt2.pack()
Butt3 = Button(root, text="Show/Hide right - range 1", command=on_click3left)
Butt3.pack()
Butt4 = Button(root, text="Show/Hide left - range 1", command=on_click4right)
Butt4.pack()
# def front:
#     on
    
# def back:
    
# def left:

# def right:

#------------------------------------------------------
# global is_on
# is_on = True

# #creating Label
# my_label = Label(root, text = "The Switch Is On!", fg="green", font=("Helvetica", 32))
# my_label.pack(pady=20)

# #define our switch function
# def switch():
#     global is_on # so we can access out side 

#     #determine is on or off
#     if is_on: #mean if is_on its true
#         on_button.config(image=off)
#         is_on= False
#     else:
#         on_button.config(image=on)
#         is_on = True
# #define Our Images
# on = PhotoImage(file = "images/on.png")
# off = PhotoImage(file = "images/off.png")

# #create A button
# on_button = Button(root, image = on, bd=0, command = switch)
# on_button.pack(pady=50)
#-----------------------------------------------------
 
root.mainloop() 

