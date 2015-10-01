import unirest
import json 

def checker(number):
 response = unirest.get("https://dndcheck.p.mashape.com/index.php?mobilenos="+number,
  headers={
    "X-Mashape-Key": "Mashape Api Key","Accept": "application/json"
   }
 )
 value = json.loads(response.raw_body)
 #print value
 for jsonobj in value:
   print "DND STATUS :"+jsonobj['DND_status']
   if jsonobj['DND_status'] == 'on':
     print "ACTIVATION DATE is "+jsonobj['activation_date']

def main():
  numbers = raw_input("Enter the number seperated by , :")
  checker(numbers)

if __name__=="__main__":
	main()
