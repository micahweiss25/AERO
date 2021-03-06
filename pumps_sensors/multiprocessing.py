from time import sleep
import serial
try:
    import multiprocessing as mp
except RuntimeError:
    print("multiprocessing failed to import")
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
GPIO.setup(7, GPIO.IN) # GPIO7 = read whether big pump is on or not
def mist_cycle():
    try:
        while True:
            GPIO.output(2, GPIO.LOW)
            sleep(300)
            GPIO.output(2, GPIO.HIGH)
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
    
def res_maintain():
    try:
        ser = serial.Serial('/dev/ttyACM0',9600)
    except:
        print("failed to find serial")
    s = [0]
    while True:
        read_serial = ser.readline() ## find the format so you can just get numbers
        print(read_serial)
        # or modify ph sketch 
        # Should I pipe data from this function to a different one?
        ##### FOR NOW #####
        ph_balance = int(read_serial[read_serial.index('pH:')+3:read_serial.index('pH:')+7])
        if ph_balance > 6.3:
            GPIO.output(3, GPIO.HIGH)
            sleep(5)
            GPIO.output(3, GPIO.LOW)
            sleep(300)
        elif ph_balance < 5.3:
            GPIO.output(4, GPIO.HIGH)
            sleep(5)
            GPIO.output(4, GPIO.LOW)
            sleep(300)



if __name__ == '__main__':
    mist_cycle_process = mp.Process(target=mist_cycle, args=(None,))
    res_maintain_process = mp.Process(target=res_maintain, args=(None,))

    mist_cycle_process.start()
    res_maintain_process.start()
    mist_cycle_process.join()
    res_maintain_process.join()
