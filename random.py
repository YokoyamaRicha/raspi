import socket
import gripper
import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control
import random

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
    inspect()
    active()
    active()
    

def inspect():
    s.send(toBytes("movej([-3.63,-2.04,1.58,-1.73,-1.66,1.04], a=0.50, v=0.50)"+"\n"))
    time.sleep(4)

def active():
  a=random.randint(-3, 3)+random.randint(0,9)*0.1
  b=random.randint(-3, 3)+random.randint(0,9)*0.1
  print("[-3.63,-2.04,1.58,-1.73"+str(a)+str(b)+"]")
  s.send(toBytes("movej([-3.63,-2.04,1.58,-1.73,a,b], a=0.50, v=0.50)"+"\n"))
  time.sleep(3)
  

























if __name__ == '__main__':
    main()
    s.close()

