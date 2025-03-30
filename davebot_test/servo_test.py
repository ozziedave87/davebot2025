# Servo test: 270 degrees of rotation
##########################################################################################
"""
High Rotation Servo Specifications:

Controllable angle range: 0 to 180 degrees, excellent linearity, precision control.

Electrical Specification:
- Operating voltage range: 4.8-6.8V
- Operating speed (6.0V): 0.15 sec/60°
- Operating speed (6.8V): 0.13 sec/60°
- Stall torque (6.0V): 21kg/cm
- Stall torque (6.8V): 25kg/cm

Control Specification:
- Control System: PWM (Pulse Width Modulation)
- Pulse width range: 500-2500μsec
- Neutral position: 1500μsec
- Running degree: 180° (when 500-2500μsec)
- Dead band width: 3μsec
- Operating frequency: 50-330Hz
- Rotating direction: Counterclockwise (when 500~2500μsec)
- Gear ratio: 275
- Bearing: Double bearing
- Waterproof performance: IP66
"""

# from gpiozero import Servo
# from time import sleep

# # Pin configuration
# SERVO_PIN = 13
# sleep_time = 2

# # Adjust these values based on your servo's datasheet
# MIN_PULSE_WIDTH = 0.5 / 1000  # 0.5 ms (converted to seconds)
# MAX_PULSE_WIDTH = 2.5 / 1000  # 2.5 ms (converted to seconds)

# # Servo object with custom pulse width range
# servo = Servo(SERVO_PIN, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH)

# def test_servo():
#     print("Starting servo test...")
#     try:
#         while True:
#             print("Moving to minimum position (0 degrees)")
#             servo.min()  # Move servo to 0 degrees
#             sleep(sleep_time)
            
#             # print("Moving to middle position (135 degrees)")
#             # servo.mid()  # Move servo to 135 degrees
#             # sleep(sleep_time)
            
#             print("Moving to maximum position (270 degrees)")
#             servo.max()  # Move servo to 270 degrees
#             sleep(sleep_time)
#     except KeyboardInterrupt:
#         print("Test interrupted by user. Exiting...")
#     finally:
#         servo.detach()  # Detach the servo
#         print("Servo test complete.")

# if __name__ == "__main__":
#     test_servo()

##########################################################################################

# from gpiozero import Servo
# from time import sleep

# # Pin configurations
# SERVO_PINS = [12, 13, 19]
# SLEEP_TIME = 2

# # Adjust these values based on your servo's datasheet
# MIN_PULSE_WIDTH = 0.5 / 1000  # 0.5 ms (converted to seconds)
# MAX_PULSE_WIDTH = 2.5 / 1000  # 2.5 ms (converted to seconds)

# def test_servo(pin):
#     # Create a Servo object for the specified pin
#     servo = Servo(pin, min_pulse_width=MIN_PULSE_WIDTH, max_pulse_width=MAX_PULSE_WIDTH)
#     print(f"Starting servo test on pin {pin}...")
#     try:
#         print("Moving to minimum position (0 degrees)")
#         servo.min()  # Move servo to 0 degrees
#         sleep(SLEEP_TIME)
        
#         print("Moving to maximum position (270 degrees)")
#         servo.max()  # Move servo to 270 degrees
#         sleep(SLEEP_TIME)
#     except KeyboardInterrupt:
#         print("Test interrupted by user. Exiting...")
#     finally:
#         servo.detach()  # Detach the servo
#         print(f"Servo test complete on pin {pin}.")

# if __name__ == "__main__":
#     for pin in SERVO_PINS:
#         test_servo(pin)


##########################################################################################


from gpiozero import Servo
from time import sleep

# Pin configurations
SERVO_PINS = {
    12: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # High Rotation Servo
    13: {"min_pulse": 0.5 / 1000, "max_pulse": 2.5 / 1000},  # High Rotation Servo
}
SLEEP_TIME = 2

# Separate configuration for pin 19 (MG996R Servo)
SERVO_19_CONFIG = {"min_pulse": 0.8 / 1000, "max_pulse": 2.4 / 1000}

def test_servo(pin, min_pulse, max_pulse):
    # Create a Servo object for the specified pin with custom pulse width range
    servo = Servo(pin, min_pulse_width=min_pulse, max_pulse_width=max_pulse)
    print(f"Starting servo test on pin {pin}...")
    try:
        print("Moving to minimum position")
        servo.min()  # Move servo to minimum position
        sleep(SLEEP_TIME)
        
        print("Moving to maximum position")
        servo.max()  # Move servo to maximum position
        sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("Test interrupted by user. Exiting...")
    finally:
        servo.detach()  # Detach the servo
        print(f"Servo test complete on pin {pin}.")

if __name__ == "__main__":
    # Test servos on pins 12 and 13
    for pin, config in SERVO_PINS.items():
        test_servo(pin, config["min_pulse"], config["max_pulse"])
    
    # Test servo on pin 19 separately
    test_servo(19, SERVO_19_CONFIG["min_pulse"], SERVO_19_CONFIG["max_pulse"])


