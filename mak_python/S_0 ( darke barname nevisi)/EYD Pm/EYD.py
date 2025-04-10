# -----Import necessary libraries for Send message from 'sms.ir'-----#

import http.client
import json

# -----Make variable for 'file path' & 'message'-----#

phonedata = "E:\WORK\MAKTABKHOONEH\mak_python\EYD Pm\phonelist.txt"
text = """سلام! نوروزتان پیروز!؟ 
"""
# -----Make Fanction for read phone numbers line by line from file-----#


def readphonelist(phonedata):
    with open(phonedata, "r") as file:
        content = file.readlines()

    content = [line.strip() for line in content]
    return content


phones = readphonelist(phonedata)

# -----Send bulk Message-----#

conn = http.client.HTTPSConnection("api.sms.ir")
payload = json.dumps(
    {
        "lineNumber": 30007732008904,
        "messageText": text,
        "mobiles": phones,
        "sendDateTime": None,
    }
)
headers = {
    "X-API-KEY": "EB6tfhzeRhIdyPtXQPhlyKIUGIwhAIcILLSJ7u7tdQBJAojE",
    "Content-Type": "application/json",
}
conn.request("POST", "/v1/send/bulk", payload, headers)
res = conn.getresponse()
data = res.read()

# -----monitoring-----#

print(data.decode("utf-8")[::-1])
