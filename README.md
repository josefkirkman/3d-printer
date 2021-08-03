# 3d-printer
Software documentation for Dienda. Setup is just a matter of setting up a virtual environment and `pip install -r requirements.txt`. 
## motor_control_test
### Dependencies
- RPi.GPIO: standard python package for connecting to raspberry pi
- RpiMotoLib: full documentaiton is [here](https://github.com/gavinlyonsrepo/RpiMotorLib)
### Functionality
- Runs a routine through a motor connected to the raspberry pi

## move_stepper
### Dependencies
- RPi.GPIO
- RPiMotorLib
### Functionality
- User tells rpi motor to move up or down by some number of steps

## pwm_test
### Dependencies
- Rpi.GPIO
### Functionality
- Outputs some PWM signal through pin 32 on the raspberry pi until interrupted.

## slideshow
### Dependencies
- PIL: python package for processing images
- tkinter: python package for making GUIs.
- RPi.GPIO
### Functionality
- Sequentially displays the images in the layers directory to the raspberry pi. 
- `python src/slideshow -f $PRINT_FOLDER`
- Use the `-p` tag to show the images on your computer

## wash
### Dependencies
- RPi.GPIO
### Functionality
- Rotates a motor