import os

if os.environ['STAGE'] == "RASPI_MODE":
    import RPi.GPIO as GPIO
else:
    BCM = "BCM"
    OUT = "OUT"
    LOW = "LOW"
    class PWM():
        def __init__(self, pin, frequency):
            print('PWM with pin {} and frequency {}'.format(pin, frequency))
        def start(self, duty_cycle):
            print('Starting PWM with duty cycle {}'.format(duty_cycle))
        def ChangeDutyCycle(self, duty_cycle):
            print('Changing PWM duty cycle to {}'.format(duty_cycle))
        def stop():
            print('Stopping PWM')
    def setwarnings(warning):
        print('Warnings set to {}'.format(warning))
    def setup(pwm_pin, GPIO_type):
        print('Setup with\n PWM pin: {}\n GPIO_type: {}'.format(pwm_pin, GPIO_type))
    def setmode(GPIO_mode):
        print('Set GPIO mode to {}'.format(GPIO_mode))
    def output(pwm_pin, GPIO_type):
        print('Output set to {} with PWM pin {}'.format(GPIO_type, pwm_pin))