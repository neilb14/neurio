import os,sys,time,requests

if(os.uname()[4][:3] == "arm"):
    from led import pi
    led = pi
else:
    from led import fake
    led = fake

sequence = ["off","white","yellow","green","turquoise","blue","violet","red"]
steps = [0,140,250,500,700,1000,2000]

if(len(sys.argv) < 2):
    raise IncorrectArgumentsException()

ip_address = sys.argv[1]
url = "http://{}/current-sample".format(ip_address)

def find_colour(power):
    for i, value in enumerate(steps):
        if(value >= power):
            return sequence[i]
    return sequence[-1]

response = requests.get(url)
if(response.status_code != 200):
    print("Error: response.code = ", response.status_code)
    raise InvalidResponseHttpStatusCode()

data = response.json()
for channel in data["channels"]:
    if(channel["type"] == "CONSUMPTION"):
        power = float(channel["p_W"])
        colour = find_colour(power)
        print("[{}] {}W ({})".format(data["timestamp"], power,colour))
        led.show(colour)

