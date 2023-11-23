import RPi.GPIO as GPIO
import time
import sys

Tring = 27
Echo = 18

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(Tring, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)


def read_distance():
    GPIO.output(Tring, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Tring, GPIO.LOW)
    
    while GPIO.input(Echo) == GPIO.LOW:
        sig_off = time.time()
    while GPIO.input(Echo) == GPIO.HIGH:
        sig_on = time.time()
        
    duration = sig_on - sig_off
    distance = duration*34000/2
    return distance

while True:
    try:
        cm = read_distance()
        print("distance=", int(cm), "cm")
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
