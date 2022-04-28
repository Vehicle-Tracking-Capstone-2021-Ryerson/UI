from tkinter import *
from PIL import ImageTk,Image
import time
import speeding
import accidentDet
import helpers
import socket

show = True
    
def main(s): #s
    
    #print("TEST" + s)  
     
    root = Tk()  
    root.title("main page") #the title of the window
     
    def clock():
      hour = time.strftime("%H")
      minute = time.strftime("%M")
      second = time.strftime("%S")
      day = time.strftime("%d")
      month = time.strftime("%B")
      year = time.strftime("%Y")
      mylabel.config(text = (hour + ":" + minute + ":" + second))
      mydate.config(text = (day + " " + month + ", " + year))
      mylabel.after(1000, clock)
        
    mylabel = Label(root, width = 0, height=0, text="", font=("Helvetica", 12))
    mylabel.place(x=400, y=0, anchor = N) #grid(row = 0, column = 1)    
    mydate = Label(root, text="", font=("Helvetica", 12))
    mydate.place(x=393, y=20, anchor = N) #grid(row = 1, column = 1)
    
    clock()    
#----------------------------------------------------------------------------------    
        
    def gps():
      var = helpers.getLastGPSPoint()
      labelgps = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
      labelgps.config(text = ("[GPS]Latitude: " +str(var["lat"]) + "\nLongitude: " +str(var["lon"]) + "\nStreet: " + str(var["street"]) + "\nspeed: " + str(var["speed"]) + "\nTime: " +str(var["time"]) ))
      labelgps.place(x=30, y=40)#grid(row = 2, column = 0,pady = 10)
      labelgps.after(1000, gps)


    
    def blindspotF():
      var2a = helpers.getLastBlindspot(posa)
      labelblindspotF.config(text = ("[Front]Data: " + str(var2a["data"]) +" -- "+ str(var2a["time"]) ))
      if (int(var2a["data"]) < 60):
            canvas.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = 
            show = False
      else:
          canvas.itemconfig(1, state='normal')
          show = True
      labelblindspotF.place(x=30, y=135)
      labelblindspotF.after(1000, blindspotF)

    	     	
    def blindspotB():
      var2b = helpers.getLastBlindspot(posb)
      labelblindspotB.config(text = ("[Back]Data: " + str(var2b["data"]) +" -- "+ str(var2b["time"]) ))
      if (int(var2b["data"]) < 60):
          canvas2.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = 
          show = False
      else:
          canvas2.itemconfig(1, state='normal')
          show = True
      labelblindspotB.place(x=30, y=158)#grid(row = 4, column = 0,pady = 10)
      labelblindspotB.after(1000, blindspotB)      
         	

    def blindspotL():
      var2c = helpers.getLastBlindspot(posc)
      labelblindspotL.config(text = ("[Left]Data: " + str(var2c["data"]) +" -- "+ str(var2c["time"]) ))
      if (int(var2c["data"]) < 60):
          canvas3.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = 
          show = False
      else:
          canvas3.itemconfig(1, state='normal')
          show = True
      labelblindspotL.place(x=30, y=181)#grid(row = 3, column = 1,padx=10)
      labelblindspotL.after(1000, blindspotL)
          
    def blindsportR():
      var2d = helpers.getLastBlindspot(posd)
      labelblindspotR.config(text = ("[Right]Data: " + str(var2d["data"]) +" -- "+ str(var2d["time"]) ))
      if (int(var2d["data"]) < 60):
            canvas4.itemconfig(1, state='hidde')
            shoe = False
      else:
            canvas4.itemconfig(1, state='normal')
            show = True
      labelblindspotR.place(x=30, y=204)#grid(row = 4, column = 1,pady = 20,padx=10)
      labelblindspotR.after(1000, blindsportR)
            
    
    def OBD():
      var3 = helpers.getLastOBD()
      labelOBD = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
      labelOBD.config(text = ("[OBD]RPM: " + str(var3["rpm"]) + "\nSpeed: " + str(var3["speed"]) + "\nThrottle: " + str(var3["throttle"]) + "\nAirTemp: " + str(var3["airTemp"]) + "\nFuel: " + str(var3["fuel"]) + "\nTime: " +str(var3["time"])  ))
      labelOBD.place(x=30, y=230)#grid(row = 5, column = 0,pady = 10)
      speed()#///////////////
      accid()#///////////////    	      
      labelOBD.after(1000, OBD)

    #         OBD              GPS
    #        111               100
    #         10               100
    def speed():
    	var = helpers.getLastGPSPoint()
    	var3 = helpers.getLastOBD()
    	if (var3["speed"] > (var["speed"])):
    		speeding.speed(var3["speed"])
    def accid():
    	if (var3["rpm"] == 0):
    		print(var3["rpm"])
    		accidentDet.accident() 

    posa = "F"
    posb = "B"
    posc = "L"
    posd = "R"
        
    var = helpers.getLastGPSPoint()
    print("Get Last GPS Point: " + str(var))
    
    var2a = helpers.getLastBlindspot(posa)
    print("Get Last Blind Spot" + str(var2a))
    var2b = helpers.getLastBlindspot(posb)
    print("Get Last Blind Spot" + str(var2b))
    var2c = helpers.getLastBlindspot(posc)
    print("Get Last Blind Spot" + str(var2c))
    var2d = helpers.getLastBlindspot(posd)
    print("Get Last Blind Spot" + str(var2d))        
    
    var3 = helpers.getLastOBD()
    print("Get Last OBD" + str(var3))
    
    
    labelgps = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
    labelgps.place(x=30, y=40)#grid(row = 2, column = 0,pady = 10)
    labelgps.after(1000, gps)
    
    
    labelblindspotF = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
    labelblindspotF.place(x=30, y=135)#grid(row = 3, column = 0)
    labelblindspotF.after(1000, blindspotF)
    
    labelblindspotB = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
    labelblindspotB.place(x=30, y=158)#grid(row = 4, column = 0,pady = 10)
    labelblindspotB.after(1000, blindspotB)
    
    labelblindspotL = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
    labelblindspotL.place(x=30, y=181)#grid(row = 3, column = 1,padx=10)
    labelblindspotL.after(1000, blindspotL)
    
    labelblindspotR = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
    labelblindspotR.place(x=30, y=204)#grid(row = 4, column = 1,pady = 20,padx=10)
    labelblindspotR.after(1000, blindsportR)


    labelOBD = Label(root, width = 0, height=0, text="", font=("Helvetica", 12), bd = 1, relief = "sunken", justify = "left")
    labelOBD.place(x=30, y=230)#grid(row = 5, column = 0,pady = 10)
    labelOBD.after(1000, OBD)    
    
#-----------------------------------------------------------        
    #800 400
    #canvas = Canvas(root, width = 800, height = 400) #the overall size of the window    
    root.geometry("800x400")
    #root.configure(bg='yellow')
    canvas1 = Label(root, text="Welcome User - AA02")
    #") #included a text at the bottom of the window
    #canvas.pack()#grid(row = 7, column = 3)#we are uploading it to the window
    canvas1.place(x=350, y=370)#grid(row = 6, column = 1)#we are uploading it to the window 
    
    
    canvas = Canvas(root, width = 80, height=60)    
    canvas.place(x=580,y=10)
    canvas2 = Canvas(root, width = 80, height=60)    
    canvas2.place(x=580,y=316) 
    canvas3 = Canvas(root, width = 60, height=80)    
    canvas3.place(x=500,y=155)
    canvas4 = Canvas(root, width = 60, height=80)    
    canvas4.place(x=670,y=155)         
           
#-------------------------------------------------------------   
    carimage = Image.open("car.png") #getting the image car
    car1 = carimage.rotate(270, expand=True) #we care rotating it and fitting the whole IMAGE
    #This will display your image at 1/3 the size:
                            #   (x porition      y position)   , resampling filter
    car = car1.resize((int(car1.size[0]/3),int(car1.size[1]/3)), 0) #resizing the image
    img = ImageTk.PhotoImage(car) #we are uploading the image
    #canvas.create_image(100, 40, anchor=NW, image=img)#(550, 40, anchor=NW, image=img) #this is the iamge position   
    labelcar = Label(root, image = img)
    labelcar.place(x=550,y=50)
   
    #top     
    waveA1 = Image.open("images/wave.png")
    waveA2 = waveA1.rotate(270, expand = True)
    waveA3 = waveA2.resize((int(waveA2.size[0]/3),int(waveA2.size[1]/3)), 0)
    img2 = ImageTk.PhotoImage(waveA3)
    canvas.create_image(40, 30, image = img2, anchor = CENTER)
        
    #back
    waveB1 = Image.open("images/wave.png")
    waveB2 = waveB1.rotate(450, expand = True)
    waveB3 = waveB2.resize((int(waveB2.size[0]/3),int(waveB2.size[1]/3)), 0)
    img3 = ImageTk.PhotoImage(waveB3)
    canvas2.create_image(40, 30, image = img3, anchor = CENTER)
    
    #left
    waveC1 = Image.open("images/wave.png")
    waveC2 = waveC1.rotate(0, expand = True)
    waveC3 = waveC2.resize((int(waveC2.size[0]/3),int(waveC2.size[1]/3)), 0)
    img4 = ImageTk.PhotoImage(waveC3)
    canvas3.create_image(40, 40, anchor = CENTER, image = img4)
    
    #right
    waveD1 = Image.open("images/wave.png")
    waveD2 = waveD1.rotate(180, expand = True)
    waveD3 = waveD2.resize((int(waveD2.size[0]/3),int(waveD2.size[1]/3)), 0)
    img5 = ImageTk.PhotoImage(waveD3)
    canvas4.create_image(30, 40, anchor = CENTER, image = img5) 

    '''def on_click1top():
       global show
       # Determine if the image is hidden or not
       if (show == True):#if the show == true then run the programm
          #while(show == True):
          canvas.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
              #time.sleep(2)
              #canvas.itemconfig(2, state='normal')
              #time.sleep(2)
          show = False
       else:#if the show == fale then run the program
          canvas.itemconfig(1, state='normal')
          show = True'''
              
    #Recording
    Butt1 = Button(root, text="Record", command= lambda: helpers.beginRecord(s))
    Butt1.pack(anchor = E, pady = 75 )
    
    #Ending session
    Butt2 = Button(root, text="END SESSION", command= lambda: helpers.endSession(s))
    Butt2.pack(anchor = E, pady = 30 )
        
    '''
    def on_click1top():
       global show
       # Determine if the image is hidden or not
       if (show == True):#if the show == true then run the programm
          #while(show == True):
          canvas.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
              #time.sleep(2)
              #canvas.itemconfig(2, state='normal')
              #time.sleep(2)
          show = False
       else:#if the show == fale then run the program
          canvas.itemconfig(1, state='normal')
          show = True
 
    def on_click2back():
       global show
       # Determine if the image is hidden or not
       if show:#if the show == true then run the programm
          canvas2.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
          time.sleep(2)
          show = False
       else:#if the show == fale then run the program
          canvas2.itemconfig(1, state='normal')
          show = True
    
    def on_click3left():
       global show
       # Determine if the image is hidden or not
       if show:#if the show == true then run the programm
          canvas3.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
          show = False
       else:#if the show == fale then run the program
          canvas3.itemconfig(1, state='normal')
          show = True
    
    def on_click4right():
       global show
       # Determine if the image is hidden or not
       if show:#if the show == true then run the programm
          canvas4.itemconfig(1, state='hidden')  #(the layers of the canvas since 1 = the car 2 = top wave 3=back wave etc )
          show = False
       else:#if the show == fale then run the program
          canvas4.itemconfig(1, state='normal')
          show = True 

    if ((var3["speed"]) > (var["speed"])):
    	speeding.speed(var3["speed"])
    
          
    Butt1 = Button(root, text="Show/Hide top - range 1", command=on_click1top)
    Butt1.pack()
    
    Butt2 = Button(root, text="Show/Hide back - range 1", command=on_click2back)
    Butt2.pack()
        
    
    Butt3 = Button(root, text="Show/Hide left - range 1", command=on_click3left)
    Butt3.pack()
    Butt4 = Button(root, text="Show/Hide right - range 1", command=on_click4right)
    Butt4.pack()
    

    def slide(var):
         while (horizontal.get() == 50):
             speeding.speed()
             speeding.Close()
             break
         while(horizontal.get() == 100):
             accidentDet.accident()
        
    horizontal = Scale(root, from_ = 0, to=100, orient = HORIZONTAL, command = slide)
    horizontal.pack()'''


    root.mainloop() 
    
    


