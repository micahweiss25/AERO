from time import sleep
import serial

def set_GPIO():
    try:
        import RPi.GPIO as GPIO
    except RuntimeError:
        print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

    GPIO.setwarnings(False) # turn off warnings
    GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
    GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW) # GPIO2 = soleniod
    GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # GPIO3 = acid
    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) # GPIO4 = base
    GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # GPIO5 = water
    GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # GPIO6 = nuterients

def start_cycle():
    try:
        while True:
            GPIO.output(2, GPIO.LOW)
            sleep(300.0)
            GPIO.output(2, GPIO.HIGH)
            sleep(5.0)
    except KeyboardInterrupt:
        GPIO.cleanup()

set_GPIO()
start_cycle()

