import os

if os.environ['STAGE'] == "RASPI_MODE":
    from RpiMotorLib import RpiMotorLib
else:
    class A4988Nema(object):
        def __init__(self, direction_pin, step_pin, mode_pins, motor_type="A4988"):
            print('Initializing Nema bi-polar stepper motor with\n Direction pin: {}\n Step pin: {}\n Mode pins: {}\n Motor type: {}'.format(direction_pin, step_pin, mode_pins, motor_type))
        def motor_stop(self):
            print('Stopping motor')
        def resolution_set(self, steptype):
            print('Setting step resolution')
        def motor_go(self, clockwise=False, steptype="Full", steps=200, stepdelay=.005, verbose=False, initdelay=.05):
            print('Moving stepper motor with\n Clockwise: {}\n Steptype: {}\n Steps: {}\n Stepdelay: .005\n Verbose: {}\n Initdelay: {}'.format(clockwise, steptype, steps, stepdelay, verbose, initdelay))
        