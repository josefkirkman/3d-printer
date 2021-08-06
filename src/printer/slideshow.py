from PIL import Image, ImageTk
import tkinter
import os
import sys
import time
import json
import settings

from models import custom_GPIO as GPIO
from models import custom_motorLib as RpiMotorLib

print_folder_path = sys.argv[sys.argv.index('-f') + 1]
with open(os.path.join(print_folder_path,'params.json')) as f:
    params = json.load(f)

#print(params)

LAYER_TIME = params['exposure_time'] # in seconds, exposure time
FIRST_LAYER_TIME = params['first_layer_exposure_time'] # in seconds, first layer exposure time
LAYER_HEIGHT = params['layer_thickness'] # layer thickness
STEPDELAY = params['step_delay'] # step_delay
RETRACTION_DWELL_TIME = params['retraction_dwell_time']
SETTING_TIME = params['setting_time']
RETRACTION_DEPTH = int(params['retraction_depth'])
PWM_PIN = 12
# NUM_FIRST_LAYERS = 2


class printer(tkinter.Tk):
    def __init__(self, image_filenames, delay):
        tkinter.Tk.__init__(self)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.overrideredirect(1)
        #self.geometry("%dx%d" % (self.width, self.height))
        self.geometry("1920x1080")
        self.bind("X", lambda fn: (fn.widget.withdraw(), fn.widget.quit()))
        self.delay = delay
        self.pictures = []
        self.frame_index = 0
        for frame in image_filenames:
            self.pictures.append(frame)
        self.picture_display = tkinter.Label(self)
        self.picture_display.pack(expand=True, fill="both")

    def show_layers(self):
        print(self.frame_index)
        if self.frame_index == 0:
            # longer first layer
            current_frame = self.pictures[self.frame_index]
            self.frame_index += 1
            display_frame = ImageTk.PhotoImage(Image.open(current_frame))
            self.picture_display.config(image=display_frame)
            self.picture_display.image = display_frame
            self.title(os.path.basename(current_frame))
            pwm.ChangeDutyCycle(100)
            # time.sleep(FIRST_LAYER_TIME - LAYER_TIME) # long first layer - layer time because layer time is run subsequently
            self.after((FIRST_LAYER_TIME - LAYER_TIME + self.delay) * 1000, self.show_black)
        elif self.frame_index < len(self.pictures):
            current_frame = self.pictures[self.frame_index]
            self.frame_index += 1
            display_frame = ImageTk.PhotoImage(Image.open(current_frame))
            self.picture_display.config(image=display_frame)
            self.picture_display.image = display_frame
            self.title(os.path.basename(current_frame))
            # motor_go(clockwise, steptype", LAYER_HEIGHT, stepdelay, verbose, initdelay)
            stepper.motor_go(False, "1/16" , 16 * RETRACTION_DEPTH, STEPDELAY, False, 0)
            time.sleep(int(RETRACTION_DWELL_TIME))
            stepper.motor_go(True, "1/16" , 16 * (RETRACTION_DEPTH - LAYER_HEIGHT), STEPDELAY, False, 0)
            self.after(self.delay * 1000, self.show_black)
            time.sleep(int(SETTING_TIME))
            pwm.ChangeDutyCycle(100)
        else:
            stepper.motor_go(True, "1/16" , 10 * 16 * LAYER_HEIGHT, STEPDELAY, False, 0)
            pwm.stop()
            sys.exit()

    def show_black(self):
        current_frame = "black.jpg"
        display_frame = ImageTk.PhotoImage(Image.open(current_frame))
        self.picture_display.config(image=display_frame)
        self.picture_display.image = display_frame
        self.title(os.path.basename(current_frame))
        self.after(int(1000 * (LAYER_HEIGHT + RETRACTION_DEPTH) * STEPDELAY), self.show_layers)
        pwm.ChangeDutyCycle(0)
        
# Collects image files from "layers" directory (which is in same directory as this script).
layers = []

for filename in os.listdir(os.path.join(print_folder_path,'layers')):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        layers.append(os.path.join(print_folder_path,'layers',filename))

# Sorts the image files (cause I'm not sure if the above for loop goes in any particular order).
enumerated_layers = []
for layer in layers:
    print(os.path.basename(layer)[:os.path.basename(layer).index('.')])
    enumerated_layers.append((int(os.path.basename(layer)[:os.path.basename(layer).index('.')]),layer))
enumerated_layers = sorted(enumerated_layers)
for i in range(len(layers)):
    layers[i] = enumerated_layers[i][1]
print(layers)
# Sets up PWM.
global pwm
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.output(PWM_PIN, GPIO.LOW)
pwm = GPIO.PWM(PWM_PIN, 1000) # Set Frequency to 1 KHz
pwm.start(100)

# Sets up motor.
GPIO_pins = (26, 19, 13)
direction = 20
step = 21
stepper = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

main = printer(layers, LAYER_TIME + RETRACTION_DWELL_TIME + SETTING_TIME)
main.show_layers()
main.mainloop()

