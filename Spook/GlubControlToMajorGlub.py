#import the necessary software

from sending import sendMessage as send
import RPi.GPIO as GPIO
from gpiozero import MotionSensor


#Create loop for selecting other Pi's
try:
    
    while True:
#Ask who the user would like to interact with
        who = input("Who do you want to contact?\nKheraass - K, Voltar - V, Bren - B, SpookFeesh - S\n")
        
#Give options and requirements
        if who == "B":
            
            send("Fire")
            
        elif who == "K":
            
            send("Move")
            
        elif who == "V":
            
            song = input("What song do you want to play\n")
            
            send("Play " + song)
            
        elif who == "S":
            
            print("glub")

#Break command to exit the loop
        
        elif who == "Break":
            
            print(x)
            
        else
#Error output        
            print("Command not recognised. Try again")
except:
    
#Exit dialouge      
    print("Exit")
