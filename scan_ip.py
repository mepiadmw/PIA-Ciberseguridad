import nmap
import main
import xlsxwriter
nmScan = nmap.PortScanner()

def scan_ip(host):
  nombre = main.checkoutput()
  if nombre == "print":
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
    for proto in nmScan[host].all_protocols():
      print('----------')
      print('Protocol : %s' % proto)
      lport = nmScan[host][proto].keys()
      lport.sort()
      for port in lport:
        print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
  elif nombre.endswith(".xlsx"):
    workbook = xlsxwriter.Workbook(nombre)
    for proto in nmScan[host].all_protocols():
      fila = 2
      worksheet = workbook.add_worksheet(proto)
      worksheet.write(1, 1, "Anfitrion")
      worksheet.write(1, 2, "Protocolo")
      worksheet.write(1, 3, "Puerto")
      worksheet.write(1, 4, "Estado")
      worksheet.write(2, 1, nmScan[host].hostname())
      worksheet.write(2, 2, proto)
      lport = nmScan[host][proto].keys()
      lport.sort()
      for port in lport:
        worksheet.write(fila, 3, port)
        worksheet.write(fila, 4, nmScan[host][proto][port]['state'])
        fila += 1