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
rtde_c.moveJ([-4.127537790928976, -1.736793657342428, -1.5042853355407715, -1.4608700585416337, 1.5471107959747314, 0.7400461435317993, 1.0, 0.1, True])
rControl_sleep()
