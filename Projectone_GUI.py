import tkinter
import pygame

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

def Units():
    print("test")

##################################################################################################################################

def changeGraphColour():
    redButton = Button(window,text="Red",width = 16, background = 'grey', fg = 'red')
    redButton.place(x=200,y=300)

    blueButton = Button(window,text="Blue",width = 16, background = 'grey', fg = 'blue')
    blueButton.place(x=200,y=350)

    yellowButton = Button(window,text="Yellow",width = 16, background = 'grey', fg = 'yellow')
    yellowButton.place(x=200,y=400)

    orangeButton = Button(window,text="Orange",width = 16, background = 'grey', fg = 'orange')
    orangeButton.place(x=200,y=450)

    #Go back 2 
    goBackButton2 = Button(window,text="Go back",width = 16, background = 'grey', fg = 'black', command = mainMenu)
    goBackButton2.place(x=200,y=500)

#################################################################################################################################

def textMessageCreator():
    #userTelephone = Entry.get()
    print("test")


################################################################################################################################

def optionsMenu():
    #startButton.pack()
    #optionsButton.pack()
    #printGraphButton.pack()
    
    
    #graph colour
    graphColourButton = Button(window,text="Graph Colour",width = 16, background = 'grey', fg = 'black', command = changeGraphColour)
    graphColourButton.place(x=200,y=300)

    #Change Units
    changeUnitsButton = Button(window,text="Change Units",width = 16, background = 'grey', fg = 'black', command = Units)
    changeUnitsButton.place(x=200,y=350)

    #Text Message
    textMessageButton = Button(window,text="Text Message",width = 16, background = 'grey', fg = 'black', command = textMessageCreator)
    textMessageButton.place(x=200,y=400)

    #Go back 
    goBackButton = Button(window,text="Go back",width = 16, background = 'grey', fg = 'black', command = mainMenu)
    goBackButton.place(x=200,y=450)

################################################################################################################################

def printGraph():
    print("test")


#################################################################################################################################

def mainMenu():
    #Adding gif to the window
    mainImage = PhotoImage(file = "giphy.gif")
    Label(window, image = mainImage, bg = "black") .grid(row = 0, column = 0, sticky = NSEW)

    #startbutton
    startButton = Button(window,text="start",width = 16, background = 'grey', fg = 'black', )
    startButton.place(x=200,y=300)

    #Options button
    optionsButton = Button(window,text="Options",width = 16, background = 'grey', fg = 'black', command = optionsMenu)
    optionsButton.place(x=200,y=350)

    #Print Graph button
    printGraphButton = Button(window,text="Print Graph",width = 16, background = 'grey', fg = 'black', command = printGraph)
    printGraphButton.place(x=200,y=400)

    window.mainloop()

##################################################################################################################################

#Main Program
#Tkinter main menu:
from tkinter import *
#Creating window 
window = Tk()
window.title("Oven Controller")
window.configure(background="Black")
full =FullScreenApp(window)

#Calling functions:
mainmenu = mainMenu()

#Loop the Window
window.mainloop()

