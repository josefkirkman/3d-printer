import RPi.GPIO as GPIO
import time
 
pwmPin = 32
def pwmSetup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pwmPin, GPIO.OUT)
    GPIO.output(pwmPin, GPIO.LOW)
    pwm = GPIO.PWM(pwmPin, 1000) # Set Frequency to 1 KHz
    pwm.start(0) # Set the starting Duty Cycle
     
def loop():
    while True:
        for dc in range(0, 101, 1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100, -1, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
         
def destroy():
    pwm.stop()
    GPIO.output(pwmPin, GPIO.LOW)
    GPIO.cleanup()
     
if  __name__ == '__main__':
    pwmSetup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()