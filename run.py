import sys,requests

if(len(sys.argv) < 2):
    raise IncorrectArgumentsException()

ip_address = sys.argv[1]
url = "http://{}/current-sample".format(ip_address)

response = requests.get(url)
if(response.status_code != 200):
    print("Error: response.code = ", response.status_code)
    raise InvalidResponseHttpStatusCode()

data = response.json()
for channel in data["channels"]:
    if(channel["type"] == "CONSUMPTION"):
        print(data["timestamp"], " ", channel["p_W"],"W")

