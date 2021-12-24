import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib


STEPDELAY = 0.00005
WASH_TIME = 300 # in seconds
WASH_STEPS = 25
WAIT_TIME = 0.25 # in seconds


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
stepper_pins = (21, 20, 16)
direction = 20
step = 21

stepper = RpiMotorLib.A4988Nema(direction, step, stepper_pins, "A4988")

for i in range(5):
	stepper.motor_go(False, "1/16", 16 * WASH_STEPS, STEPDELAY, False, 0)
	time.sleep(WAIT_TIME)
	stepper.motor_go(True, "1/16", 16 * WASH_STEPS, STEPDELAY, False, 0)
	time.sleep(WAIT_TIME)
