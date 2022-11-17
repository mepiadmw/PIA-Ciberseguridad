import subprocess
import logging

logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.DEBUG)

def all_process(salida):
    if salida.endswith(".json") or salida.endswith(".txt"):
        process = "powershell -Executionpolicy ByPass -Command Get-Process | Format-Table | Out-File "+salida
    else:
        process = "powershell -Executionpolicy ByPass -Command Get-Process | Format-Table"    
    runningProcesses = subprocess.check_output(process)
    return(runningProcesses.decode())
def single_process(name, salida):
    try:
        if salida.endswith(".json") or salida.endswith(".txt"):
            process = "powershell -Executionpolicy ByPass -Command Get-Process -Name "+name+" | Format-Table | Out-File "+salida
            
        else:
            process = "powershell -Executionpolicy ByPass -Command Get-Process -Name "+name+" | Format-Table"
        runningProcesses = subprocess.check_output(process)
        return(runningProcesses.decode())
    except:
      logging.error('Error de escaneo de Proceso: El proceso no existe o no se esta ejecutando')
      return("El proceso no existe o no se esta ejecutando")