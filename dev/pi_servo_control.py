# # Xbox Controller Servo Control Script
# # Change Log:
# # V1.0 - Implemented control for yaw, pitch, and actuation servos using an Xbox controller.

# import pygame
# from gpiozero import Servo
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Servo configurations
# SERVO_CONFIGS = {
#     12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # Yaw servo
#     13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # Pitch servo
#     19: {"min_pulse": 0.8 / 1000, "max_pulse": 2.4 / 1000},  # Actuation servo
# }

# # Initialize servos
# yaw_servo = Servo(12, min_pulse_width=SERVO_CONFIGS[12]["min_pulse"], max_pulse_width=SERVO_CONFIGS[12]["max_pulse"])
# pitch_servo = Servo(13, min_pulse_width=SERVO_CONFIGS[13]["min_pulse"], max_pulse_width=SERVO_CONFIGS[13]["max_pulse"])
# actuation_servo = Servo(19, min_pulse_width=SERVO_CONFIGS[19]["min_pulse"], max_pulse_width=SERVO_CONFIGS[19]["max_pulse"])

# # Deadman and action button configuration
# deadman_button = 6
# fire_button = 7

# # Check joystick connection
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize joystick
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Helper function to map joystick axis to servo range
# def map_axis_to_servo(value, min_position, max_position):
#     return min_position + (value + 1) * (max_position - min_position) / 2

# # Main control loop
# try:
#     print("Controller Ready. Use the joystick and buttons to control the servos.")
#     while True:
#         pygame.event.pump()

#         # Check if the deadman button is pressed
#         if not joystick.get_button(deadman_button):
#             print("Deadman button not pressed. Returning servos to rest positions.")
#             yaw_servo.mid()
#             pitch_servo.min()
#             actuation_servo.min()
#             sleep(0.1)
#             continue

#         # # Control yaw servo (pin 12)
#         # yaw_value = joystick.get_axis(2)  # Right joystick X-axis
#         # yaw_position = map_axis_to_servo(yaw_value, -1, 1)  # Map to servo range
#         # yaw_servo.value = yaw_position

#         # Control pitch servo (pin 13)
#         pitch_value = joystick.get_axis(3)  # Right joystick Y-axis
#         if pitch_value > 0:  # Only positive values affect the servo
#             pitch_position = map_axis_to_servo(pitch_value, -1, 1)
#             pitch_servo.value = pitch_position
#         else:
#             pitch_servo.min()  # Rest position

#         # Control actuation servo (pin 19)
#         if joystick.get_button(fire_button):
#             actuation_servo.max()  # Max position when button is pressed
#         else:
#             actuation_servo.min()  # Min position when button is not pressed

#         sleep(0.01)  # Small delay to reduce CPU usage

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     # Reset all servos to their rest positions
#     yaw_servo.mid()
#     pitch_servo.min()
#     actuation_servo.min()
#     pygame.quit()

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
# Xbox Controller Servo Control Script
# Change Log:
# V1.0 - Implemented control for yaw, pitch, and actuation servos using an Xbox controller.

# import pygame
# from gpiozero import Servo
# from time import sleep

# # Initialize pygame
# pygame.init()

# # Servo configurations
# SERVO_CONFIGS = {
#     12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # Yaw servo
#     13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # Pitch servo
#     19: {"min_pulse": 0.8 / 1000, "max_pulse": 2.4 / 1000},  # Actuation servo
# }

# # Initialize servos
# yaw_servo = Servo(12, min_pulse_width=SERVO_CONFIGS[12]["min_pulse"], max_pulse_width=SERVO_CONFIGS[12]["max_pulse"])
# pitch_servo = Servo(13, min_pulse_width=SERVO_CONFIGS[13]["min_pulse"], max_pulse_width=SERVO_CONFIGS[13]["max_pulse"])
# actuation_servo = Servo(19, min_pulse_width=SERVO_CONFIGS[19]["min_pulse"], max_pulse_width=SERVO_CONFIGS[19]["max_pulse"])

# # Deadman and action button configuration
# deadman_button = 6
# fire_button = 7

# # Check joystick connection
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize joystick
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Helper function to map joystick axis to servo range
# def map_axis_to_servo(value, min_position, max_position):
#     return min_position + (value + 1) * (max_position - min_position) / 2

# # Main control loop
# try:
#     print("Controller Ready. Use the joystick and buttons to control the servos.")
#     while True:
#         pygame.event.pump()

#         # Check if the deadman button is pressed
#         if not joystick.get_button(deadman_button):
#             print("Deadman button not pressed. Returning servos to rest positions.")
#             yaw_servo.mid()
#             pitch_servo.min()
#             actuation_servo.min()
#             sleep(0.1)
#             continue

#         # Control yaw servo (pin 12)
#         yaw_value = joystick.get_axis(2)  # Right joystick X-axis
#         yaw_position = map_axis_to_servo(yaw_value, -1, 1)  # Map to servo range
#         yaw_servo.value = yaw_position

#         # Control pitch servo (pin 13)
#         pitch_value = joystick.get_axis(3)  # Right joystick Y-axis
#         if pitch_value > 0:  # Only positive values affect the servo
#             pitch_position = map_axis_to_servo(pitch_value, -1, 1)
#             pitch_servo.value = pitch_position
#         else:
#             pitch_servo.min()  # Rest position

#         # Control actuation servo (pin 19)
#         if joystick.get_button(fire_button):
#             actuation_servo.max()  # Max position when button is pressed
#         else:
#             actuation_servo.min()  # Min position when button is not pressed

#         sleep(0.01)  # Small delay to reduce CPU usage

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     # Reset all servos to their rest positions
#     yaw_servo.mid()
#     pitch_servo.min()
#     actuation_servo.min()
#     pygame.quit()

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
# import pygame
# from gpiozero import Servo
# from time import sleep

# # Xbox Controller Servo Control Script
# # Change Log:
# # V1.0 - Implemented control for yaw, pitch, and actuation servos using an Xbox controller.
# # V1.1 - Added deadband to joystick inputs to reduce servo twitching.

# # Initialize pygame
# pygame.init()

# # Servo configurations
# SERVO_CONFIGS = {
#     12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # Yaw servo
#     13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # Pitch servo
#     19: {"min_pulse": 0.8 / 1000, "max_pulse": 2.4 / 1000},  # Actuation servo
# }

# # Initialize servos
# yaw_servo = Servo(12, min_pulse_width=SERVO_CONFIGS[12]["min_pulse"], max_pulse_width=SERVO_CONFIGS[12]["max_pulse"])
# pitch_servo = Servo(13, min_pulse_width=SERVO_CONFIGS[13]["min_pulse"], max_pulse_width=SERVO_CONFIGS[13]["max_pulse"])
# actuation_servo = Servo(19, min_pulse_width=SERVO_CONFIGS[19]["min_pulse"], max_pulse_width=SERVO_CONFIGS[19]["max_pulse"])

# # Deadman and action button configuration
# deadman_button = 6
# fire_button = 7

# # Check joystick connection
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     pygame.quit()
#     exit()

# # Initialize joystick
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Helper function to map joystick axis to servo range
# def map_axis_to_servo(value, min_position, max_position):
#     return min_position + (value + 1) * (max_position - min_position) / 2

# # Initialize servos to start positions
# yaw_servo.mid()
# pitch_servo.min()
# actuation_servo.min()

# # Main control loop
# try:
#     print("Controller Ready. Use the joystick and buttons to control the servos.")
#     while True:
#         pygame.event.pump()

#         # Check if the deadman button is pressed
#         if not joystick.get_button(deadman_button):
#             print("Deadman button not pressed. Returning servos to rest positions.")
#             yaw_servo.value = None
#             pitch_servo.value = None
#             actuation_servo.value = None
#             sleep(0.1)
#             continue

#         # Control yaw servo (pin 12)
#         yaw_value = joystick.get_axis(2)  # Right joystick X-axis
#         if abs(yaw_value) > 0.05:  # Deadband to prevent twitching
#             yaw_position = map_axis_to_servo(yaw_value, -1, 1)  # Map to servo range
#             yaw_servo.value = yaw_position
#         else:
#             yaw_servo.value = None

#         # Control pitch servo (pin 13)
#         pitch_value = joystick.get_axis(3)  # Right joystick Y-axis
#         if abs(pitch_value) > 0.05:  # Deadband to prevent twitching
#             pitch_position = map_axis_to_servo(pitch_value, -1, 1)
#             pitch_servo.value = pitch_position
#         else:
#             pitch_servo.value = None

#         # Control actuation servo (pin 19)
#         if joystick.get_button(fire_button):
#             actuation_servo.max()  # Max position when button is pressed
#         else:
#             actuation_servo.value = None

#         sleep(0.01)  # Small delay to reduce CPU usage

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     # Reset all servos to their home positions
#     yaw_servo.mid()
#     pitch_servo.min()
#     actuation_servo.min()
#     pygame.quit()

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

# import pygame
# from gpiozero import Servo
# from time import sleep

# # Xbox Controller Servo Control Script - Corrected Range for Servo Values
# # joystick control of servo 12 and 13 is working

# # Initialize pygame
# pygame.init()

# # Servo configurations for yaw (pin 12) and pitch (pin 13)
# SERVO_CONFIGS = {
#     12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},
#     13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},
# }

# # Initialize servos
# yaw_servo = Servo(12, min_pulse_width=SERVO_CONFIGS[12]["min_pulse"], max_pulse_width=SERVO_CONFIGS[12]["max_pulse"])
# pitch_servo = Servo(13, min_pulse_width=SERVO_CONFIGS[13]["min_pulse"], max_pulse_width=SERVO_CONFIGS[13]["max_pulse"])

# # Set servos to their home positions
# yaw_servo.mid()
# pitch_servo.min()

# # Check joystick connection
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     yaw_servo.mid()
#     pitch_servo.min()
#     pygame.quit()
#     exit()

# # Initialize joystick
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Helper function to map joystick axis to servo range (-1 to 1)
# def map_axis_to_servo(value):
#     return max(-1, min(1, value))  # Clamp the value between -1 and 1

# # Main control loop
# try:
#     print("Controller Ready. Use the joystick to control the yaw and pitch servos.")
#     while True:
#         pygame.event.pump()

#         # Control yaw servo (pin 12)
#         yaw_value = joystick.get_axis(2)  # Right joystick X-axis
#         yaw_position = map_axis_to_servo(yaw_value)  # Map and clamp to servo range
#         yaw_servo.value = yaw_position

#         # Control pitch servo (pin 13)
#         pitch_value = joystick.get_axis(3)  # Right joystick Y-axis
#         if pitch_value < 0:  # Move only when the joystick is pushed upward
#             pitch_position = map_axis_to_servo(pitch_value)  # Map and clamp to servo range
#             pitch_servo.value = pitch_position
#         else:
#             pitch_servo.value = None  # Keep the servo stationary when joystick is down

#         sleep(0.005)  # Reduced delay for faster response

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     # Reset servos to their home positions
#     yaw_servo.mid()
#     pitch_servo.min()
#     pygame.quit()


######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

# Changes made to control Servo 19 (Actuation Servo) using Button 7 (Fire Button) on the Xbox controller:
# - Servo 19 (Actuation Servo) is mapped to Button 7 (Fire Button).
# - When Button 7 is pressed, Servo 19 moves to its maximum position (actuation_servo.max()).
# - When Button 7 is not pressed, Servo 19 returns to its minimum position (actuation_servo.min()).
# This allows toggling the servo between its min and max positions based on the button press state.


# import pygame
# from gpiozero import Servo
# from time import sleep

# # Xbox Controller Servo Control Script - Corrected Range for Servo Values

# # Initialize pygame
# pygame.init()

# # Servo configurations for yaw (pin 12), pitch (pin 13), and actuation (pin 19)
# SERVO_CONFIGS = {
#     12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},
#     13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},
#     19: {"min_pulse": 0.8 / 1000, "max_pulse": 2.4 / 1000},  # Actuation servo
# }

# # Initialize servos
# yaw_servo = Servo(12, min_pulse_width=SERVO_CONFIGS[12]["min_pulse"], max_pulse_width=SERVO_CONFIGS[12]["max_pulse"])
# pitch_servo = Servo(13, min_pulse_width=SERVO_CONFIGS[13]["min_pulse"], max_pulse_width=SERVO_CONFIGS[13]["max_pulse"])
# actuation_servo = Servo(19, min_pulse_width=SERVO_CONFIGS[19]["min_pulse"], max_pulse_width=SERVO_CONFIGS[19]["max_pulse"])

# # Set servos to their home positions
# yaw_servo.mid()
# pitch_servo.min()
# actuation_servo.min()

# # Check joystick connection
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("No joystick detected.")
#     yaw_servo.mid()
#     pitch_servo.min()
#     actuation_servo.min()
#     pygame.quit()
#     exit()

# # Initialize joystick
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
# print(f"Joystick detected: {joystick.get_name()}")

# # Helper function to map joystick axis to servo range (-1 to 1)
# def map_axis_to_servo(value):
#     return max(-1, min(1, value))  # Clamp the value between -1 and 1

# # Main control loop
# try:
#     print("Controller Ready. Use the joystick to control the yaw, pitch, and actuation servos.")
#     while True:
#         pygame.event.pump()

#         # Control yaw servo (pin 12)
#         yaw_value = joystick.get_axis(2)  # Right joystick X-axis
#         yaw_position = map_axis_to_servo(yaw_value)  # Map and clamp to servo range
#         yaw_servo.value = yaw_position

#         # Control pitch servo (pin 13)
#         pitch_value = joystick.get_axis(3)  # Right joystick Y-axis
#         if pitch_value < 0:  # Move only when the joystick is pushed upward
#             pitch_position = map_axis_to_servo(pitch_value)  # Map and clamp to servo range
#             pitch_servo.value = pitch_position
#         else:
#             pitch_servo.value = None  # Keep the servo stationary when joystick is down

#         # Control actuation servo (pin 19) based on button 7
#         if joystick.get_button(7):  # Check if button 7 is pressed
#             actuation_servo.value = 1  # Move to max position
#         else:
#             actuation_servo.value = -1  # Move to min position

#         sleep(0.005)  # Reduced delay for faster response

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     # Reset servos to their home positions
#     yaw_servo.mid()
#     pitch_servo.min()
#     actuation_servo.min()
#     pygame.quit()

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

import pygame
from gpiozero import Servo
from time import sleep

# Xbox Controller Servo Control Script - Corrected Range for Servo Values

# Initialize pygame
pygame.init()

# Servo configurations for yaw (pin 12), pitch (pin 13), and actuation (pin 19)
SERVO_CONFIGS = {
    12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},
    13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},
    19: {"min_pulse": 0.8 / 1000, "max_pulse": 2.4 / 1000},  # Actuation servo
}

# Initialize servos
yaw_servo = Servo(12, min_pulse_width=SERVO_CONFIGS[12]["min_pulse"], max_pulse_width=SERVO_CONFIGS[12]["max_pulse"])
pitch_servo = Servo(13, min_pulse_width=SERVO_CONFIGS[13]["min_pulse"], max_pulse_width=SERVO_CONFIGS[13]["max_pulse"])
actuation_servo = Servo(19, min_pulse_width=SERVO_CONFIGS[19]["min_pulse"], max_pulse_width=SERVO_CONFIGS[19]["max_pulse"])

# Set servos to their home positions
yaw_servo.mid()
pitch_servo.max()
actuation_servo.min()

# Check joystick connection
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick detected.")
    yaw_servo.mid()
    pitch_servo.max()
    actuation_servo.min()
    pygame.quit()
    exit()

# Initialize joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick detected: {joystick.get_name()}")

# Helper function to map joystick axis to servo range (-1 to 1)
def map_axis_to_servo(value):
    return max(-1, min(1, value))  # Clamp the value between -1 and 1

# Main control loop
try:
    print("Controller Ready. Use the joystick to control the yaw, pitch, and actuation servos.")
    while True:
        pygame.event.pump()

        # Control yaw servo (pin 12)
        yaw_value = joystick.get_axis(2)  # Right joystick X-axis
        if abs(yaw_value) > 0.1:  # Move only if the joystick is outside the deadband
            yaw_position = map_axis_to_servo(yaw_value)  # Map and clamp to servo range
            yaw_servo.value = yaw_position
        else:
            yaw_servo.mid()  # Return to home position

        # Control pitch servo (pin 13)
        pitch_value = joystick.get_axis(3)  # Right joystick Y-axis
        if pitch_value < 0.1:  # Move only if the joystick is outside the deadband
            pitch_position = map_axis_to_servo(pitch_value)  # Map and clamp to servo range
            pitch_servo.value = pitch_position
        elif pitch_value > -0.1:  # Move only if the joystick is outside the deadband
            pitch_servo.max()  # Return to home position
        else:
            pitch_servo.max()  # Return to home position

        # Control actuation servo (pin 19) based on button 7
        if joystick.get_button(7):  # Check if button 7 is pressed
            actuation_servo.value = 1  # Move to max position
        else:
            actuation_servo.value = -1  # Move to min position

        sleep(0.005)  # Reduced delay for faster response

except KeyboardInterrupt:
    print("Exiting program.")
finally:
    # Reset servos to their home positions
    yaw_servo.mid()
    pitch_servo.max()
    actuation_servo.min()
    pygame.quit()

