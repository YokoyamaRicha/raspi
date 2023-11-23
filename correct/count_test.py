import socket
import cv2       #for using OpenCV
#import numpy as np
import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control
#import sys
import multiprocessing as mp  #for using multiprocess
#from multiprocessing import Process
#HOST = "150.89.169.88"
#PORT = 30002

Tring = 27                    #set number
Echo = 18

GPIO.setwarnings(False)       #disregard warnings
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tring, GPIO.OUT)   #set pin27 out mode
GPIO.setup(Echo, GPIO.IN)     #set pin18 in mode

def toBytes(str):
    return bytes(str.encode())

def clear_q(q):
    _ = q.get()

def sensor(q):            #get distance func
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
        print(distance)
        if distance >30:
             q.put(1)            
        time.sleep(1)
           
def ur_cw():
    n=0
    while True:
        print(n)
        n += 1
        time.sleep(1)

def ur_ccw():
    n=100
    while True:
        print(n)
        n += 1
        time.sleep(1) 
  
if __name__ == '__main__':
    
    q = mp.Queue()
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((HOST, PORT))
    
    ps_s = mp.Process(target=sensor, args=(q,))    #set worker_1's task(dis)
 #   urcw = mp.Process(target=ur_cw)
 #   urccw = mp.Process(target=ur_ccw)
    '''
    ps_s.daemon = True
    urcw.daemon = True
    urccw.daemon = True
    '''    
    ps_s.start()
    #urcw.start()
    a=0
    while True:
        a+=1
        urcw = mp.Process(target=ur_cw)
        urcw.start()
        while True:
            if q.get()==1:       #show a hand
                urcw.terminate()
                urcw.join()
                break
        urccw = mp.Process(target=ur_ccw)
        urccw.start()
        clear_q(q)
        while True:
            if q.get()==1:       #show a hand
                urccw.terminate()
                urccw.join()
                break
        print("ok")
        if a==3:
            break
    print("finish")
    ps_s.terminate()
    ps_s.join()
