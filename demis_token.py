import pycurl
from urllib.parse import urlencode
from io import BytesIO
import json

def token_generation():
  buffer = BytesIO()
  c = pycurl.Curl()
  #initializing the request URL
  c.setopt(c.URL, 'https://localhost:7443/auth/realms/LAB/protocol/openid-connect/token')
  #the data that we need to Post
  post_data = {
    'grant_type' : 'password',
    'client_id': 'demis-adapter',
    'client_secret': 'secret_client_secret',
    'username' : 'test-lab999'
  }
  # encoding the string to be used as a query
  postfields = urlencode(post_data)
  #setting the cURL for POST operation
  c.setopt(c.POSTFIELDS, postfields)
  #disable SSL verification to run on localhost
  ##comment out if run on productive system!
  c.setopt(pycurl.SSL_VERIFYPEER, 0)
  c.setopt(pycurl.SSL_VERIFYHOST, 0)
  ##
  c.setopt(c.WRITEDATA, buffer)
  c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded'])
  #set key and cert
  c.setopt(c.SSLKEY, "key.pem")
  c.setopt(c.SSLCERT, "cert.pem")
  # perform file transfer
  c.perform()
  #Ending the session and freeing the resources
  c.close()
  #return result
  body = buffer.getvalue()
  #print(body)
  body.decode('iso-8859-1')
  myjson = body.decode('utf8').replace("'",'"')
  token_response = json.loads(myjson)
  return token_response
