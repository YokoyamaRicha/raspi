import socket
import gripper
import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control
import numpy as np

HOST = "150.89.169.116"
PORT = 30002

Tring = 27                    #set number
Echo = 18

senser_sampling = 0.1
 
values = [1, 1, 1]
epsilon = 0.4        # 探索率(epsilon)

GPIO.setwarnings(False)       #disregard warnings
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tring, GPIO.OUT)   #set pin27 out mode
GPIO.setup(Echo, GPIO.IN)     #set pin18 in mode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
g = gripper.RobotiqGripper()
g.connect(HOST, 63352)
g.activate()

damage = 0

def main():
    while True:
        home()
        time.sleep(1)
        g.move_and_wait_for_pos(255, 255, 255)
        move()
        time.sleep(1)
        selected_action = epsilon_greedy_selection(epsilon, values)  #e
        
        
        if selected_action == 0:
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.50,1.00], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage == 1:
                values[0]+=1      #reward
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.70,2.26], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage ==1:
                values[1]+=1
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.00,2.26], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage ==1:
                values[2]+=1
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
                
                
        if selected_action == 1:
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.70,2.26], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage == 1:
                values[1]+=1      #reward
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.00,2.26], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage ==1:
                values[2]+=1
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.50,1.00], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage ==1:
                values[0]+=1
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
                
                
        if selected_action == 2:
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.00,2.26], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage == 1:
                values[2]+=1      #reward
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.50,1.00], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage ==1:
                values[0]+=1
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.70,2.26], a=0.50, v=0.50)"+"\n"))
            time.sleep(4)
            if damage ==1:
                values[1]+=1
                NG_box()
                g.move_and_wait_for_pos(0, 255, 255)
                break
            
        OK_box()
        g.move_and_wait_for_pos(0, 255, 255)






def log_info(g):
    print(f"Pos: {str(g.get_current_position()): >3} "
          f"Open: {g.is_open(): <2} "
          f"Closed: {g.is_closed(): <2} ")

def epsilon_greedy_selection(epsilon, values):
    """
        epsilon-greedy 行動選択
    """
    nb_values = len(values)
    if np.random.uniform() < epsilon:   # 探索(epsilonの確率で)
        action = np.random.randint(0, nb_values)
    else:                               # 知識利用(1-epsilonの確率で)
        action = np.argmax(values)

    return action
    
def toBytes(str):
    return bytes(str.encode())

def home():
        s.send(toBytes("movej([-2.47,-1.73,-1.28,-1.64,1.50,0.57], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        s.send(toBytes("movej([-2.05,-1.73,-1.28,-1.64,1.50,0.57], a=0.50, v=0.50)"+"\n"))
        time.sleep(3)
        s.send(toBytes("movej([-2.07,-1.85,-1.31,-1.52,1.50,0.57], a=0.50, v=0.50)"+"\n"))
        time.sleep(2)
        
def move():
        s.send(toBytes("movej([-2.05,-1.73,-1.28,-1.64,1.50,0.57], a=0.50, v=0.50)"+"\n"))
        time.sleep(2)
        s.send(toBytes("movej([-2.74,-1.48,-1.29,-1.64,1.50,1.00], a=0.50, v=0.50)"+"\n"))
        time.sleep(3)
        s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.33,1.50,2.26], a=0.50, v=0.50)"+"\n"))
        time.sleep(3)
        
def OK_box():
    s.send(toBytes("movej([-3.05,-1.79,-1.28,-1.57,1.60,2.25], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)
    
def NG_box():
    s.send(toBytes("movej([-2.42,-1.79,-1.28,-1.57,1.60,2.25], a=0.50, v=0.50)"+"\n"))
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
    s.send(toBytes("movej([-2.74,-1.48,-1.29,-0.34,1.50,0.76], a=0.50, v=0.50, t=8)"+"\n"))
    while True:
        if sensor()>30:
            break
        else:
            None
        time.sleep(senser_sampling)

    s.send(toBytes("movej([-2.74,-1.48,-1.28,-0.34,1.50,2.26], a=0.50, v=0.50, t=8)"+"\n"))
    while True:
        if sensor()<30:
            break
        else:
            None
        time.sleep(senser_sampling)

    while True:
        if sensor()>30:
            break
        else:
            None
        time.sleep(senser_sampling)

if __name__ == '__main__':
    main()
    s.close()