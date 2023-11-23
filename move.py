import socket
import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control

HOST = "150.89.169.116"
PORT = 30002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
    
def toBytes(str):
    return bytes(str.encode())

def main():
    b=0
    while b<3:
        s.send(toBytes("movej([-1.80,-1.08,-2.23,-1.39,1.61,0.62], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        s.send(toBytes("movej([-1.01,-1.08,-2.23,-1.36,1.60,0.62], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        s.send(toBytes("movej([-1.01,-1.15,-2.37,-1.17,1.63,0.62], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        #gripper close
        s.send(toBytes("movej([-2.10,-1.20,-1.87,-1.16,1.45,0.62], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        s.send(toBytes("movej([-3.06,-1.72,-1.85,-1.04,1.57,1.11], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        #open
        s.send(toBytes("movej([-2.54,-1.72,-1.85,-1.04,1.57,1.11], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        #open
        b+=1


if __name__ == '__main__':
    main()
    s.close()
