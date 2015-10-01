import unirest
import json

message = raw_input("Enter the message :")
phone   = raw_input("Enter phone number :")

response = unirest.get("https://webaroo-send-message-v1.p.mashape.com/sendMessage?message="+message+"&phone="+phone,
  headers={
    "X-Mashape-Key": "Mashape API Key"
  }
)

#print response.status
#data = json.loads(response.raw_body)
#print data['response']['id']
