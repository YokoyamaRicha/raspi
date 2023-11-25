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
        s.send(toBytes("movej([-3.63,-2.04,1.58,-1.73,-1.66,1.04], a=0.50, v=0.50)"+"\n"))
        time.sleep(4)
        b+=1


if __name__ == '__main__':
    main()
    s.close()
