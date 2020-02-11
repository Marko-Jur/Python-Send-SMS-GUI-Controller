import tkinter
import pygame
import serial
import pygame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math

#Global Variables:
GRAPHLINECOLOUR ='red'
MAINSCREEN = 'oven.gif'
OPTIONSSCREEN = 'Oven2.gif'
userName = 'test'
NOTIFICATION = 'not yet'
USERNUMBER = 121

#Com ports:
ARDUINOPORT = 'COM10' #Port of arduino
PUTTYPORT = 'COM7' #Port of Putty

#test
i = 1

#Global button Colours
BUTTONCOLOUR = '#33AAFF'
BUTTONCOLOURFLASH = 'grey'
BUTTONFOREGROUND = 'black'
OPTIONSBUTTONCOLOUR = '#3379FF'
GRAPHBUTTONCOLOUR = 'black'
TEXTMESSAGEBUTTONCOLOUR = 'red'
###################################################################################################################################
def checkPuttyPort():
    global PUTTYPORT
    PUTTYPORT = PUTTYPORT.get()
    
    showPutty = Label(window, text = 'Putty: ' + PUTTYPORT, font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showPutty.place(x = 790, y = 500)

    PUTTYPORT = "'" + PUTTYPORT + "'"
    #print(PUTTYPORT)

###################################################################################################################################
def checkArduinoPort():
    global ARDUINOPORT
    ARDUINOPORT = ARDUINOPORT.get()
    
    showArduino = Label(window, text = 'Arduino: ' + ARDUINOPORT, font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showArduino.place(x = 790, y = 600)

    ARDUINOPORT = "'" + ARDUINOPORT + "'"
    #print(ARDUINOPORT)

##################################################################################################################################
def comSetter():
    global ARDUINOPORT
    global PUTTYPORT

    # Clearing everything:
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Putty Port
    PUTTYPORT = Entry(window, background = 'grey')
    PUTTYPORT.place(x  = 790, y = 465)

    enterPuttyButton = Button(window,text="Enter Putty port",width = 16, background = 'yellow', fg = 'black', activebackground = 'grey',  command = checkPuttyPort)
    enterPuttyButton.place(x=650,y=460)

    #Arduino port
    ARDUINOPORT = Entry(window, background = 'grey')
    ARDUINOPORT.place(x = 790, y = 565)

    enterNumberButton = Button(window,text="Enter number",width = 16, background = 'yellow', fg = 'black', activebackground = 'grey',command = checkArduinoPort)
    enterNumberButton.place(x=650,y=560)

    doneButton = Button(window,text="Done",width = 16, background = 'yellow', fg = 'black', activebackground = 'grey', command = mainMenu)
    doneButton.place(x='650',y=660)


###################################################################################################################################

def pythonGraph():

        #Opening the port
        #Putty = serial.Serial(port= PUTTYPORT,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_TWO)

        def data_gen():
                t = data_gen.t

                while True:
                        t+=1
                        #Read output from arduino serial port
                        getLine = Putty.read(4)
                        puttyNumber = int(getLine)

                        #Convert the number into format readable by python
                        print(puttyNumber)
                        yield t, puttyNumber
        
        def run(data):
                # update the data
                t,y = data
                if t>-1:
                        xdata.append(t)
                        ydata.append(y)
                        if t>xsize: # Scroll to the left.
                                ax.set_xlim(t-xsize, t)
                        line.set_data(xdata, ydata)
                return line,

        def on_close_figure(event):
                sys.exit(0)
       
        while 1 :
                xsize=600
                data_gen.t = -1
                fig = plt.figure()
                fig.canvas.mpl_connect('close_event', on_close_figure)
                ax = fig.add_subplot(111)
                line, = ax.plot([], [], lw=2,color = GRAPHLINECOLOUR)
                ax.set_ylim(-10, 300)
                ax.set_xlim(0, xsize)
                ax.grid()
                xdata, ydata = [], []

                # Important: Although blit=True makes graphing faster, we need blit=False to prevent
                # spurious lines to appear when resizing the stripchart.
                ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=50, repeat=False)
                plt.show()
####################################################################################################################################

def graphScaling():
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    try:
        #Opening the port
        arduinoSerial = serial.Serial(port = ARDUINOPORT)
        arduinoSerial.isOpen()

        arduinoOutput = arduinoSerial.readline()
        displayNumber = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
        displayNumber = int(displayNumber)

        a = StringVar()
        a.set(displayNumber)

        
        while 1:
            arduinoOutput = arduinoSerial.readline()
            displayNumber = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
            displayNumber = int(displayNumber)
            print(displayNumber)
            testLabel = Label(window,textvariable = a, width = 24, background = 'black', fg = 'white')
            testLabel.place(x = 340, y = 710)
            testLabel.config(text=str(a))


            if (displayNumber > 30):
                x = mainMenu()
                arduinoSerial.close()

    except:
        errorLabel = Label(window, text = "Oooops!", font=("Comic Sans MS", 32), background = 'white', fg = 'black')
        errorLabel.place(x = 610, y = 460) 

        error2Label = Label(window, text = "Looks like your COM port is wrong, please reset your ports", font=("Comic Sans MS", 32), background = 'white', fg = 'black')
        error2Label.place(x = 130, y = 540) 

        #Button
        setComButton = Button(window,text="Set COM",width = 24, background ='yellow', fg = 'black', activebackground = 'grey', command = comSetter)
        setComButton.place(x = 620, y = 710)

        mainButton = Button(window,text="Go back",width = 24, background = 'yellow', fg = 'black', activebackground = 'grey', command = mainMenu)
        mainButton.place(x = 620, y = 760) 


    #arduinoOutputLabel = Label(window,textvariable = a, width = 24, background = 'black', fg = 'white')
    #arduinoOutputLabel.place(x = 340, y = 710)


####################################################################################################################################

def introToOven():
    pygame.init()
    from pygame import mixer
    mixer.init()
    mixer.music.load("C:/Users/Marko/Desktop/Work/Elec291/project 1/Code/Python GUI/harshproper.mp3")
    mixer.music.play()

    #intro
    first = Label(window, text = "Welcome to our Oven", font=("Comic Sans MS", 32), background = 'white', fg = 'black')
    first.place(x = 505, y = 460)
    
    #next line
    first2 = Label(window, text = "Where all soldering is possible", font=("Comic Sans MS", 32), background = 'white', fg = 'black')
    first2.place(x = 415, y = 560)


    #Button
    mainButton = Button(window,text="Proceed to Main Menu",width = 24, background = BUTTONCOLOUR, fg = 'black', activebackground = 'grey', command = mainMenu)
    mainButton.place(x = 640, y = 710)

#############################################################################################################################################################
def startProcess():

    # Clearing everything
    mainScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 100,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    soakTimeLabel = Label(window,text = 'Soak Time:', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    soakTimeLabel.place(x = 0, y = 470)

    soakTemperatureLabel = Label(window,text = 'Soak Temperature:', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    soakTemperatureLabel.place(x = 400, y = 470)

    reflowTimeLabel = Label(window,text = 'Reflow Time:', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    reflowTimeLabel.place(x = 800, y = 470)

    reflowTemperatureLabel = Label(window,text = 'Reflow Temperature:', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    reflowTemperatureLabel.place(x = 1200, y = 470)


##############################################################################################################################################################

def add():
    global i
    i += 1
    a = StringVar()
    a.set(i)
    print("new"+ str(a))
    testLabel = Label(window,textvariable = a, width = 24, background = 'black', fg = 'white')
    testLabel.place(x = 340, y = 710)
    testLabel.config(text=str(a))
    #window.update_idletasks()

##############################################################################################################################################################

def credits():
    mainScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 100,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    plusButton = Button(window,text="Proceed to Main Menu",width = 24, background = BUTTONCOLOUR, fg = 'black', activebackground = 'grey', command = add)
    plusButton.place(x = 640, y = 710)

     

##############################################################################################################################################################


# Change graph colours
def redLine():
    global COLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    COLOUR = 'red'
    redBox = Label(window, background = 'red', width = 8)
    redBox.place(x=800,y=460)



def blueLine():
    global COLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    COLOUR = 'blue'

    blueBox = Label(window, background = 'blue', width = 8)
    blueBox.place(x=800,y=510)

def yellowLine():
    global COLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    COLOUR = 'yellow'

    yellowBox = Label(window, background = 'yellow', width = 8)
    yellowBox.place(x=800,y=570)

def orangeLine():
    global COLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    COLOUR = 'orange'

    orangeBox = Label(window, background = 'orange', width = 8)
    orangeBox.place(x=800,y=630)


#Function taken from: https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
#################################################################################################################################

#Open the Ardunio serial port and read the data:
def arduino():
        #Opening the port
        while 1:
            arduinoSerial = serial.Serial(port = PORT)
            arduinoOutput = arduinoSerial.readline()
            displayNumber =int(arduinoOutput.decode())
            print(displayNumber)
            #arduinoData = Label(window, textvariable = arduinoOutput, width = 25, background = 'black', fg = 'blue').place(x = 10, y =70)


#################################################################################################################################

def Units():
    print("test")

def ovenNotification():
    global userName
    global NOTIFICATION
    Message1 = "Hello " + userName
    Message2 = ".\nYour oven has finished soldering!"
    Message3 = Message1 + Message2
    
    NOTIFICATION = Message3

##################################################################################################################################

def changeGraphColour():
    redButton = Button(window,text="Red",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH, fg = 'red', command = redLine)
    redButton.place(x=650,y=460)

    blueButton = Button(window,text="Blue",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'blue', command = blueLine)
    blueButton.place(x=650,y=510)

    yellowButton = Button(window,text="Yellow",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'yellow', command = yellowLine)
    yellowButton.place(x=650,y=560)

    orangeButton = Button(window,text="Orange",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'orange',command = orangeLine)
    orangeButton.place(x=650,y=610)
#################################################################################################################################

def checkUserName():
    user = userName.get()
    #print(user)
    showUserName = Label(window, text = "Hello " + user + "!", font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showUserName.place(x = 790, y = 500)

#################################################################################################################################

def checkUserNumber():
    userNum = USERNUMBER.get()
    #print(userNum)
    showUserName = Label(window, text = "Cool Number: " + userNum, font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showUserName.place(x = 790, y = 600)

##################################################################################################################################

def doneData():
    clearButton = Label(window,width = 19, background = 'white')
    clearButton.place(x  = 790, y = 465)

    clear2Button = Label(window,width = 19,  background = 'white')
    clear2Button.place(x  = 790, y = 470)

    clear3Button = Label(window,width = 19,  background = 'white')
    clear3Button.place(x = 790, y = 565)

    clear4Button = Label(window,width = 19,  background = 'white')
    clear4Button.place(x=483,y=570)

    clear5Button = Label(window,width = 19,  background = 'white')
    clear5Button.place(x=650,y=560)

    clear6Button = Label(window,width = 19,  background = 'white')
    clear6Button.place(x=650,y=565)

    clear7Button = Label(window,width = 19,  background = 'white')
    clear7Button.place(x=650,y=460)

    clear8Button = Label(window,width = 19,  background = 'white')
    clear8Button.place(x=650,y=465)

    clear9Button = Label(window,width = 19,  background = 'white')
    clear9Button.place(x=650,y=660)

    clear10Button = Label(window,width = 19,  background = 'white')
    clear10Button.place(x=650,y=665)

    clear11Button = Label(window,width = 19,  background = 'white')
    clear11Button.place(x = 790, y = 600)

    clear12Button = Label(window,width = 19,  background = 'white')
    clear12Button.place(x = 790, y = 500)

    clear13Button = Label(window,width = 19,  background = 'white')
    clear13Button.place(x = 790, y = 505)

    clear14Button = Label(window,width = 19,  background = 'white')
    clear14Button.place(x = 790, y = 605)

    clear15Button = Label(window,width = 40,  background = 'white')
    clear15Button.place(x = 800, y = 605)

    clear16Button = Label(window,width = 20,  background = 'white')
    clear16Button.place(x = 810, y = 505)

    clear17Button = Label(window,width = 20,  background = 'white')
    clear17Button.place(x = 820, y = 505)

    clear18Button = Label(window,width = 20,  background = 'white')
    clear18Button.place(x = 830, y = 505)

    name = userName.get()
    number = USERNUMBER.get()

    #Print text set message
    Message = Label(window,width = 60,  background = 'white', text = "Thank you " + name + ",you will be sent a text message at: ", font=("Comic Sans MS", 20), fg = 'black')
    Message.place(x = 220,y = 460)

    Message2 = Label(window,width = 40,  background = 'white', text = number , font=("Comic Sans MS", 20), fg = 'black')
    Message2.place(x = 395,y = 560)

    homeButton = Button(window,text="Return",width = 16, background = 'green', fg = 'black', activebackground = 'grey', command = mainMenu)
    homeButton.place(x= 650 ,y = 660)

    redoButton = Button(window,text="Redo",width = 16, background = 'green', fg = 'black', activebackground = 'grey', command = textMessageCreator)
    redoButton.place(x = 650, y = 710)

#################################################################################################################################

def textMessageCreator():
    global userName
    global USERNUMBER

    # covering up labels
    coverup = Label(window,width = 19, background = 'white')
    coverup.place(x = 650,y = 515)

    coverup1 = Label(window,width = 19, background = 'white')
    coverup1.place(x = 650,y = 510)

    coverup2 = Label(window,width = 19, background = 'white')
    coverup2.place(x = 650,y = 610)

    coverup2 = Label(window,width = 19, background = 'white')
    coverup2.place(x = 650,y = 615)

    #Covering up redo buttons

    coverup3 = Label(window,width = 19, background = 'white')
    coverup3.place(x= 650 ,y = 660)

    coverup4 = Label(window,width = 19, background = 'white')
    coverup4.place(x= 650 ,y = 665)

    coverup5 = Label(window,width = 19, background = 'white')
    coverup5.place(x = 650, y = 710)

    coverup6 = Label(window,width = 19, background = 'white')
    coverup6.place(x = 650, y = 715)

    #text cover
    coverup7 = Label(window,width = 300, background = 'white')
    coverup7.place(x = 220,y = 460)

    coverup8 = Label(window,width = 300, background = 'white')
    coverup8.place(x = 220,y = 465)

    coverup9 = Label(window,width = 300, background = 'white')
    coverup9.place(x = 220,y = 470)

    coverup10 = Label(window,width = 300, height = 300, background = 'white')
    coverup10.place(x = 220,y = 475)

    #Username
    userName = Entry(window, background = 'grey')
    userName.place(x  = 790, y = 465)

    enterNameButton = Button(window,text="Enter name",width = 16, background = TEXTMESSAGEBUTTONCOLOUR, fg = 'black', activebackground = 'grey',  command = checkUserName)
    enterNameButton.place(x=650,y=460)

    #User Number
    USERNUMBER = Entry(window, background = 'grey')
    USERNUMBER.place(x = 790, y = 565)

    enterNumberButton = Button(window,text="Enter number",width = 16, background = TEXTMESSAGEBUTTONCOLOUR, fg = 'black', activebackground = 'grey',command = checkUserNumber)
    enterNumberButton.place(x=650,y=560)

    doneButton = Button(window,text="Done",width = 16, background = TEXTMESSAGEBUTTONCOLOUR, fg = 'black', activebackground = 'grey', command = doneData)
    doneButton.place(x='650',y=660)

##########################################################################################################################################################
    
def changeMainScreen():
    global MAINSCREEN 
    MAINSCREEN = 'homer.gif'
    

#########################################################################################################################################################

def optionsMenu():
    
    #graph colour
    graphColourButton = Button(window,text="Graph Colour",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH,  command = changeGraphColour)
    graphColourButton.place(x=650,y=460)

    #Change Units
    changeUnitsButton = Button(window,text="Change Units",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH,  command = Units)
    changeUnitsButton.place(x=650,y=510)

    #Text Message
    textMessageButton = Button(window,text="Text Message",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = textMessageCreator)
    textMessageButton.place(x=650,y=560)

    #Oven
    #mainScreenButton = Button(window,text="Don't click the oven",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = changeMainScreen)
    #mainScreenButton.place(x=650,y=610)

    #Size graph
    graphSizeButton = Button(window,text="Graph size",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = graphScaling)
    graphSizeButton.place(x=650,y=610)

    #Set COM
    setCOMButton = Button(window,text="Set COMS",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = comSetter)
    setCOMButton.place(x=650,y=610)
    
    

################################################################################################################################
    
def mainMenu():

    # Clearing everything:
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)
    
   
    #startbutton
    startButton = Button(window,text="Start", width = 16, background = BUTTONCOLOUR , activebackground = BUTTONCOLOURFLASH  ,  fg = 'black',command = startProcess)
    startButton.place(x=650,y=460)
    

    #Options button
    optionsButton = Button(window,text="Options",width = 16, background = BUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH, command = optionsMenu)
    optionsButton.place(x=650,y=510)

    #Print Graph button
    printGraphButton = Button(window,text="Print Graph",width = 16, background = BUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH, command = pythonGraph)
    printGraphButton.place(x=650,y=560)

    #Go back 
    goBackButton = Button(window,text="Go back",width = 16, background = BUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = mainMenu) 
    goBackButton.place(x=2,y=4)
    
    #Credits
    creditsButton = Button(window,text="Credits",width = 16, background = BUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH, command = credits)
    creditsButton.place(x=650,y=610)



    window.mainloop()

##################################################################################################################################

#Main Program
#Tkinter main menu:
from tkinter import *
#Creating window 
window = Tk()
window.title("Oven Controller")
window.configure(background="white")
full =FullScreenApp(window)

#Adding gif to the window
mainImage = PhotoImage(file = MAINSCREEN)
Label(window, image = mainImage, bg = "white") .grid(row = 0, column = 0, padx  =480, pady = 0)

#Calling functions:
intro = introToOven()
#mainmenu = mainMenu()


#Loop the Window
window.mainloop()

