import psutil
import subprocess
from time import sleep
Victus_cmd = ['C:\\Users\\Alberto\\AppData\\Local\\Microsoft\\WindowsApps\\python3.exe', 'C:\\Users\\Alberto\\Documents\\python\\programas\\Victus\\main.py']
Proc_lst = []
while True:
    for p in psutil.process_iter():
        if p.name() == "python3.10.exe" and p.cmdline() == Victus_cmd:
            Proc_lst.append(p)
    if Proc_lst == []:
        subprocess.run(Victus_cmd, shell=True)
        Proc_lst = []