import serial
#Opening the port
arduinoSerial = serial.Serial(port ='COM10')
arduinoSerial.isOpen()
        
while 1:
    arduinoOutput = arduinoSerial.readline()
    displayNumber = arduinoOutput.decode("utf-8").replace("\r\n", "\n")
    displayNumber = int(displayNumber)
    print(displayNumber)