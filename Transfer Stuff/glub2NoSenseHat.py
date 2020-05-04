from sending import sendMessage as send


try:
    
    while True:

        who = input("Who do you want to contact?\nKheraass - K, Voltar - V, Bren B\n")
        
        if who == "B":
            
            send("Fire")
            
        elif who == "K":
            
            send("Move")
            
        elif who == "V":
            
            song = input("What song do you want to play\n")
            
            send("Play " + song)
        
        elif who == "Break":
            
            print(x)
            
        else:
            
            print("Command not recognised. Try again")

except:
    
    print("Exit")
