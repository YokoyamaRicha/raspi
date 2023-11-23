import psutil

def find_zombie_processes():
    zombies = []
    
    for proc in psutil.process_iter(['pid', 'status']):
        if proc.status() == psutil.STATUS_ZOMBIE:
            zombies.append(proc)
            
    return zombies

if __name__ == '__main__':
    zombie_processes = find_zombie_processes()
    
    if zombie_processes:
        print("Zombie processes found:")
        for proc in zombie_processes:
            print(f"PID: {proc.pid}")
    else:
        print("No zombie processes found.")
#import cv2
#cv2.__version__
