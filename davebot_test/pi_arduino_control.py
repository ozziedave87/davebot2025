# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Configure the joystick
# pygame.joystick.init()
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600)  # Update the port to /dev/ttyACM0

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Read the X-axis and Y-axis of the left joystick
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)

#         # Send the joystick values to the Arduino via serial
#         message = f"{scaled_left_x},{scaled_left_y}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y}")

#         sleep(0.05)  # Add a small delay to avoid CPU overload

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Check if joystick is detected
# joystick_count = pygame.joystick.get_count()
# print(f"Number of joysticks detected: {joystick_count}")
# if joystick_count == 0:
#     print("No joystick detected!")
#     pygame.quit()
#     exit()

# # Configure the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600)  # Update the port to /dev/ttyACM0

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Connection is working" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 # If there's an error decoding, print the raw bytes and continue
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Read the X-axis and Y-axis of the left joystick
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Print raw axis values to check if they are being updated
#         print(f"Raw Left Joystick - X: {left_x_axis}, Y: {left_y_axis}")

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)

#         # Send the joystick values to the Arduino via serial
#         message = f"{scaled_left_x},{scaled_left_y}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y}")

#         sleep(0.05)  # Add a small delay to avoid CPU overload

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################

# Davebot forward and back is successful

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     while True:
#         pygame.event.pump()  # Process joystick events
        
#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Exiting program.")
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         if abs(right_x_axis) < DEADZONE:
#             right_x_axis = 0
#         if abs(right_y_axis) < DEADZONE:
#             right_y_axis = 0

#         # Add fire control on button 7
#         button_7_pressed = joystick.get_button(7)

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             scaled_left_x = scaled_left_y  # Both motors move forward
#         elif scaled_left_y < 0:  # Backward
#             scaled_left_x = scaled_left_y  # Both motors move backward
#         else:
#             scaled_left_x = 0  # Stop both motors if no movement

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{scaled_left_x},{scaled_left_y}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 7 status only when it is pressed
#         if button_7_pressed:
#             print("Button 7 is pressed - fire")

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.01)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()


##########################################################################################################
##########################################################################################################
##########################################################################################################

#davebot x and y appear to be working for differential drive

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     while True:
#         pygame.event.pump()  # Process joystick events
        
#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Exiting program.")
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         if abs(right_x_axis) < DEADZONE:
#             right_x_axis = 0
#         if abs(right_y_axis) < DEADZONE:
#             right_y_axis = 0

#         # Add fire control on button 7
#         button_7_pressed = joystick.get_button(7)

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis)
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(100, motor1_speed + scaled_left_x)  # Motor 1 faster
#             motor2_speed = max(-100, motor2_speed - scaled_left_x)  # Motor 2 slower
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(-100, motor1_speed + scaled_left_x)  # Motor 1 slower
#             motor2_speed = min(100, motor2_speed - scaled_left_x)  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 7 status only when it is pressed
#         if button_7_pressed:
#             print("Button 7 is pressed - fire")

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.01)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################

#Davebot differential drive is working and button 0 (A) is now a keyboard interrupt/remote E-stop

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     while True:
#         pygame.event.pump()  # Process joystick events
        
#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Exiting program.")
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         if abs(right_x_axis) < DEADZONE:
#             right_x_axis = 0
#         if abs(right_y_axis) < DEADZONE:
#             right_y_axis = 0

#         # Add fire control on button 7
#         button_7_pressed = joystick.get_button(7)

#         # Check if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             print("Button 0 pressed - Exiting program.")
#             pygame.quit()
#             exit()

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis)
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(100, motor1_speed + scaled_left_x)  # Motor 1 faster
#             motor2_speed = max(-100, motor2_speed - scaled_left_x)  # Motor 2 slower
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(-100, motor1_speed + scaled_left_x)  # Motor 1 slower
#             motor2_speed = min(100, motor2_speed - scaled_left_x)  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 7 status only when it is pressed
#         if button_7_pressed:
#             print("Button 7 is pressed - fire")

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.01)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()


##########################################################################################################
##########################################################################################################
##########################################################################################################

# #Deadman switch works - however motors continue at last known velocity when E-stop or deadman switch are used

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     while True:
#         pygame.event.pump()  # Process joystick events
        
#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Exiting program.")
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         if abs(right_x_axis) < DEADZONE:
#             right_x_axis = 0
#         if abs(right_y_axis) < DEADZONE:
#             right_y_axis = 0

#         # Add fire control on button 7
#         button_7_pressed = joystick.get_button(7)

#         # Check if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             print("Button 0 pressed - Exiting program.")
#             pygame.quit()
#             exit()

#         # Check if button 6 is pressed (allow joystick input)
#         button_9_pressed = joystick.get_button(9)

#         if not button_9_pressed:
#             print("Please hold down button 9 to control the motors.")
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop and ask the user to hold down button 6

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis)
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(100, motor1_speed + scaled_left_x)  # Motor 1 faster
#             motor2_speed = max(-100, motor2_speed - scaled_left_x)  # Motor 2 slower
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(-100, motor1_speed + scaled_left_x)  # Motor 1 slower
#             motor2_speed = min(100, motor2_speed - scaled_left_x)  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 7 status only when it is pressed
#         if button_7_pressed:
#             print("Button 7 is pressed - fire")

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.01)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()
##########################################################################################################
##########################################################################################################
##########################################################################################################

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     return int(value * 100)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     while True:
#         pygame.event.pump()  # Process joystick events
        
#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Exiting program.")
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         if abs(right_x_axis) < DEADZONE:
#             right_x_axis = 0
#         if abs(right_y_axis) < DEADZONE:
#             right_y_axis = 0

#         # Add fire control on button 7
#         button_7_pressed = joystick.get_button(7)

#         # Remote E-stop - check if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             print("Button 0 pressed - Exiting program.")
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             pygame.quit()
#             exit()

#         # Check if button 6 is pressed (allow joystick input)
#         button_9_pressed = joystick.get_button(9)

#         if not button_9_pressed:
#             print("Please hold down button 9 to control the motors.")
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop and ask the user to hold down button 6

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis)
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(100, motor1_speed + scaled_left_x)  # Motor 1 faster
#             motor2_speed = max(-100, motor2_speed - scaled_left_x)  # Motor 2 slower
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(-100, motor1_speed + scaled_left_x)  # Motor 1 slower
#             motor2_speed = min(100, motor2_speed - scaled_left_x)  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 7 status only when it is pressed
#         if button_7_pressed:
#             print("Button 7 is pressed - fire")

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.01)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################

# #davebot update turn logic and increase the scale to 250 instead of 100
# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# #Global variables 
# #Button numbers for deadman and fire are LB and RB however this does change sometimes; either 6 & 7 or 9 & 10
# deadman = 6
# fire = 7

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -250 to +250
# def map_axis_to_range(value):
#     return int(value * 250)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")
    
#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()
                
#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError as e:
#                 print(f"Error decoding message: {e}. Raw data: {raw_data}")
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     while True:
#         pygame.event.pump()  # Process joystick events
        
#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Exiting program.")
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         if abs(right_x_axis) < DEADZONE:
#             right_x_axis = 0
#         if abs(right_y_axis) < DEADZONE:
#             right_y_axis = 0

#         # Add fire control on button fire
#         button_fire_pressed = joystick.get_button(fire)

#         # Remote E-stop - check if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             print("Button 0 pressed - Exiting program.")
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             pygame.quit()
#             exit()

#         # Check if button deadman_button is pressed (allow joystick input)
#         button_deadman_pressed = joystick.get_button(deadman)

#         if not button_deadman_pressed:
#             print("Please hold down button deadman_button to control the motors.")
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop and ask the user to hold down button 9

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis)
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(250, motor1_speed + scaled_left_x)  # Motor 1 faster
#             motor2_speed = max(0, motor2_speed - scaled_left_x)  # Motor 2 slower (not going negative)
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(0, motor1_speed + scaled_left_x)  # Motor 1 slower (not going negative)
#             motor2_speed = min(250, motor2_speed - scaled_left_x)  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 10 status only when it is pressed
#         if button_fire_pressed:
#             print("Button pressed - fire")

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.01)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################
# Title: Joystick-Controlled Robot Motor Driver
# Author: Davebot
# Developed in conjunction with ChatGPT
#
# Description:
# This script interfaces a joystick with a robot via an Arduino. It reads joystick inputs to control the robot's differential drive motors (forward, backward, and turning). The joystick axes are mapped to motor speeds, and the script includes a deadman switch for safety (button press required to enable motor control). An emergency stop button (button 0) halts motor operation. The script communicates with the Arduino via serial to send motor speed commands and receive feedback.
#
# Change Log:
# 1.0 - Initial version, developed with ChatGPT
# 1.1 - Added deadman switch functionality
# 1.2 - Integrated emergency stop (button 0)
# 1.3 - Introduced deadzone filtering for joystick inputs
# 1.4 - Adjusted joystick axis mapping to improve responsiveness
# 1.5 - Optimized communication with Arduino (timeout and buffer clearing)

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Global variables 
# deadman = 6 # Button numbers for deadman; either 6 or 9

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -250 to +250
# def map_axis_to_range(value):
#     return int(value * 250)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")

#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()

#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError:
#                 pass
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     deadman_message_shown = False

#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # # Read the X-axis and Y-axis of the right joystick for use with turret
#         # right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         # right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0
#         # if abs(right_x_axis) < DEADZONE:
#         #     right_x_axis = 0
#         # if abs(right_y_axis) < DEADZONE:
#         #     right_y_axis = 0

#         # Remote E-stop - if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             print("Emergency E stop has been pressed - program has been ended.") 
#             pygame.quit()
#             exit()

#         # Check if button deadman_button is pressed (allow joystick input)
#         button_deadman_pressed = joystick.get_button(deadman)

#         if not button_deadman_pressed:
#             if not deadman_message_shown:
#                 print("Please hold down button deadman_button to control the motors.")
#                 deadman_message_shown = True
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop and ask the user to hold down button 9
#         else:
#             deadman_message_shown = False

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         # scaled_right_x = map_axis_to_range(right_x_axis)
#         # scaled_right_y = map_axis_to_range(right_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis)
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(250, motor1_speed + scaled_left_x)  # Motor 1 faster
#             motor2_speed = max(0, motor2_speed - scaled_left_x)  # Motor 2 slower (not going negative)
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(0, motor1_speed + scaled_left_x)  # Motor 1 slower (not going negative)
#             motor2_speed = min(250, motor2_speed - scaled_left_x)  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.05)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################
# Title: Joystick-Controlled Robot Motor Driver
# Author: Davebot
# Developed in conjunction with ChatGPT
#
# Description:
# This script interfaces a joystick with a robot via an Arduino. It reads joystick inputs to control the robot's differential drive motors (forward, backward, and turning). The joystick axes are mapped to motor speeds, and the script includes a deadman switch for safety (button press required to enable motor control). An emergency stop button (button 0) halts motor operation. The script communicates with the Arduino via serial to send motor speed commands and receive feedback.
#
# Change Log:
# 1.0 - Initial version, developed with ChatGPT
# 1.1 - Added deadman switch functionality
# 1.2 - Integrated emergency stop (button 0)
# 1.3 - Introduced deadzone filtering for joystick inputs
# 1.4 - Adjusted joystick axis mapping to improve responsiveness
# 1.5 - Optimized communication with Arduino (timeout and buffer clearing)
# 1.6 - Implemented speed-based steering sensitivity adjustment with configurable speed ranges and sensitivity levels.

# import pygame
# import serial
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Global variables for speed ranges and sensitivity levels
# LOW_SPEED_MAX = 70
# MID_SPEED_MIN = LOW_SPEED_MAX+1
# MID_SPEED_MAX = 140
# HIGH_SPEED_MIN = MID_SPEED_MAX+1
# HIGH_SPEED_MAX = 250

# STEERING_SENSITIVITY_LOW = 0.6  # 40% reduction in sensitivity at low speed
# STEERING_SENSITIVITY_MID = 0.5  # 50% reduction in sensitivity at mid speed
# STEERING_SENSITIVITY_HIGH = 0.2  # 80% reduction in sensitivity at high speed

# # Deadman button number (either 6 or 9)
# deadman = 6

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -250 to +250
# def map_axis_to_range(value):
#     return int(value * 250)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# # Function to adjust steering sensitivity based on speed
# def adjust_steering_sensitivity(speed):
#     if speed <= LOW_SPEED_MAX:
#         return STEERING_SENSITIVITY_LOW
#     elif MID_SPEED_MIN <= speed <= MID_SPEED_MAX:
#         return STEERING_SENSITIVITY_MID
#     elif HIGH_SPEED_MIN <= speed <= HIGH_SPEED_MAX:
#         return STEERING_SENSITIVITY_HIGH
#     return 1.0  # Default sensitivity (shouldn't reach here)

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")

#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()

#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError:
#                 pass
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     deadman_message_shown = False

#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Check for quit event
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0

#         # Remote E-stop - if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             print("Emergency E stop has been pressed - program has been ended.") 
#             pygame.quit()
#             exit()

#         # Check if button deadman_button is pressed (allow joystick input)
#         button_deadman_pressed = joystick.get_button(deadman)

#         if not button_deadman_pressed:
#             if not deadman_message_shown:
#                 print("Please hold down button deadman_button to control the motors.")
#                 deadman_message_shown = True
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command to Arduino
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop and ask the user to hold down button 9
#         else:
#             deadman_message_shown = False

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Adjust steering sensitivity based on Y-axis speed (forward/backward)
#         steering_sensitivity = adjust_steering_sensitivity(abs(scaled_left_y))

#         # Control logic for forward and backward movement (Y-axis)
#         if scaled_left_y > 0:  # Forward
#             motor1_speed = scaled_left_y  # Both motors move forward
#             motor2_speed = scaled_left_y
#         elif scaled_left_y < 0:  # Backward
#             motor1_speed = scaled_left_y  # Both motors move backward
#             motor2_speed = scaled_left_y
#         else:
#             motor1_speed = 0  # Stop both motors if no movement
#             motor2_speed = 0

#         # Control logic for left-right movement (X-axis) with adjusted steering sensitivity
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(250, motor1_speed + int(scaled_left_x * steering_sensitivity))  # Motor 1 faster
#             motor2_speed = max(0, motor2_speed - int(scaled_left_x * steering_sensitivity))  # Motor 2 slower (not going negative)
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(0, motor1_speed + int(scaled_left_x * steering_sensitivity))  # Motor 1 slower (not going negative)
#             motor2_speed = min(250, motor2_speed - int(scaled_left_x * steering_sensitivity))  # Motor 2 faster
#         else:  # X-axis neutral: Both motors at the same speed
#             motor1_speed = motor2_speed

#         # Send the joystick values to the Arduino via serial (for robot control)
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.05)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################
# Title: Joystick-Controlled Robot Motor Driver
# Author: Davebot
# Developed in conjunction with ChatGPT
#
# Description:
# This script interfaces a joystick with a robot via an Arduino. It reads joystick inputs to control the robot's differential drive motors (forward, backward, and turning). The joystick axes are mapped to motor speeds, and the script includes a deadman switch for safety (button press required to enable motor control). An emergency stop button (button 0) halts motor operation. The script communicates with the Arduino via serial to send motor speed commands and receive feedback.
#
# Change Log:
# 1.0 - Initial version, developed with ChatGPT
# 1.1 - Added deadman switch functionality
# 1.2 - Integrated emergency stop (button 0)
# 1.3 - Introduced deadzone filtering for joystick inputs
# 1.4 - Adjusted joystick axis mapping to improve responsiveness
# 1.5 - Optimized communication with Arduino (timeout and buffer clearing)
# 1.6 - Implemented speed-based steering sensitivity adjustment with configurable speed ranges and sensitivity levels
# 1.7 - Added safety feature to stop motors if joystick disconnects for more than 3 seconds

# import pygame
# import serial
# from time import sleep, time

# # Initialize pygame
# pygame.init()

# # Global variables for speed ranges and sensitivity levels
# LOW_SPEED_MAX = 70
# MID_SPEED_MIN = LOW_SPEED_MAX + 1
# MID_SPEED_MAX = 140
# HIGH_SPEED_MIN = MID_SPEED_MAX + 1
# HIGH_SPEED_MAX = 250

# STEERING_SENSITIVITY_LOW = 0.6  # 40% reduction in sensitivity at low speed
# STEERING_SENSITIVITY_MID = 0.5  # 50% reduction in sensitivity at mid speed
# STEERING_SENSITIVITY_HIGH = 0.2  # 80% reduction in sensitivity at high speed

# # Deadman button number (either 6 or 9)
# deadman = 6

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -250 to +250
# def map_axis_to_range(value):
#     return int(value * 250)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# # Function to adjust steering sensitivity based on speed
# def adjust_steering_sensitivity(speed):
#     if speed <= LOW_SPEED_MAX:
#         return STEERING_SENSITIVITY_LOW
#     elif MID_SPEED_MIN <= speed <= MID_SPEED_MAX:
#         return STEERING_SENSITIVITY_MID
#     elif HIGH_SPEED_MIN <= speed <= HIGH_SPEED_MAX:
#         return STEERING_SENSITIVITY_HIGH
#     return 1.0  # Default sensitivity (shouldn't reach here)

# # Initialize a timer for joystick disconnection
# last_joystick_event_time = time()

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")

#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()

#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError:
#                 pass
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     deadman_message_shown = False

#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Check joystick connection
#         try:
#             left_x_axis = joystick.get_axis(0)  # Attempt to read joystick input
#             last_joystick_event_time = time()  # Update the last event time
#         except pygame.error:
#             current_time = time()
#             if current_time - last_joystick_event_time > 3:  # 3-second timeout
#                 motor1_speed = 0
#                 motor2_speed = 0
#                 arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
#                 print("Joystick disconnected for more than 3 seconds. Motors stopped.")
#             continue  # Skip the rest of the loop until joystick reconnects

#         # Read the Y-axis of the left joystick to control differential robot drive
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0

#         # Remote E-stop - if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
#             print("Emergency E-stop has been pressed - program ended.")
#             pygame.quit()
#             exit()

#         # Check if button deadman is pressed (allow joystick input)
#         button_deadman_pressed = joystick.get_button(deadman)

#         if not button_deadman_pressed:
#             if not deadman_message_shown:
#                 print("Please hold down the deadman button to control the motors.")
#                 deadman_message_shown = True
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop
#         else:
#             deadman_message_shown = False

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Adjust steering sensitivity based on Y-axis speed (forward/backward)
#         steering_sensitivity = adjust_steering_sensitivity(abs(scaled_left_y))

#         # Control logic for forward and backward movement (Y-axis)
#         motor1_speed = scaled_left_y
#         motor2_speed = scaled_left_y

#         # Control logic for left-right movement (X-axis) with adjusted steering sensitivity
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(250, motor1_speed + int(scaled_left_x * steering_sensitivity))
#             motor2_speed = max(0, motor2_speed - int(scaled_left_x * steering_sensitivity))
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(0, motor1_speed + int(scaled_left_x * steering_sensitivity))
#             motor2_speed = min(250, motor2_speed - int(scaled_left_x * steering_sensitivity))

#         # Send the joystick values to the Arduino via serial
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.05)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################
# Title: Joystick-Controlled Robot Motor Driver
# Author: Davebot
# Developed in conjunction with ChatGPT
#
# Description:
# This script interfaces a joystick with a robot via an Arduino. It reads joystick inputs to control the robot's differential drive motors (forward, backward, and turning). The joystick axes are mapped to motor speeds, and the script includes a deadman switch for safety (button press required to enable motor control). An emergency stop button (button 0) halts motor operation. The script communicates with the Arduino via serial to send motor speed commands and receive feedback.
#
# Change Log:
# 1.0 - Initial version, developed with ChatGPT
# 1.1 - Added deadman switch functionality
# 1.2 - Integrated emergency stop (button 0)
# 1.3 - Introduced deadzone filtering for joystick inputs
# 1.4 - Adjusted joystick axis mapping to improve responsiveness
# 1.5 - Optimized communication with Arduino (timeout and buffer clearing)
# 1.6 - Implemented speed-based steering sensitivity adjustment with configurable speed ranges and sensitivity levels
# 1.7 - Added safety feature to stop motors if joystick disconnects for more than 3 seconds

# import pygame
# import serial
# from time import sleep, time

# # Initialize pygame
# pygame.init()

# # Global variables for speed ranges and sensitivity levels
# LOW_SPEED_MAX = 70
# MID_SPEED_MIN = LOW_SPEED_MAX + 1
# MID_SPEED_MAX = 140
# HIGH_SPEED_MIN = MID_SPEED_MAX + 1
# HIGH_SPEED_MAX = 250

# STEERING_SENSITIVITY_LOW = 0.6  # 40% reduction in sensitivity at low speed
# STEERING_SENSITIVITY_MID = 0.5  # 50% reduction in sensitivity at mid speed
# STEERING_SENSITIVITY_HIGH = 0.2  # 80% reduction in sensitivity at high speed

# # Bluetooth timeout and toggle
# BLUETOOTH_TIMEOUT = 1  # Seconds for the joystick to be considered out of range
# BLUETOOTH_SAFETY = True  # Enable/disable the Bluetooth out-of-range feature

# # Deadman button number (either 6 or 9)
# DEADMAN = 6

# # Check the number of joysticks connected
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize the joystick
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Initialize serial communication with Arduino
# arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# # Function to map joystick axis to a range of -250 to +250
# def map_axis_to_range(value):
#     return int(value * 250)

# # Threshold for joystick movement (minimum value before motor operates)
# THRESHOLD = 10
# DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# # Function to adjust steering sensitivity based on speed
# def adjust_steering_sensitivity(speed):
#     if speed <= LOW_SPEED_MAX:
#         return STEERING_SENSITIVITY_LOW
#     elif MID_SPEED_MIN <= speed <= MID_SPEED_MAX:
#         return STEERING_SENSITIVITY_MID
#     elif HIGH_SPEED_MIN <= speed <= HIGH_SPEED_MAX:
#         return STEERING_SENSITIVITY_HIGH
#     return 1.0  # Default sensitivity (shouldn't reach here)

# # Initialize a timer for joystick disconnection
# last_joystick_event_time = time()

# try:
#     print("Controller Ready. Use the joysticks to control the motors.")

#     # Wait for the Arduino to send the initial connection message
#     while True:
#         if arduino.in_waiting > 0:
#             try:
#                 # Read and decode the message, ignore errors and handle non-UTF-8 bytes
#                 raw_data = arduino.readline()
#                 message = raw_data.decode('utf-8', errors='ignore').strip()

#                 if "Arduino is connected and ready" in message:
#                     print("Arduino: " + message)
#                     break
#             except UnicodeDecodeError:
#                 pass
#         sleep(0.1)  # Wait a bit before checking again

#     print("Starting joystick processing loop...")
#     deadman_message_shown = False

#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Check joystick connection
#         try:
#             left_x_axis = joystick.get_axis(0)  # Attempt to read joystick input
#             last_joystick_event_time = time()  # Update the last event time
#         except pygame.error:
#             current_time = time()
#             if BLUETOOTH_SAFETY and current_time - last_joystick_event_time > BLUETOOTH_TIMEOUT:  # Check timeout
#                 motor1_speed = 0
#                 motor2_speed = 0
#                 arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
#                 print("Joystick disconnected for more than 1 second(s). Motors stopped.")
#             continue  # Skip the rest of the loop until joystick reconnects

#         # Read the Y-axis of the left joystick to control differential robot drive
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Apply deadzone to joystick inputs
#         if abs(left_x_axis) < DEADZONE:
#             left_x_axis = 0
#         if abs(left_y_axis) < DEADZONE:
#             left_y_axis = 0

#         # Remote E-stop - if button 0 is pressed (exit the program)
#         button_0_pressed = joystick.get_button(0)
#         if button_0_pressed:
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
#             print("Emergency E-stop has been pressed - program ended.")
#             pygame.quit()
#             exit()

#         # Check if button deadman is pressed (allow joystick input)
#         button_deadman_pressed = joystick.get_button(DEADMAN)

#         if not button_deadman_pressed:
#             if not deadman_message_shown:
#                 print("Please hold down the deadman button to control the motors.")
#                 deadman_message_shown = True
#             motor1_speed = 0
#             motor2_speed = 0
#             arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
#             sleep(0.5)  # Delay to prevent spamming the message
#             continue  # Skip the rest of the loop
#         else:
#             deadman_message_shown = False

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)

#         # Apply threshold to ensure no motor operates unless joystick is moved enough
#         if abs(scaled_left_x) < THRESHOLD:
#             scaled_left_x = 0
#         if abs(scaled_left_y) < THRESHOLD:
#             scaled_left_y = 0

#         # Adjust steering sensitivity based on Y-axis speed (forward/backward)
#         steering_sensitivity = adjust_steering_sensitivity(abs(scaled_left_y))

#         # Control logic for forward and backward movement (Y-axis)
#         motor1_speed = scaled_left_y
#         motor2_speed = scaled_left_y

#         # Control logic for left-right movement (X-axis) with adjusted steering sensitivity
#         if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
#             motor1_speed = min(250, motor1_speed + int(scaled_left_x * steering_sensitivity))
#             motor2_speed = max(0, motor2_speed - int(scaled_left_x * steering_sensitivity))
#         elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
#             motor1_speed = max(0, motor1_speed + int(scaled_left_x * steering_sensitivity))
#             motor2_speed = min(250, motor2_speed - int(scaled_left_x * steering_sensitivity))

#         # Send the joystick values to the Arduino via serial
#         message = f"{motor1_speed},{motor2_speed}\n"
#         arduino.write(message.encode())  # Send data as bytes

#         # Read Arduino response and clear buffer if necessary
#         if arduino.in_waiting > 0:
#             arduino.readline()  # Clear any old data from the buffer

#         sleep(0.05)  # Shorten sleep time to reduce lag

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()
#     arduino.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################
# Title: Joystick-Controlled Robot Motor Driver
# Author: Davebot
# Developed in conjunction with ChatGPT
#
# Description:
# This script interfaces a joystick with a robot via an Arduino. It reads joystick inputs to control the robot's differential drive motors (forward, backward, and turning). The joystick axes are mapped to motor speeds, and the script includes a deadman switch for safety (button press required to enable motor control). An emergency stop button (button 0) halts motor operation. The script communicates with the Arduino via serial to send motor speed commands and receive feedback.
#
# Change Log:
# 1.0 - Initial version, developed with ChatGPT
# 1.1 - Added deadman switch functionality
# 1.2 - Integrated emergency stop (button 0)
# 1.3 - Introduced deadzone filtering for joystick inputs
# 1.4 - Adjusted joystick axis mapping to improve responsiveness
# 1.5 - Optimized communication with Arduino (timeout and buffer clearing)
# 1.6 - Implemented speed-based steering sensitivity adjustment with configurable speed ranges and sensitivity levels
# 1.7 - Added safety feature to stop motors if joystick disconnects for more than 3 seconds

import pygame
import serial
from time import sleep, time

# Initialize pygame
pygame.init()

# Global variables for speed ranges and sensitivity levels
LOW_SPEED_MAX = 70
MID_SPEED_MIN = LOW_SPEED_MAX + 1
MID_SPEED_MAX = 140
HIGH_SPEED_MIN = MID_SPEED_MAX + 1
HIGH_SPEED_MAX = 250

STEERING_SENSITIVITY_LOW = 0.6  # 40% reduction in sensitivity at low speed
STEERING_SENSITIVITY_MID = 0.5  # 50% reduction in sensitivity at mid speed
STEERING_SENSITIVITY_HIGH = 0.2  # 80% reduction in sensitivity at high speed

# Bluetooth timeout and toggle
BLUETOOTH_TIMEOUT = 1  # Seconds for the joystick to be considered out of range
BLUETOOTH_SAFETY = True  # Enable/disable the Bluetooth out-of-range feature

# Deadman button number (either 6 or 9)
DEADMAN = 6

# Check the number of joysticks connected
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick detected.")
    pygame.quit()
    exit()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
joystick.init()
print(f"Joystick detected: {joystick.get_name()}")

# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/ttyACM0', 57600, timeout=1)  # Add timeout to prevent freezing

# Function to map joystick axis to a range of -250 to +250
def map_axis_to_range(value):
    return int(value * 250)

# Threshold for joystick movement (minimum value before motor operates)
THRESHOLD = 10
DEADZONE = 0.1  # Deadzone to avoid small movements being detected

# Function to adjust steering sensitivity based on speed
def adjust_steering_sensitivity(speed):
    if speed <= LOW_SPEED_MAX:
        return STEERING_SENSITIVITY_LOW
    elif MID_SPEED_MIN <= speed <= MID_SPEED_MAX:
        return STEERING_SENSITIVITY_MID
    elif HIGH_SPEED_MIN <= speed <= HIGH_SPEED_MAX:
        return STEERING_SENSITIVITY_HIGH
    return 1.0  # Default sensitivity (shouldn't reach here)

# Initialize a timer for joystick disconnection
last_joystick_event_time = time()

try:
    print("Controller Ready. Use the joysticks to control the motors.")

    # Wait for the Arduino to send the initial connection message
    while True:
        if arduino.in_waiting > 0:
            try:
                # Read and decode the message, ignore errors and handle non-UTF-8 bytes
                raw_data = arduino.readline()
                message = raw_data.decode('utf-8', errors='ignore').strip()

                if "Arduino is connected and ready" in message:
                    print("Arduino: " + message)
                    break
            except UnicodeDecodeError:
                pass
        sleep(0.1)  # Wait a bit before checking again

    print("Starting joystick processing loop...")
    deadman_message_shown = False

    while True:
        pygame.event.pump()  # Process joystick events

        # Check joystick connection
        try:
            left_x_axis = joystick.get_axis(0)  # Attempt to read joystick input
            last_joystick_event_time = time()  # Update the last event time
        except pygame.error:
            current_time = time()
            if BLUETOOTH_SAFETY and current_time - last_joystick_event_time > BLUETOOTH_TIMEOUT:  # Check timeout
                motor1_speed = 0
                motor2_speed = 0
                arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
                print("Joystick disconnected for more than 1 second(s). Motors stopped.")
            # Check for reconnected joysticks
            pygame.joystick.quit()  # Uninitialize the joystick module
            pygame.joystick.init()  # Reinitialize the joystick module

            # Check if a joystick is available
            joystick_count = pygame.joystick.get_count()
            if joystick_count > 0:
                joystick = pygame.joystick.Joystick(0)  # Reinitialize the first joystick
                joystick.init()
                print("Joystick reconnected.")
            else:
                print("No joystick detected. Waiting for reconnection.")

            continue  # Skip the rest of the loop until joystick reconnects

        # Read the Y-axis of the left joystick to control differential robot drive
        left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

        # Apply deadzone to joystick inputs
        if abs(left_x_axis) < DEADZONE:
            left_x_axis = 0
        if abs(left_y_axis) < DEADZONE:
            left_y_axis = 0

        # Remote E-stop - if button 0 is pressed (exit the program)
        button_0_pressed = joystick.get_button(0)
        if button_0_pressed:
            motor1_speed = 0
            motor2_speed = 0
            arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
            print("Emergency E-stop has been pressed - program ended.")
            pygame.quit()
            exit()

        # Check if button deadman is pressed (allow joystick input)
        button_deadman_pressed = joystick.get_button(DEADMAN)

        if not button_deadman_pressed:
            if not deadman_message_shown:
                print("Please hold down the deadman button to control the motors.")
                deadman_message_shown = True
            motor1_speed = 0
            motor2_speed = 0
            arduino.write(f"{motor1_speed},{motor2_speed}\n".encode())  # Send stop command
            sleep(0.5)  # Delay to prevent spamming the message
            continue  # Skip the rest of the loop
        else:
            deadman_message_shown = False

        # Scale the axis values
        scaled_left_x = map_axis_to_range(left_x_axis)
        scaled_left_y = map_axis_to_range(left_y_axis)

        # Apply threshold to ensure no motor operates unless joystick is moved enough
        if abs(scaled_left_x) < THRESHOLD:
            scaled_left_x = 0
        if abs(scaled_left_y) < THRESHOLD:
            scaled_left_y = 0

        # Adjust steering sensitivity based on Y-axis speed (forward/backward)
        steering_sensitivity = adjust_steering_sensitivity(abs(scaled_left_y))

        # Control logic for forward and backward movement (Y-axis)
        motor1_speed = scaled_left_y
        motor2_speed = scaled_left_y

        # Control logic for left-right movement (X-axis) with adjusted steering sensitivity
        if scaled_left_x > 0:  # Positive X-axis: Motor 1 faster, Motor 2 slower
            motor1_speed = min(250, motor1_speed + int(scaled_left_x * steering_sensitivity))
            motor2_speed = max(0, motor2_speed - int(scaled_left_x * steering_sensitivity))
        elif scaled_left_x < 0:  # Negative X-axis: Motor 1 slower, Motor 2 faster
            motor1_speed = max(0, motor1_speed + int(scaled_left_x * steering_sensitivity))
            motor2_speed = min(250, motor2_speed - int(scaled_left_x * steering_sensitivity))

        # Send the joystick values to the Arduino via serial
        message = f"{motor1_speed},{motor2_speed}\n"
        arduino.write(message.encode())  # Send data as bytes

        # Read Arduino response and clear buffer if necessary
        if arduino.in_waiting > 0:
            arduino.readline()  # Clear any old data from the buffer

        sleep(0.05)  # Shorten sleep time to reduce lag

except KeyboardInterrupt:
    print("Exiting program.")
finally:
    pygame.quit()
    arduino.close()
