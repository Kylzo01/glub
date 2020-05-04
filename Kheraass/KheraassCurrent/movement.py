from sense_hat import SenseHat
sense = SenseHat()
import time


#from adafruit_motorkit import MotorKit   #This line imports the library that interfaces with the adafruit motorkit, because I do not have the motorkit, this line causes errors, in the library file, because it cannot detect the motorkit connected

#motor = MotorKit()

#This code is intended to be used with a motor control board, due to the current situation I was unable to aquire the relevant hardware
#Therefore the code as it stands uses print statements to simulate motor output




#The motor unit that I have coded for using is the Adafruit DC and stepper hat: https://www.adafruit.com/product/2348
#This board would allow an extra 2 motors to be used, however to save on cost and code complexity
#I elected to use only 2. with motor1 being on the left side of the unit and motor 2 being on the right side
def getDirection(): #function intended to return the current orientation of the pi for use in determining direction
    orientation = sense.get_orientation_degrees()
    Direction = round(orientation["yaw"],0)
    return Direction;
    


def move():
    
    pathFile = open("./path/path.txt", "r")
    for line in pathFile:
        input = line
        #print (input)
        fullComm = input.split('~')
        #print (fullComm)
        command = fullComm[0]
        value = fullComm[1]
        #print ("Value " + value)
        value = int(value)
   
        if command == "fore":
            #kit.motor1.throttle = 0.5
            #kit.motor2.throttle = 0.5
            print ("forwards")
            time.sleep(value)
            #kit.motor1.throttle = 0
            #kit.motor2.throttle = 0
            print ("Stop forwards")
        elif command == "back":
            #kit.motor1.throttle = -0.5
            #kit.motor1.throttle = -0.5
            print ("Backwards")
            time.sleep(value)
            #kit.motor1.throttle = 0
            #kit.motor2.throttle = 0
            print ("Stop Backwards")
        elif command == "cw":
            initDirection = getDirection();
            direction = initDirection
            if (initDirection + value) > 360:
                temp = (initDirection + value) - 360
                targetDirection = 0 + temp
                print ("turn Clockwise target direction = " + str(targetDirection) )
                
                while (direction < targetDirection):
                    #kit.motor1.throttle = 0.1
                    #kit.motor2.throttle = -0.1
                    direction = getDirection();
                    print(direction)
                #kit.motor1.throttle = 0
                #kit.motor1.throttle = 0
                print ("Stop clockwise")
            else:
                targetDirection = initDirection + value
                print ("turn Clockwise target direction = " + str(targetDirection) )
                while(direction < targetDirection):
                    #kit.motor1.throttle = 0.1
                    #kit.motor2.throttle = -0.1
                    
                    direction = getDirection();
                    print(direction)
                #kit.motor1.throttle = 0
                #kit.motor2.throttle = 0
                print ("Stop clockwise")
  
        elif command == "ccw":
           
            initDirection = getDirection();
            if (initDirection - value) < 0:
                temp = abs(initDirection - value)
                targetDirection = 360 - temp
                print ("Turn counterclockwise")
                while (direction > targetDirection):
                    #kit.motor1.throttle = -0.1
                    #kit.motor2.throttle = 0.1
                    direction = getDirection();
                    print(direction)
                #kit.motor1.throttle = 0
                #kit.motor1.throttle = 0
                print ("Stop counterclockwise")
            else:
                targetDirection = initDirection - value
                print ("print counterclockwise")
                while (direction != targetDirection):
                    #kit.motor1.throttle = -0.1
                    #kit.motor2.throttle = 0.1
                    direction = getDirection();
                    print(direction)
                #kit.motor1.throttle = 0
                #kit.motor1.throttle = 0
                print ("Stop counterclockwise")
    print ("Path done")
    
            
            
 
        
            
        
  
    



    

