from virus_total_apis import PublicApi
from hashlib import md5

# Create dictionary containing the file to send for multipart encoding upload

def scan_files(input2, key):
  client=PublicApi(key)
  with open(input2, "rb") as file:
    fhash = md5(file.read()).hexdigest()
  status=client.get_file_report(fhash)
  return status

def scanlink(input2, llave):
 
  client=PublicApi(llave)
  status=client.get_url_report(input2)
  return status
