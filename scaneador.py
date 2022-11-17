# LIBRERIAS
import argparse
import scan_virus
import scan_img
import scan_pdf
import scan_process
#import scan_links
#import scan_ip
import json
import logging
import os
import pprint
# ------------------- ARCHIVO CONFIG --------------------
logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.DEBUG)
#------------------ARGUMENTOS DEL SCRIPT-------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("-ty", "-typ", "--Type",
                    help = "Usa este argumento para especificar que tipo de archivo sera escaneado", 
                    required=True, choices=['file', 'link', 'image', 'ip', 'pdf', 'process'])
parser.add_argument("-OuRo","-out", "--OutputRoute", 
                    help = "Usa este argumento para especificar donde sera guardado el archivo de+\
                      salida (SIN EL NOMBRE DEL ARCHIVO), Si no es especificado solo sera impreso en la pantalla", 
                    required=False, default = "print")
parser.add_argument("-OuFi", "-outfile", "--OutputFile", 
                    help = "Usa este argumento para especificar el nombre del archivo de salida +\
                      (SOLO EL NOMBRE DEL ARCHIVO); Para archivos de escaneo de ip se utilizara excel +\
                      por defecto, los demas seran guardados en archivos .json por defecto", 
                    required=False, default = "results.json")
parser.add_argument("-InRo", "-input1", "--InputRoute", 
                    help = "Usa este argumento para especificar la ruta del objeto a escanear +\
                      (Archivos, imagenes, links, pdfs, y procesos del equipo): En caso de querer escanear +\
                      procesos favor de introducir all (si lo deseado es escanear todos los procesos) ó +\
                      en su defecto el proceso especifico a escanear", 
                    required=True)
parser.add_argument("-key", "-llave", "--LlaveAPI", 
                    help = "Usa este argumento para introducir tu llave para la API", 
                    required=False)
args = parser.parse_args()   

if args.Type:
  typ = args.Type
if args.OutputRoute:
  out = args.OutputRoute
if args.OutputFile:
  outfile = args.OutputFile
if args.InputRoute:
  input1 = args.InputRoute
if args.LlaveAPI:
  #print(args.LlaveAPI)
  llave = args.LlaveAPI
else:
  llave='xx'
#-----------------VERIFICAR QUE EL ARCHIVO A ESCANEAR EXISTE----------
if typ == "file" or typ == "image" or typ == "pdf":
  filexist = os.path.exists(input1)
  if filexist == False:
    print("Ha ocurrido un error, se ha guardado esta exepcion en: error.log")
    logging.error('Error General: El archivo no existe')
    exit()
#-----------------VERIFICAR ARCHIVO DE SALIDA--------------------------  
def checkoutput():
  if out == "print":
    return("print")
  elif outfile.endswith(".json"):
    global jsonfile
    jsonfile = out + outfile
    return(jsonfile)
  elif outfile.endswith(".txt"):
    global txtfile
    txtfile = out + outfile
    return(txtfile)
  elif outfile.endswith(".xlsx") and typ == "ip":
    xlsxfile = out + outfile
    return(xlsxfile)
  else:
    print("Ha ocurrido un error, se ha guardado esta exepcion en: error.log")
    logging.error('Error General: Tipo de archivo de salida no compatible')
    exit()
#-------------CURSO DE ACCION EN CASO DE SER UN ARCHIVO CUALQUIERA---------------
if typ == "file":
  if llave=="xx":
    print("Se necesita ingresar llave del API")
    input("llave: ")
  resultadofile = scan_virus.scan_files(input1, llave)
  salida = checkoutput()
  if salida == "print":
    print(resultadofile)
  else:
    if salida.endswith(".json"):
      with open(salida, 'w') as file_object:
        for linea in resultadofile:
          dato={
            linea : resultadofile[linea]

          } 
          json.dump(dato, file_object, indent=4)
    elif salida.endswith(".txt"):
      with open (salida, "w") as file_object:
        for l in resultadofile:
          file_object.write(l+" : "+str(resultadofile[l])+"\n")
#-------------CURSO DE ACCION EN CASO DE SER UN LINK---------------
if typ == "link":
  if llave=="xx":
    #print(llave)
    print("Se necesita ingresar llave del API")
    input("llave: ")
  scan=scan_virus.scanlink(input1, llave)
  nombre = checkoutput()
  if nombre.endswith(".json"):
    with open (nombre,"w") as salida:
      for linea in scan:
        dato={
          linea : scan[linea]

        } 
        json.dump(dato, salida, indent=4)
  elif nombre.endswith(".txt"):
    with open (nombre, "w") as salida:
      for l in scan:
        salida.write(l+" : "+str(scan[l])+"\n")
  else:
    print(scan)   
#-------------CURSO DE ACCION EN CASO DE SER UNA IMAGEN---------------
if typ == "image":
  etiq = scan_img.scan_image(input1)
  nombre = checkoutput()
  if nombre == "print":
    print(etiq)
  elif nombre.endswith(".json"):
    with open(nombre, 'w') as file_object:
      for line in etiq:
        dato={
          line : str(etiq[line])
        }
        json.dump(dato, file_object, indent=4)
  else:
    f=open(nombre, "a+")
    for line in etiq:
      #f.write(" ".join(line) + "\n")
      f.write(line+" : "+str(etiq[line])+"\n")
    f.close()
#---------CURSO DE ACCION EN CASO DE SER UN ARCHIVO PDF---------------
if typ == "pdf":
  meta=scan_pdf.scanpdf(input1)
  nombre=checkoutput()
  if nombre.endswith(".json"):
    with open(nombre,"w") as salida:    
      for m in meta:
        linea=m+" : "+meta[m]
        json.dump(linea, salida)
  elif nombre.endswith(".txt"):
    with open(nombre,"w") as salida:    
      for m in meta:
        salida.write(m+" : "+meta[m])
  else:
    for m in meta:
      print(m+" : "+meta[m])
          
#--CURSO DE ACCION EN CASO DE QUERER ESCANEAR TODOS LOS PROCESOS-------
if typ == "process" and input1 == "all":
  nombre = checkoutput()
  etiq = scan_process.all_process(nombre)
  if nombre == "print":
    print(etiq)
#----------CURSO DE ACCION EN CASO DE QUERER ESCANEAR UN PROCESO--------
if typ == "process" and not input1 == "all":
  nombre = checkoutput()
  etiq = scan_process.single_process(input1, nombre)  
  if nombre == "print":
    print(etiq)
  
#-------CURSO DE ACCION EN CASO DE QUERER ESCANEAR PUERTOS DE UNA IP---------
'''if typ == "ip":
  scan_ip.scan_ip(input1)'''