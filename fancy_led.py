import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Red   Vf= 2.0 If= 20mA    R= 65ohm using~68ohm | R=150ohm @5V supply
# Green Vf= 3.2 If= 20mA    R= 5ohm             | R=90                                                              ohm @5V supply
# Blue  Vf= 3.2 If= 20mA    R= 5ohm             | R=90ohm @5V supply

sequence = [
    [0,0,0],    #0 0 0 white
    [0,0,1],    #0 0 1 yellow
    [1,0,1],    #1 0 1 green
    [1,0,0],    #1 0 0 light blue
    [1,1,0],    #1 1 0 dark blue
    [0,1,0],    #0 1 0 violet
    [0,1,1]    #0 1 1 red    
]

ledRed = 18
ledGreen = 17
ledBlue = 22
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

GPIO.output(ledRed, 1)
GPIO.output(ledGreen,1)
GPIO.output(ledBlue,1)

for s in sequence:    
    red = s[0]
    green = s[1]
    blue = s[2]
    print(red, green, blue)
    GPIO.output(ledRed,red)
    GPIO.output(ledGreen,green)
    GPIO.output(ledBlue,blue)
    time.sleep(2)

for i in range(0,10):
    GPIO.output(ledRed,0)
    GPIO.output(ledGreen,0)
    GPIO.output(ledBlue,0)
    time.sleep(0.2)
    GPIO.output(ledRed,0)
    GPIO.output(ledGreen,1)
    GPIO.output(ledBlue,1)
    time.sleep(0.3)

GPIO.output(ledRed, 1)
GPIO.output(ledGreen,1)
GPIO.output(ledBlue,1)

GPIO.cleanup()
print('Done Fancy LED')

#R G B
#0 0 0 white
#0 0 1 yellow
#0 1 0 violet
#0 1 1 red
#1 0 0 light blue
#1 0 1 green
#1 1 0 dark blue
#1 1 1 off

