from sending import sendMessage as send
import RPi.GPIO as GPIO
from gpiozero import MotionSensor


try:
    
    while True:

        who = input("Who do you want to contact?\nKheraass - K, Voltar - V, Bren - B, SpookFeesh - S\n")
        
        if who == "B":
            
            send("Fire")
            
        elif who == "K":
            
            send("Move")
            
        elif who == "V":
            
            song = input("What song do you want to play\n")
            
            send("Play " + song)
            
        elif who == "S":
            
            print("glub")

        
        elif who == "Break":
            
            print(x)
            
        else:
            
            print("Command not recognised. Try again")

except:
    
    print("Exit")