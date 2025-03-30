from gpiozero import Button #import button from the Pi GPIO library
import time # import time functions
import os #imports OS library for Shutdown control

stopButton = Button(26) # defines the button as an object and chooses GPIO 26

while True: #infinite loop
     if stopButton.is_pressed: #Check to see if button is pressed
        print('Soft shutdown button has been pressed - hold for 5 seconds')
        time.sleep(5) # wait for the hold time we want. 
        if stopButton.is_pressed: #check if the user let go of the button
            #os.system("sudo systemctl poweroff") #shut down the Pi -h is or -r will reset
            print('Legoman is shutting Davebot down now - goodbye')
        time.sleep(1) # wait to loop again so we don’t use the processor too much.