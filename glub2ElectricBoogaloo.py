from sense_hat import SenseHat
sense = SenseHat()
from sending import sendMessage as send

from time import sleep

def contact(direction):
        
    if direction == "left":
        
        sense.show_message("Contacting Bren")
        send("Fire")
        
        
    elif direction == "right":
        
        sense.show_message("Contacting Kheraass")
        
        send("Move")
        
    elif direction == "up":
        
        sense.show_message("Contacting Voltar")
        
        song = input("What sont do you want voltar to \"play\"?\n")
        send("Play " + song)
        
    
    elif direction == "down":
        
        sense.show_message("Glub")
        
        sleep(5)
                        
    sense.clear((0, 0, 0))


sense.clear((0, 0, 0))


while True:
    
    for event in sense.stick.get_events():
        
        
        if event.action == "released":
                        
            dir = event.direction
            
            contact(dir)
