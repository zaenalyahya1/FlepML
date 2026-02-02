import tkinter as tk
import random
import time
import ctypes
import os
import threading
from PIL import Image, ImageTk
from ctypes import wintypes

def fake_bsod():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="#0078D7")
    
    error_text = """
    :( PC Anda Mengalami Masalah dan Perlu Restart.
    Kami Hanya Mengumpulkan Beberapa Info Kesalahan Lalu Anda bisa Restart.
    (0% selasai)
    
    STOP CODE: CRITICAL_PROCESS_DIED 
    """
    
    label = tk.Label(
        root,
        text=error_text,
        fg="white",
        bg="#0078D7",
        font=("Segoe UI", 24),
        justify="left"
    )
    label.pack(expand=True)
    root.after(120000, root.destroy)
    root.mainloop()
    
def screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    
    canvas = tk.Canvas(root, bg="black")
    canvas.pack(fill="both", expand=True)
    
    def draw():
        for _ in range(50):
            x1 = random.randint(0, root.winfo_screenwidth())
            y1 = random.randint(0, root.winfo_screenheight())
            x2 = random.randint(0, root.winfo_screenwidth())
            y2 = random.randint(0, root.winfo_screenheight())
            
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            canvas.create_line(x1, y1, x2, y2, fill=color, width=3)
        
        root.after(100, draw)
    draw()
    root.after(120000, root.destroy)
    root.mainloop()

def main():
    threading.Thread(target=fake_bsod).start()
    threading.Thread(target=screen).start()
    time.sleep(120)
    os.system("taskill /f /im pythonw.exe")

if __name__ == "__main__":
    main()