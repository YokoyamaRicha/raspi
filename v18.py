import RPi.GPIO as GPIO   #for using GPIO 
import time      #time control

GPIO.setwarnings(False)       #disregard warnings

#sensor
Tring = 27                    #set number
Echo = 18
senser_sampling = 0.05
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tring, GPIO.OUT)   #set pin27 out mode
GPIO.setup(Echo, GPIO.IN)     #set pin18 in mode


#detect damage from jetson
cam_trg = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(cam_trg, GPIO.IN)

    
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

