# Author: Davebot
# Developed in conjunction with ChatGPT
# Verion 1 Date: 22/Dec/2024
# 
# This program is designed to interface with a joystick and read the joystick axis values and button presses. 
# It uses pygame to capture joystick input, including axis values for both joysticks (0-5) and button presses. 
# The program features a deadman switch functionality using Button 6 (LB), where the joysticks will only respond when Button 9 is pressed. 
# Additionally, it includes fire control on Button 10, which is only displayed when pressed. The joystick axis values are scaled 
# from -100 to +100 for easier interpretation. The program continuously checks for button presses and axis changes, 
# updating the terminal with the current joystick status. 

# Pressing Button 6 enables joystick input, while Button 7 triggers a fire action when pressed.

##########################################################################################################
##########################################################################################################
##########################################################################################################

#Check which button is pressed 

import pygame
from time import sleep

# Initialize pygame
pygame.init()

# Configure the joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
joystick.init()

# Get the total number of buttons on the joystick
num_buttons = joystick.get_numbuttons()

try:
    print("Controller Ready. Press any button to see which ones are pressed.")
    while True:
        pygame.event.pump()  # Process joystick events

        # Check all buttons
        for button_id in range(num_buttons):
            button_pressed = joystick.get_button(button_id)
            if button_pressed:
                print(f"Button {button_id} is pressed!")

        # Read and print the joystick axis values (axes 0 to 5)
        for axis_id in range(6):  # Assuming there are at least 6 axes
            axis_value = joystick.get_axis(axis_id)
            print(f"Axis {axis_id}: {axis_value:.2f}")

        sleep(0.05)  # Add a small delay to avoid CPU overload

except KeyboardInterrupt:
    print("Exiting program.")
finally:
    pygame.quit()

##########################################################################################################
##########################################################################################################
##########################################################################################################

# Davebot 2 axis control with LB button (button 9) as a deadman switch

# import pygame
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Configure the joystick
# pygame.joystick.init()
# joystick = pygame.joystick.Joystick(0)  # Use the first connected joystick
# joystick.init()

# # Function to map joystick axis to a range of -100 to +100
# def map_axis_to_range(value):
#     # Joystick axis ranges from -1.0 to 1.0
#     # Map this to -100 to +100
#     return int(value * 100)

# try:
#     print("Controller Ready. Use the joysticks to see X and Y values between -100 and +100.")
#     while True:
#         pygame.event.pump()  # Process joystick events

#         # Check if button 6 (deadman switch) is pressed
#         button_6_pressed = joystick.get_button(6)
#         if not button_6_pressed:
#             print("Button 6 is NOT pressed! Deadman switch activated. Joysticks are disabled.")
#             sleep(0.05)  # Add a small delay before checking again
#             continue  # Skip joystick processing if button 9 is not pressed

#         # Read the X-axis and Y-axis of the left joystick to control differential robot drive
#         left_x_axis = joystick.get_axis(0)  # X-axis of the left joystick
#         left_y_axis = -joystick.get_axis(1)  # Y-axis of the left joystick (flipped)

#         # Read the X-axis and Y-axis of the right joystick for use with turret
#         right_x_axis = joystick.get_axis(2)  # X-axis of the right joystick
#         right_y_axis = -joystick.get_axis(3)  # Y-axis of the right joystick (flipped)

#         # Add fire control on button 10 
#         button_7_pressed = joystick.get_button(7)

#         # Scale the axis values
#         scaled_left_x = map_axis_to_range(left_x_axis)
#         scaled_left_y = map_axis_to_range(left_y_axis)
#         scaled_right_x = map_axis_to_range(right_x_axis)
#         scaled_right_y = map_axis_to_range(right_y_axis)

#         # Print the scaled values to the terminal
#         print(
#             f"Left Joystick - X: {scaled_left_x}, Y: {scaled_left_y} | "
#             f"Right Joystick - X: {scaled_right_x}, Y: {scaled_right_y}"
#         )

#         # Print the button 10 status only when it is pressed
#         if button_7_pressed:
#             print("Button 7 is pressed - fire")

#         sleep(0.05)  # Add a small delay to avoid CPU overload

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     pygame.quit()