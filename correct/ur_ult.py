import socket
import cv2       #for using OpenCV
import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control
import multiprocessing as mp  #for using multiprocess

HOST = "150.89.169.116"
PORT = 30002

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
        if distance <10:
             q.put(1)            
        time.sleep(0.5)
           
def ur_cw(q):
    s.send(toBytes("movej([-2.47,-1.73,-1.28,-1.64,1.50,1.70], a=0.50, v=0.50, t=8)"+"\n"))
    for n in range(50):
        if q.get()==1:
            s.send(p_command.encode())                
            break
        else:
            None
        time.sleep(0.1)
    #clear_q(q)
    #time.sleep(2)
    s.send(toBytes("movej([-2.47,-1.73,-1.28,-1.64,1.50,-1.70], a=0.50, v=0.50, t=8)"+"\n"))
    for n in range(50):
        if q.get()==1:
            s.send(p_command.encode())
            break
        else:
            None
        time.sleep(0.1)
    #clear_q(q)

if __name__ == '__main__':
    
    q = mp.Queue()
    #q2 =mp.Queue()
    ps_s = mp.Process(target=sensor, args=(q,))    #set worker_1's task(dis)
    ps_s.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    p_command="stop\n"
    s.send(toBytes("movej([-2.47,-1.73,-1.28,-1.64,1.50,0.00], a=1.40, v=1.04)"+"\n"))
    time.sleep(2)
    s.send(p_command.encode())
    print("stop")
    #stopj(2)
    #time.sleep(2)
#     ps_s = mp.Process(target=sensor, args=(q,))    #set worker_1's task(dis)
    #urcw = mp.Process(target=ur_cw, args=(q,))
    #urccw = mp.Process(target=ur_ccw, args=(q,))
    '''
    ps_s.daemon = True
    urcw.daemon = True
    urccw.daemon = True
    '''    
#     ps_s.start()
    #urcw.start()
    a=0
    while True:
        a+=1
        #s.send(toBytes("movej([-2.47,-1.73,-1.28,-1.64,1.50,1.20], a=1.40, v=1.04)"+"\n"))
        #time.sleep(2)
        urcw = mp.Process(target=ur_cw, args=(q,))
        urcw.start() 
        urcw.join()
        urcw.terminate()
        #time.sleep(2)
        if a==5:
            break
    print("finish")
    ps_s.terminate()
    #ps_s.join()
    s.close()
