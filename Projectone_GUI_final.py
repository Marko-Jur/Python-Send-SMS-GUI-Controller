import tkinter
import pygame
import serial
import pygame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import sys, time, math
import twilio

#Global Variables:
GRAPHLINECOLOUR ='red'
MAINSCREEN = 'oven.gif'
OPTIONSSCREEN = 'Oven2.gif'
USERNAME = 'test'
NOTIFICATION = 'not yet'
USERNUMBER = 121
GRAPHSIZE = 1
TESTMESSAGE = 'not yet'
GRAPHSCALE = 100

#Com ports:
ARDUINOPORT = 'COM9' #Port of arduino
PUTTYPORT = 'COM8' #Port of Putty
PLACEBOARDUINOPORT = 'COM1' #Placebo port of arduino
PLACEBOPUTTYPORT = 'COM3'

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
    global PLACEBOPUTTYPORT
    PLACEBOPUTTYPORT = PLACEBOPUTTYPORT.get()
    
    showPutty = Label(window, text = 'Putty: ' + PLACEBOPUTTYPORT, font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showPutty.place(x = 790, y = 500)

    PLACEBOPUTTYPORT = "'" + PLACEBOPUTTYPORT + "'"
    #print(PUTTYPORT)

###################################################################################################################################
def checkArduinoPort():
    global PLACEBOARDUINOPORT
    PLACEBOARDUINOPORT = PLACEBOARDUINOPORT.get()
    
    showArduino = Label(window, text = 'Arduino: ' +    PLACEBOARDUINOPORT, font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showArduino.place(x = 790, y = 600)

    PLACEBOARDUINOPORT = "'" + ARDUINOPORT + "'"
    PLACEBOARDUINOPORT = str(ARDUINOPORT)
    #print(ARDUINOPORT)

##################################################################################################################################
def comSetter():
    global PLACEBOARDUINOPORT
    global PLACEBOPUTTYPORT

    # Clearing everything:
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Putty Port
    PLACEBOPUTTYPORT = Entry(window, background = 'grey')
    PLACEBOPUTTYPORT.place(x  = 790, y = 465)

    enterPuttyButton = Button(window,text="Enter Putty port",width = 16, background = 'yellow', fg = 'black', activebackground = 'grey',  command = checkPuttyPort)
    enterPuttyButton.place(x=650,y=460)

    #Arduino port
    PLACEBOARDUINOPORT = Entry(window, background = 'grey')
    PLACEBOARDUINOPORT.place(x = 790, y = 565)

    enterNumberButton = Button(window,text="Enter Arduino port",width = 16, background = 'yellow', fg = 'black', activebackground = 'grey',command = checkArduinoPort)
    enterNumberButton.place(x=650,y=560)

    doneButton = Button(window,text="Done",width = 16, background = 'yellow', fg = 'black', activebackground = 'grey', command = mainMenu)
    doneButton.place(x='650',y=660)


###################################################################################################################################

def pythonGraph():
    global GRAPHLINECOLOUR
    print(GRAPHLINECOLOUR)

    #Opening the port
    Putty = serial.Serial(port= PUTTYPORT,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_TWO)
    plt.close('all')

    #previous putty
    previousPuttyNumber = 0 #
    puttyNumber = 0 #

    def data_gen():
        t = data_gen.t
        puttyNumber = 0 #

        while True:
            t+=1
            #Read output from putty serial port
            previousPuttyNumber = puttyNumber #
            getLine = Putty.read(4)
            puttyNumber = int(getLine)
            if (puttyNumber == 1):
                x = sendRealSMS()
                puttyNumber = previousPuttyNumber #
                print('TEST') #
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
        plt.close('all')
        Putty.close()
        x = mainMenu()
        #sys.exit(0)

    #plt.ion(blocking)
    fig = plt.figure()
        
    try:
        while 1 :
            xsize=600
            data_gen.t = -1
            plt.pause(0.01)
            #fig = plt.figure() # uncommetning this makes infinite windows
            fig.canvas.mpl_connect('close_event', on_close_figure)
            ax = fig.add_subplot(111)
            line, = ax.plot([], [], lw=2,color = GRAPHLINECOLOUR)
            ax.set_ylim(-10, GRAPHSCALE)
            ax.set_xlim(0, xsize)
            ax.grid()
            xdata, ydata = [], []

            #fig.canvas.draw() # updates figure
            # Important: Although blit=True makes graphing faster, we need blit=False to prevent
            # spurious lines to appear when resizing the stripchart.
            ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=1, repeat=False)
            plt.show()
            #window.update()
    except:
        Putty.close()
        
##################################################################################################################################
def setGraphMessage():
        #clearing everything
        mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
        mainScreenCoverup.place(x = 0,y = 450)

        main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
        main2ScreenCoverup.place(x = 240, y = 500)

        finalLabel = Label(window,text = 'Done! Graph Scale set to:' + GRAPHSIZE, width = 2,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
        finalLabel.place(x = 880, y = 710)

        yellowButton = Button(window,text="Yellow",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'yellow', command = yellowLine)
        yellowButton.place(x=650,y=560)
        x =mainMenu()
        



####################################################################################################################################
#Arduino Graph
def graphScaling():
    global GRAPHSIZE
    global GRAPHSCALE

    ratio = 100
    #cleraing data
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Setting up distance and timers
    distanceHeaderLabel = Label(window,text = 'Distance', width = 7,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    distanceHeaderLabel.place(x = 880, y = 470)

    cmLabel = Label(window,text = 'Cm', width = 2,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    cmLabel.place(x = 930, y = 510)

    scaleHeaderLabel = Label(window, text = 'Scale' , width = 4,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE))
    scaleHeaderLabel.place(x = 1175, y = 470)

    
    scaleLabel = Label(window,text = ' X 600', width = 4,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    scaleLabel.place(x = 1200, y = 510)

    window.update()
    
    try:
        #Opening the port
        arduinoSerial = serial.Serial(port = ARDUINOPORT)
        arduinoOutput = arduinoSerial.readline()
        GRAPHSIZE = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
        GRAPHSIZE = int(GRAPHSIZE)
        #print(GRAPHSIZE)
        displayColour = 'green'

        def on_close_figure(event):
                        plt.close('all')
                        #x = mainMenu()
                        #sys.exit(0)

        plt.ion()
        fig = plt.figure()

        #setting graphsize as variable
        a = StringVar()
        a.set(GRAPHSIZE)

        #getting base time
        baseSeconds = time.time()

        #setting scale as variable
        scaler = StringVar()
        scaler.set(GRAPHSIZE * ratio)

        while GRAPHSIZE > 1:
            #Read output from arduino serial port
            #while counter > 0:
                arduinoOutput = arduinoSerial.readline()
                GRAPHSIZE = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
                GRAPHSIZE = int(GRAPHSIZE)
                xsize=600
                fig.canvas.mpl_connect('close_event', on_close_figure)
                ax = fig.add_subplot(111)
                line, = ax.plot([], [], lw=2,color = 'red')
                ax.set_ylim(0, GRAPHSIZE * ratio) 
                ax.set_xlim(0, xsize)
                ax.grid()
                plt.pause(0.1)
                fig.canvas.draw()
                
                #Setting variables
                a.set(GRAPHSIZE)
                #scaler.set(GRAPHSIZE * ratio)
                #print('test')
                #printing variables
                #distance
                distanceLabel = Label(window,textvariable = a, width = 2,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
                distanceLabel.place(x = 880, y = 510)
                
                distanceLabel.config(text=str(a))
                aboutToSetLabel = Label(window, width = 4,height = 2, background = 'green', fg = 'black')
                aboutToSetLabel.place(x = 1000, y = 510)
                
                #scale
                b = GRAPHSIZE * ratio
                scaler.set(b)
                scaleLabel = Label(window,textvariable = scaler , width = 3,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
                scaleLabel.place(x = 1150, y = 510)
                scaleLabel.config(text=str(a))


                #Comparing seconds
                compareSeconds =time.time()
                testSeconds1 = compareSeconds - 5
                testSeconds2 = compareSeconds - 8
                testSeconds3 = compareSeconds - 11
                count = 0 
                
                window.update()
                if  (testSeconds1 > baseSeconds) and count == 0 :
                    aboutToSetLabel = Label(window, width = 4,height = 2, background = 'yellow', fg = 'black')
                    aboutToSetLabel.place(x = 1000, y = 510)
                    count += 1

                    window.update()

                if  testSeconds2 > baseSeconds:
                    aboutToSetLabel = Label(window, width = 4,height = 2, background = 'red', fg = 'black')
                    aboutToSetLabel.place(x = 1000, y = 510)
                    count = 0        
            
                    #scaleNumberLabel = Label(window,text = '100' + 'X 600' , width = 3,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
                    #scaleNumberLabel.place(x = 1200, y = 810)
                    window.update()
                    while count < 10000:
                        count+=1
                        print(count)
                    break

        window.update()     
        plt.close('all')

        print('test')
        GRAPHSIZE = GRAPHSIZE
        GRAPHSCALE = GRAPHSIZE * ratio
        #print (GRAPHSCALE)
        arduinoSerial.close()
        x = mainMenu()


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

    #Clearing everyhing
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)


    #intro
    first = Label(window, text = "Welcome to our Oven", font=("Comic Sans MS", 32), background = 'white', fg = 'black')
    first.place(x = 505, y = 460)
    
    #next line
    first2 = Label(window, text = "Where all soldering is possible", font=("Comic Sans MS", 32), background = 'white', fg = 'black')
    first2.place(x = 415, y = 560)


    #Button
    mainButton = Button(window,text="Proceed to Main Menu",width = 24, background = BUTTONCOLOUR, fg = 'black', activebackground = 'grey', command = mainMenu)
    mainButton.place(x = 640, y = 710)
    window.update()
    #x = motionProceed() #Change forms here
    #x = mainMenu()
############################################################################################################################################################
def motionProceed():
    arduinoSerial = serial.Serial(port = ARDUINOPORT)
    arduinoSerial.isOpen()

    arduinoOutput = arduinoSerial.readline()
    displayNumber = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
    displayNumber = int(displayNumber)


    while displayNumber > 10:
        #print(displayNumber)
        arduinoOutput = arduinoSerial.readline()
        displayNumber = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
        displayNumber = int(displayNumber)
    
    arduinoSerial.close()
    x =mainMenu()
#############################################################################################################################################################

#############################################################################################################################################################
def startProcess():

    # Clearing everything
    mainScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 100,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Putty = serial.Serial(port= PUTTYPORT,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_TWO)
    #Putty.isOpen()

    #Reprinting back button
    #Go back 
    goBackButton = Button(window,text="Go back",width = 16, background = BUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = mainMenu()) 
    goBackButton.place(x=2,y=4)

    soakTemperatureLabel = Label(window,text = 'Oven Temperature:', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20,UNDERLINE) )
    soakTemperatureLabel.place(x = 600, y = 470)

    #Setting up the temp label
    #scaleLabel = Label(window,text = '28' , width = 3,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 80) )
    #scaleLabel.place(x = 640, y =550)
   
    window.update()
############################################################################################################################################
    #Opening the port
    
    Putty = serial.Serial(port= PUTTYPORT,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_TWO)
    Putty.isOpen()

    #Get line
    getLine = Putty.read(4)
    puttyNumber = int(getLine.decode())
    
    a = StringVar()
    a.set(puttyNumber)

    while 1:
        getLine = Putty.read(4)
        puttyNumber = int(getLine.decode())
        print(puttyNumber)
        a.set(puttyNumber)
        scaleLabel = Label(window,textvariable = a , width = 3,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 80) )
        scaleLabel.place(x = 640, y = 550)
        scaleLabel.config(text=str(a))
        window.update()
        if (puttyNumber == 80):
            Putty.close()
            break


##########################################################################################################################################


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

    #Clearing screen
    mainScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 100,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Reprinting back button
    #Go back 
    goBackButton = Button(window,text="Go back",width = 16, background = BUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = mainMenu) 
    goBackButton.place(x=2,y=4)

    # Printing names

    HarshLabel = Label(window,text = 'Harsh Rajoria', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
    HarshLabel.place(x = 584, y = 500)

    YemiLabel = Label(window,text = 'Yemi ' + 'DSEG ' + 'Oke', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
    YemiLabel.place(x = 584, y = 550)

    JinLabel = Label(window,text = 'Jin Hee Yun', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
    JinLabel.place(x = 584, y = 600)

    MarkoLabel = Label(window,text = 'Marko Jurisic', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
    MarkoLabel.place(x = 570, y = 650)

    TaherLabel = Label(window,text = 'Taher Kathawala', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
    TaherLabel.place(x = 570, y = 700)

    TaherLabel = Label(window,text = 'Janith Wijekoon', width = 15,height = 1, background = 'white', fg = 'black', font = ("MS Sans Serif", 20) )
    TaherLabel.place(x = 570, y = 750)

##############################################################################################################################################################

# Change graph colours
def redLine():
    global GRAPHLINECOLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    GRAPHLINECOLOUR = 'red'
    redBox = Label(window, background = 'red', width = 8)
    redBox.place(x=800,y=460)



def blueLine():
    global GRAPHLINECOLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    GRAPHLINECOLOUR = 'blue'

    blueBox = Label(window, background = 'blue', width = 8)
    blueBox.place(x=800,y=510)

def yellowLine():
    global GRAPHLINECOLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    GRAPHLINECOLOUR = 'yellow'

    yellowBox = Label(window, background = 'yellow', width = 8)
    yellowBox.place(x=800,y=570)

def orangeLine():
    global GRAPHLINECOLOUR
    #Clearing the screen
    clear = Label(window, background = 'white', width = 8)
    clear.place(x=800,y=460)

    clear2 = Label(window, background = 'white', width = 8)
    clear2.place(x=800,y=510)

    clear3 = Label(window, background = 'white', width = 8)
    clear3.place(x=800,y=570)

    clear4 = Label(window, background = 'white', width = 8)
    clear4.place(x=800,y=630)

    GRAPHLINECOLOUR = 'orange'

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
def testMessageCreate():
    global TESTMESSAGE
    Message = "\nHello " + USERNAME + "\nthis is a test message from your oven"

    TESTMESSAGE = Message

    
##################################################################################################################################

def ovenNotification():
    global USERNAME
    global NOTIFICATION
    Message1 = "Hello " + USERNAME
    Message2 = ".\nYour oven has finished soldering!"
    Message3 = Message1 + Message2
    
    NOTIFICATION = Message3
    print(NOTIFICATION)
    

##################################################################################################################################

def changeGraphColour():
    #Clearing screen
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    redButton = Button(window,text="Red",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH, fg = 'red', command = redLine)
    redButton.place(x=650,y=460)

    blueButton = Button(window,text="Blue",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'blue', command = blueLine)
    blueButton.place(x=650,y=510)

    yellowButton = Button(window,text="Yellow",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'yellow', command = yellowLine)
    yellowButton.place(x=650,y=560)

    orangeButton = Button(window,text="Orange",width = 16, background = GRAPHBUTTONCOLOUR, activebackground = BUTTONCOLOURFLASH,  fg = 'orange',command = orangeLine)
    orangeButton.place(x=650,y=610)
#################################################################################################################################

def sendTestSMS():
    global TESTMESSAGE
    global USERNUMBER
    x = testMessageCreate()

    # we import the Twilio client from the dependency we just installed
    from twilio.rest import Client

    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC99e9e01f137d4f28043bba819a9c8cc3", "3ccbf1dbb4fcadbf8d2923957d33f824")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to=USERNUMBER, 
                        from_="+17316024317", 
                        body=TESTMESSAGE)

#######################################################################################################################################
def sendRealSMS():
    global NOTIFICATION
    global USERNUMBER
    x = testMessageCreate()

    # we import the Twilio client from the dependency we just installed
    from twilio.rest import Client

    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC99e9e01f137d4f28043bba819a9c8cc3", "3ccbf1dbb4fcadbf8d2923957d33f824")

    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to=USERNUMBER, 
                        from_="+17316024317", 
                        body=NOTIFICATION)

########################################################################################################################################

def checkUserName():
    global USERNAME
    USERNAME = userName.get()
    #print(user)
    showUserName = Label(window, text = "Hello " + USERNAME + "!", font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showUserName.place(x = 790, y = 500)

#################################################################################################################################

def checkUserNumber():
    global USERNUMBER
    USERNUMBER = '+1' + userNum.get()
    #print(userNum)
    showUserName = Label(window, text = "Cool Number: " + USERNUMBER, font=("Comic Sans MS", 16), background = 'white', fg = 'black')
    showUserName.place(x = 790, y = 600)
    

##################################################################################################################################

def doneData():
    global USERNAME
    global USERNUMBER
    
    #Clearing screen
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Print text set message
    Message = Label(window,width = 60,  background = 'white', text = "Thank you " + USERNAME + ",you will be sent a text message at: ", font=("Comic Sans MS", 20), fg = 'black')
    Message.place(x = 220,y = 460)

    Message2 = Label(window,width = 40,  background = 'white', text = USERNUMBER , font=("Comic Sans MS", 20), fg = 'black')
    Message2.place(x = 395,y = 560)

    x = ovenNotification()

    SMSTestButton = Button(window,text="Send Test SMS",width = 16, background = 'green', fg = 'black', activebackground = 'grey', command = sendTestSMS)
    SMSTestButton.place(x = 650, y = 740)

    homeButton = Button(window,text="Return",width = 16, background = 'green', fg = 'black', activebackground = 'grey', command = mainMenu)
    homeButton.place(x= 650 ,y = 690)

    redoButton = Button(window,text="Redo",width = 16, background = 'green', fg = 'black', activebackground = 'grey', command = textMessageCreator)
    redoButton.place(x = 650, y = 640)

#################################################################################################################################

def textMessageCreator():
    global userName
    global USERNUMBER
    global userNum

    #Clearing screen
    mainScreenCoverup = Label(window,width = 1200, height = 1000, background = 'white')
    mainScreenCoverup.place(x = 0,y = 450)

    main2ScreenCoverup = Label(window,width = 1000, height = 1000, background = 'white')
    main2ScreenCoverup.place(x = 240, y = 500)

    #Username
    userName = Entry(window, background = 'grey')
    userName.place(x  = 790, y = 465)

    enterNameButton = Button(window,text="Enter name",width = 16, background = TEXTMESSAGEBUTTONCOLOUR, fg = 'black', activebackground = 'grey',  command = checkUserName)
    enterNameButton.place(x=650,y=460)

    #User Number
    userNum = Entry(window, background = 'grey')
    userNum.place(x = 790, y = 565)

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

    #Change Units, no command yet, MUST ADD!
    #changeUnitsButton = Button(window,text="Change Units",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH)
    #changeUnitsButton.place(x=650,y=510)

    #Text Message
    textMessageButton = Button(window,text="Text Message",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = textMessageCreator)
    textMessageButton.place(x=650,y=560)

    #Oven
    #mainScreenButton = Button(window,text="Don't click the oven",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = changeMainScreen)
    #mainScreenButton.place(x=650,y=610)

    #Size graph
    graphSizeButton = Button(window,text="Graph size",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = graphScaling) # Change the graphs scale here
    graphSizeButton.place(x=650,y=610)

    #Set COM
    setCOMButton = Button(window,text="Set COMS",width = 16, background = OPTIONSBUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = comSetter)
    setCOMButton.place(x=650,y=510)

    #Go back 
    goBackButton = Button(window,text="Go back",width = 16, background = BUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = mainMenu) 
    goBackButton.place(x=2,y=4)
    
    

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
    goBackButton = Button(window,text="Go back",width = 16, background = BUTTONCOLOUR, fg = 'black',  activebackground = BUTTONCOLOURFLASH, command = introToOven) 
    goBackButton.place(x=2,y=4)
    
    #Credits
    creditsButton = Button(window,text="Credits",width = 16, background = BUTTONCOLOUR, fg = 'black', activebackground = BUTTONCOLOURFLASH, command = credits)
    creditsButton.place(x=650,y=610)



    window.mainloop()

##################################################################################################################################


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

