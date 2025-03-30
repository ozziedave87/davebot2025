''' 
Davebot Soft Shutdown Script
Version: 1.1
Author: DK and Legoman
References: https://core-electronics.com.au/guides/how-to-make-a-safe-shutdown-button-for-raspberry-pi/
            Developed with GPT for efficiency and clarity

Description:
This script listens for a button press on GPIO 26 to initiate a soft shutdown 
of the Raspberry Pi. A momentary open button must be held for 5 seconds to trigger shutdown.

## How to Run on Raspberry Pi Startup:
### Option 1: Using systemd (Recommended)
1. Create a systemd service file:
   sudo nano /etc/systemd/system/shutdown-button.service
2. Add the following content:
   [Unit]
   Description=Davebot Shutdown Button Service
   After=multi-user.target

   [Service]
   Type=simple
   ExecStart=/usr/bin/python3 /path/to/shutdown.py
   Restart=always
   User=pi

   [Install]
   WantedBy=multi-user.target
3. Save and exit.
4. Reload systemd:  
   sudo systemctl daemon-reload
5. Enable the service to run on boot:  
   sudo systemctl enable shutdown-button
6. Start the service manually for testing (optional):  
   sudo systemctl start shutdown-button
7. Check service status:  
   sudo systemctl status shutdown-button

To stop the service: sudo systemctl stop shutdown-button

### Option 2: Using crontab (@reboot)
1. Open crontab:  
   crontab -e
2. Add the following line at the bottom:  
   @reboot /usr/bin/python3 /path/to/shutdown.py &
3. Save and exit.
4. Reboot to test:  
   sudo reboot

'''

from gpiozero import Button #import button from the Pi GPIO library
import time # import time functions
import os #imports OS library for Shutdown control

stopButton = Button(26) # defines the button as an object and chooses GPIO 26

while True: #infinite loop
     print('Soft shutdown is running')
     if stopButton.is_pressed: #Check to see if button is pressed
        print('Soft shutdown button has been pressed - hold for 5 seconds')
        time.sleep(5) # wait for the hold time we want. 
        if stopButton.is_pressed: #check if the user let go of the button
            os.system("sudo systemctl poweroff") #shut down the Pi -h is or -r will reset
            print('Legoman is shutting Davebot down now - goodbye')
        time.sleep(1) # wait to loop again so we don’t use the processor too much.