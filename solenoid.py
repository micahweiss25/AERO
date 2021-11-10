from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setwarnings(False) # turn off warnings
GPIO.setmode(GPIO.BCM) # use GPIO numbers to specify inputs
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW) # use GPIO2 as output

try:
    while True:
        GPIO.output(2, GPIO.LOW)
        sleep(300.0)
        GPIO.output(2, GPIO.HIGH)
        sleep(5.0)
except KeyboardInterrupt:
    GPIO.cleanup()
    