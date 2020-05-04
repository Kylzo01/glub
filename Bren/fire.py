import RPi.GPIO as GPIO
from gpiozero import MotionSensor
from sense_hat import SenseHat
import time
#import publish

def startWatch():
    
    #This sets the infrared sensor to be on the pin 5
    irSense = MotionSensor(5)
    
    #This will then wait on this line untill motion is detected
    irSense.wait_for_motion()
    
    shootWithServo()

    #publish.connectUp()
    #publish.sendMessage("Target Down")
    #publish.finishedPublishing()
    


#With Trial it is possible this might not work due to there not being
#enough force to pull on the trigger but it is not possible to know
#this in the current situation
def shootWithServo():
    
    #This sets the numbering system on the GPIO board
    GPIO.setmode(GPIO.BOARD)

    #This sets pin 11 to be the output (the one that the servo would 
    #have been hooked up to
    GPIO.setup(11,GPIO.OUT)
    
    #Create variable for the servo that states that it's on pin 11
    #with a 75Hz pulse
    servo = GPIO.PWM(11,75)
    
    #Starts the servo but doesn't set it to move
    servo.start(0)
    
    
    
    #This will loop 20 times and will turn the servo back and forth to
    #Pull the trigger
    
    for i in range(20):
        
        #This is the position that the servo arm will be at, 2 is 0 degrees
        pos = 2
    
        #This sets the position of the servo arm
        servo.ChangeDutyCycle(pos)
        
        #Wait half a second to ensure the servo has the time to turn
        sleep(0.5)
        
        #This is the position that the servo arm will be at, 2 is 0 degrees
        pos = 8
    
        #This sets the position of the servo arm
        servo.ChangeDutyCycle(pos)
        
        sleep(0.5)
        
    #Reset The Servo
    servo.ChangeDutyCycle(2)
    
    
    
    
def simulatedWatch():
    
    movement = input("Has there been movement?(y/n):\n")
    
    
    while movement != "y":
    
        movement = input("Has there been movement?(y/n)\n")
    
    
    
    #This then "shoots" at the found target
    shootWithSenseHat()

    #This then sends another messagfe to the client and then closes the link
   # publish.sendMessage("Target Down")
   # publish.finishedPublishing()
    
   # print("done sending")
                
        
#This simulates the nerf gun shooting with a sense hat saying pew pew
def shootWithSenseHat():

    sense = SenseHat()
        
    sense.show_message("Pew Pew")


#shootWithSenseHat()


