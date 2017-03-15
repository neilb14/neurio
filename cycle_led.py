import time
from led import pi

# Red   Vf= 2.0 If= 20mA    R= 65ohm using~68ohm | R=150ohm @5V supply
# Green Vf= 3.2 If= 20mA    R= 5ohm             | R=90                                                              ohm @5V supply
# Blue  Vf= 3.2 If= 20mA    R= 5ohm             | R=90ohm @5V supply

sequence = ["white", "yellow", "green", "turquoise", "blue", "violet", "red"]
pi.show("off")
for colour in sequence:    
    pi.show(colour)
    time.sleep(2)

for i in range(0,10):
    pi.show("white")
    time.sleep(0.3)
    pi.show("red")
    time.sleep(0.3)

pi.show("off")
pi.cleanup()
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

