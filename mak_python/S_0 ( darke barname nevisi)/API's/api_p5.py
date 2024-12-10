#------import necessary library-----#  
import requests
import http.client
import json
#-----Using the 'jokeapi.dev' website API-----#
url = "https://v2.jokeapi.dev/joke/Programming/Any?format=json&lang=en&type=single&blacklistFlags=nsfw,racist,sexist"
response = requests.get(url)
#-----Extracting joke text from JSON-----#
joke = response.json()['joke']
print(joke)

#-----request with POST method from 'SMS.IR'-----#
conn = http.client.HTTPSConnection("api.sms.ir")
payload = json.dumps({
  "lineNumber": 30007732008904,
  "messageText": joke,
  "mobiles": [
    "09208575035",
    "09210522124"
  ],
  "sendDateTime": None
})
headers = {
  'X-API-KEY': 'EB6tfhzeRhIdyPtXQPhlyKIUGIwhAIcILLSJ7u7tdQBJAojE',
  'Content-Type': 'application/json'
}
conn.request("POST", "/v1/send/bulk", payload, headers)
res = conn.getresponse()
data = res.read()
#-----monitoring-----#
print(data.decode("utf-8"))