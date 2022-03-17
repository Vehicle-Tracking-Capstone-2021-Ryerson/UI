# from tkinter import *
# #from unicodedata import is_normalized
# from PIL import ImageTk, Image

# root = Tk()
# root.geometry("1000x1000")
#creating a label widget
#myLabel = Label(root, text = "Hello World!").grid(row=0, column=0)#label widget
#myLabel2 = Label(root, text = "HIIIIIIII").grid(row=1,column =10) #label widget

#shoving it on the screen
#myLabel.pack()
#myLabel.grid(row=0, column=0)
#myLabel2.grid(row=1,column =10)

#loop event for the mouse to update until the program end


#myBUtton = Button(root, text = "Clock Me!", state=DISABLED)

#def myClick(): #a function
#    myLabel = Label(root, text="look I clicked a button!!")
#    myLabel.pack()


#myBUtton = Button(root, text = "Clock Me!", command=myClick)

#myBUtton.pack()

#keep track of the button state on/off
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
# on = PhotoImage(file= "images/on.png")
# off = PhotoImage(file= "images/off.png")

# #create A button
# on_button = Button(root, image = on, bd=0, command = switch)
# on_button.pack(pady=50)

# my_canvas = Canvas(root, width = 600/2, height = 400/2)
# my_canvas.pack(pady=20)

# my_img = ImageTk.PhotoImage(Image.open("images/wave.png"))
# my_label = Label(image = my_img)
# my_label.pack()

#root.mainloop()

# Import the required libraries
# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk

# # Create an instance of tkinter frame or window
# win = Tk()

# # Set the size of the window
# win.geometry("700x350")

# # Globally Declare the Boolean value
# show = True

# def on_click():
#    global show

#    # Determine if the image is hidden or not
#    if show: #if the show == true then run the programm
#       canvas.itemconfig(1, state='hidden')
#       show = False
#    else:   #if the show == fale then run the program
#       canvas.itemconfig(1, state='normal')
#       show = True

# # Add a Canvas widget
# canvas = Canvas(win, width=440, height=300)
# canvas.pack()

# # Add image to the canvas
# img = ImageTk.PhotoImage(file="car.png")
# canvas.create_image(200, 200, image=img, anchor=CENTER)

# # Add a Button to Show/Hide Canvas Items
# Button(win, text="Show/Hide", command=on_click).pack()

# win.mainloop()



