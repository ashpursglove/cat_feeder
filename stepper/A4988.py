import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

speed = 800.0

Time = 1/speed

pulse = 200

p=0
i=0

# Define GPIO signals to use
step_pin = 18 # use Pull down resistor
dir_pin = 19 # use Pull down resistor
enable_pin = 17 # use Pull up resistor
sleep_pin = 22 # use Pull down resistor

button_1 = 6
button_2 = 5

# bridge sleep pin and reset pin

GPIO.setup(button_1,GPIO.IN)
GPIO.setup(button_2,GPIO.IN)

GPIO.setup(enable_pin,GPIO.OUT) #Active low
GPIO.output(enable_pin, False)

GPIO.setup(sleep_pin,GPIO.OUT)
GPIO.output(sleep_pin, True) #Active low

GPIO.setup(step_pin,GPIO.OUT)
GPIO.output(step_pin, False)

GPIO.setup(dir_pin,GPIO.OUT)
GPIO.output(dir_pin, False)

while GPIO.input(button_2) + GPIO.input(button_1) != 2: # us 2 buttons at same time to exit program and shutdown GPIO
    
    if GPIO.input(button_1) == 1:
        GPIO.output(dir_pin, False)
        
        GPIO.output(step_pin, True)
        time.sleep(Time)
        GPIO.output(step_pin, False)
        time.sleep(Time)
        
    if GPIO.input(button_2) == 1:
        GPIO.output(dir_pin, True)
        
        GPIO.output(step_pin, True)
        time.sleep(Time)
        GPIO.output(step_pin, False)
        time.sleep(Time)

GPIO.cleanup()
print ("Succesful Shutdown")
 

 