from PIL import Image
from PIL.ExifTags import TAGS
 
def scan_image(imagen):
  image = Image.open(imagen)
  exifdata = image.getexif()
  etiq = {}
  for tagid in exifdata:
    tagname = TAGS.get(tagid, tagid)
    value = exifdata.get(tagid)
    etiq[tagname]=value
    #etiq = etiq.append(f"{tagname:25}: {value}")
  return(etiq)