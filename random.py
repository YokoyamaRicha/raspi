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
  r=random.randint(1, 13)+random.randint(0,9)*0.1
  if r==1:
    s.send(toBytes("movej([-4.35,-2.60,2.15,-2.10,-0.86,0.87], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==2:
    s.send(toBytes("movej([-3.37,-1.16,0.39,-0.54,-2.00,1.22], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==3:
    s.send(toBytes("movej([-4.29,-1.99,1.45,-1.14,-0.92,0.59], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==4:
    s.send(toBytes("movej([-4.19,-1.56,0.93,-0.61,-1.02,-0.26], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==5:
    s.send(toBytes("movej([-4.66,-1.81,1.60,-0.26,-0.59,-1.56], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==6:
    s.send(toBytes("movej([-5.08,-2.37,1.85,-0.08,-0.47,-1.42], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==7:
    s.send(toBytes("movej([-3.71,-1.61 0.95 -1.04 -1.56 1.33], a=0.50, v=0.50)"+"\n"))'
    time.sleep(3)
  if r==8:
    s.send(toBytes("movej([-3.81,-1.49,0.78,-0.84,-1.44,-0.41], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==9:
    s.send(toBytes("movej([-3.41,-1.95,1.53,-1.69,-1.94, 0.81], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==10:
    s.send(toBytes("movej([-3.29,-1.31,0.68,-0.73,-2.11,0.90] a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==
    s.send(toBytes("movej([-3.12,-1.34,0.90,-0.71,-2.38,1.24], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==12:
    s.send(toBytes("movej([-4.54,-1.97,1.51,-0.75,-0.68,-0.85], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  if r==13:
    s.send(toBytes("movej([-3.96,-2.35,1.94,-2.05,-1.27,0.04], a=0.50, v=0.50)"+"\n"))
    time.sleep(3)
  

























if __name__ == '__main__':
    main()
    s.close()

