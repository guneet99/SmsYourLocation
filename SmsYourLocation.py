import urllib3
import json
from twilio.rest import Client
import requests
http = urllib3.PoolManager()
r = http.request('GET', 'http://ipinfo.io/json')
data = json.loads(r.data.decode('utf-8'))
city=data['city']
loc=data['loc']
print(city,loc)
SID="Twilio SID shows on your account's dashboard"
AUTH_TOKEN="Account's Auth Token available on your account's dashboard"
client = Client("SID", "AUTH_TOKEN")
client.messages.create(to="Receiver's Contact Number",
                       from_="Twilio's Purchased or alloted Number",
                       body="Hey,I am in "+city+" now and my locaton cordinates are " +loc)
