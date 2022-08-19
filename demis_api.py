import pycurl
import json
from urllib.parse import urlencode
from io import BytesIO

def api(data, access_token):
  buffer = BytesIO()
  c = pycurl.Curl()
  #disable ssl verfication to run on localhost
  ##comment out if run as productive system
  c.setopt(pycurl.SSL_VERIFYPEER, 0)
  c.setopt(pycurl.SSL_VERIFYHOST, 0)
  ##
  c.setopt(pycurl.URL, 'https://localhost:7443/notification-api/fhir/$process-notification')
  c.setopt(pycurl.POST, 1)
  c.setopt(pycurl.POSTFIELDS, data)
  c.setopt(pycurl.HTTPHEADER, ['Authorization: Bearer ' + access_token,
                               'Content-Type: application/json'])
  c.setopt(c.WRITEDATA, buffer)
  c.perform()
  c.close()
  
  #buffer
  res = buffer.getvalue().decode('utf8').replace("'",'"')
  return res
