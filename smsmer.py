import unirest
import json
import sys
import dndchecker

to  = raw_input("Enter the Phone number :")
print "Checking if dnd activated or not"
dndchecker.checker(to)
msg = raw_input("Enter the message :")
response = unirest.get("https://freesms8.p.mashape.com/index.php?msg="+msg+"&phone="+to+"&pwd=fullonlinesms_password&uid=fullonlinesms_password",
  headers={
    "X-Mashape-Key": "Mashape API KEY"
  }
)

print response.code
#print response.raw_body
if response.raw_body == 'invalid login':
  print "Invalid Login detail"
  sys.exit()
data = json.loads(response.raw_body)
print data['response']
