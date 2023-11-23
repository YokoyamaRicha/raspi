import socket
import time

HOST = "150.89.169.106"
PORT = 30002

def toBytes(str):
    return bytes(str.encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    p_command="stop\n"
    s.send(toBytes("movej([-2.47,-1.73,-1.28,-1.64,1.50,-1.70], a=1.40, v=1.04)"+"\n"))
    time.sleep(2)
    s.send(p_command.encode())
    
    
    data=s.recv(1024)
    s.close()
    print("Receved", repr(data))
    print("Program finish")
    
if __name__=='__main__':
    main()