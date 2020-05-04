import RPi.GPIO as GPIO
from gpiozero import MotionSensor

#This sets the infrared sensor to be on the pin 5
irSense = MotionSensor(5)
    
#This will then wait on this line untill motion is detected
irSense.wait_for_motion()
