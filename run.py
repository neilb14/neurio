import sys,requests

steps = [0,140,250,500,700,1000,2000]

if(len(sys.argv) < 2):
    raise IncorrectArgumentsException()

ip_address = sys.argv[1]
url = "http://{}/current-sample".format(ip_address)

def find_step(power):
    for i, value in enumerate(steps):
        if(value >= power):
            return i

response = requests.get(url)
if(response.status_code != 200):
    print("Error: response.code = ", response.status_code)
    raise InvalidResponseHttpStatusCode()

data = response.json()
for channel in data["channels"]:
    if(channel["type"] == "CONSUMPTION"):
        power = float(channel["p_W"])
        print("[{}] {}W ({})".format(data["timestamp"], power,find_step(power)))

