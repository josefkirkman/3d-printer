import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

STEPDELAY = 0.00008
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
stepper_pins = (26, 19, 13)
direction = 20
step = 21

stepper = RpiMotorLib.A4988Nema(direction, step, stepper_pins, "A4988")

print("stepper initialized")

dir = input("up? (enter True or False):")
motor_direction = True
if dir == "True":
	motor_direction = True
elif dir == "False":
	motor_direction = False
steps = input("how many steps? (enter an integer):")
print("moving " + steps + " steps")

stepper.motor_go(motor_direction, "1/16", int(steps), STEPDELAY, False, 0)

input("back down? (enter anything to go back down):")

stepper.motor_go((not motor_direction), "1/16", int(steps), STEPDELAY, False, 0)
