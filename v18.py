import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control
import serial
import binascii

ser = serial.Serial('COM6', 115200, timeout = 0.5)

GPIO.setwarnings(False)       #disregard warnings

#sensor
Tring = 27                    #set number
Echo = 18
sensor_sampling = 0.05
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tring, GPIO.OUT)   #set pin27 out mode
GPIO.setup(Echo, GPIO.IN)     #set pin18 in mode


#detect damage from jetson
cam_trg = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(cam_trg, GPIO.IN)

def sensor():            #get distance func
    while True:
        GPIO.output(Tring, GPIO.HIGH)       #Tring HIGH
        time.sleep(0.00001)                 #wait 10us
        GPIO.output(Tring, GPIO.LOW)        #Tring LOW
        
        while GPIO.input(Echo) == 0:        #time of Echo_LOW
            sig_off = time.time()
        while GPIO.input(Echo) == 1:        #time of Echo_HIGH
            sig_on = time.time()
            
        duration = sig_on - sig_off         #calculate duration
        distance = duration*34000/2         #(distance)calculate to [cm]
        return distance        

def main():
    while True:
        if GPIO.input(cam_trg) == 1:
            ser.write(1)
        elif sensor()>30:
            ser.write(2)
        else:
            None
        time.sleep(sensor_sampling = 0.05)

if __name__ == '__main__':
    main()

