import socket
import gripper
import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control

HOST = "150.89.169.116"
PORT = 30002

Tring = 27                    #set number
Echo = 18

cam_trg = 26

senser_sampling = 0.05


GPIO.setwarnings(False)       #disregard warnings
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tring, GPIO.OUT)   #set pin27 out mode
GPIO.setup(Echo, GPIO.IN)     #set pin18 in mode

GPIO.setmode(GPIO.BCM)
GPIO.setup(cam_trg, GPIO.IN)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
g = gripper.RobotiqGripper()
g.connect(HOST, 63352)
g.activate()
    
def main():
    while True:
        home()
        time.sleep(2)
        grip()
        time.sleep(1)
        g.move_and_wait_for_pos(165, 255, 220)
        home()
        inspect()
        time.sleep(1)
        ur = ur_cw()
        if ur==1:
            NG_box()
            g.move_and_wait_for_pos(0, 255, 255)
            time.sleep(3)
            inspect()
        else:
            OK_box()
            g.move_and_wait_for_pos(0, 255, 255)
            time.sleep(3)
            inspect()

def log_info(g):
    print(f"Pos: {str(g.get_current_position()): >3} "
          f"Open: {g.is_open(): <2} "
          f"Closed: {g.is_closed(): <2} ")
    
def toBytes(str):
    return bytes(str.encode())

def home():
    s.send(toBytes("movej([-4.77,-2.06,1.44,-1.01,-1.62,1.46], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)
        
def grip():
    s.send(toBytes("movej([-4.77,-1.87,2.32,-2.07,-1.62,1.46], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)

def inspect():
    s.send(toBytes("movej([-3.63,-2.04,1.58,-1.73,-1.66,1.04], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)
    
def OK_box():
    s.send(toBytes("movej([-3.45,-1.10,1.44,-1.91,-1.59,1.25], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)
    
def NG_box():
    s.send(toBytes("movej([-3.07,-1.10,1.44,-1.91,-1.59,1.66], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)
        
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
           
def ur_cw():
    ur_state = 1
    s.send(toBytes("movej([-3.63,-2.04,1.58,-1.73,-1.66,-0.46], a=0.50, v=0.50, t=8)"+"\n"))
    while True:
        if GPIO.input(cam_trg) == 1:
            ur_state = 0
            break            
        elif sensor()>30:
            break
        else:
            None
        time.sleep(senser_sampling)

    s.send(toBytes("movej([-3.63,-2.04,1.58,-1.73,-1.66,1.04], a=0.50, v=0.50, t=8)"+"\n"))
    while (ur_state == 1):
        if GPIO.input(cam_trg) == 1:
            ur_state = 0
            break 
        elif sensor()<30:
            break
        else:
            None
        time.sleep(senser_sampling)

    while (ur_state == 1):
        if GPIO.input(cam_trg) == 1:
            ur_state = 0
            break 
        elif sensor()>30:
            break
        else:
            None
        time.sleep(senser_sampling)
    return ur_state

if __name__ == '__main__':
    main()
    s.close()
