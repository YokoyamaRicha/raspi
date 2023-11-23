import os
import signal

def reap_zombie_processes():
    try:
        while True:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
            print(f"Zombie process {pid} terminated with status {status}")
    except ChildProcessError:
        print("OK")
    

if __name__ == '__main__':
    reap_zombie_processes()