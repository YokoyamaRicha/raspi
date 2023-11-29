import rtde_control
import time

robotIP = "150.89.169.193"  #自分のURのIPアドレスに変更
rtde_c = rtde_control.RTDEControlInterface(robotIP)#送信用

def rControl_sleep():   #URが完全に止まるまで次のプログラムに移行しない設定
    print("Start of movement...")
    while True:
        time.sleep(0.5)
        if rtde_c.isSteady() == True:
            break 
    print("End of movement!")

#例えば
rtde_c.moveJ([-3.63, -2.04, 1.58, -1.73, -1.66, 1.04, 1.0, 0.1, True])
rControl_sleep()
