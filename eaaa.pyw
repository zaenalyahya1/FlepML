import tkinter as tk
import random
import threading
import time
from tkinter import messagebox
import os
import ctypes

def fake_bsod():
    bsod = tk.Tk()
    bsod.attributes("-fullscreen", True)
    bsod.configure(bg="blue")
    error_codes = [
        "CRITICAL_PROCESS_DIED",
        "MEMORY_MANAGEMENT",
        "SYSTEM_THREAD_EXCEPTION",
        "KERNEL_SECURITY_CHECK_FAIL URE",
    ]
    error_msg = f"""
    :( Your PC Ran Into A Problem and Need to Restart.
    ERROR Code : {random.choice(error_codes)}
    
    {random.randint(0, 100)} % Complate
    """
    
    label = tk.Label(bsod, text=error_msg, fg="white", bg="blue", font=("Arial", 24))
    label.pack(expand=True)
    bsod.after(300000, bsod.destory)
    bsod.mainloop()
    
def notifikasi_spam():
    fake_messages = [
        "VIRUS DETECTED! CLICK HARE TO REMOVE.",
        "YOUR SYSTEM IS COMPROMISED!",
        "WARNING: TROJAN VIRUS ACTIVITY DETECTED!",
        "CRITICAL UPDATE REQUIRED!",
        "YOUR FILES ARE BEING ENCRYTED.....",
    ]
    end_time = time.time() + 300 
    while time.time() < end_time:
        msg = random.choice(fake_messages)
        ctypes.windll.user32.MessageBoxW(0, msg, "SYSTEM ALERT", 0x30)
        time.sleep(random.randint(5, 15))
        
if __name__ == "__main__":
    threading.Thread(target=fake_bsod).start()
    threading.Thread(target=notifikasi_spam).start()