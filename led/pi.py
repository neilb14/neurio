import RPi.GPIO as GPIO

colours = {
    "off":[1,1,1],
    "white":[0,0,0],
    "yellow":[0,0,1],
    "green":[1,0,1],
    "turquoise":[1,0,0],
    "blue":[1,1,0],
    "violet":[0,1,0],
    "red":[0,1,1]
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledRed = 22
ledGreen = 18
ledBlue = 17

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

def show(name):
    colour = colours[name]
    red = colour[0]
    green = colour[1]
    blue = colour[2]
    GPIO.output(ledRed,red)
    GPIO.output(ledGreen,green)
    GPIO.output(ledBlue,blue)

def cleanup():
    GPIO.cleanup()
