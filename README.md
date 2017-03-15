# Neurio
This is a little home energy indicator that is an awesome way to trim excess Watts off your energy consumption! Put an LED in a nice container and stick it in a visible area of your house to build more awareness about your home's energy consumption. It's a great reminder to shut things off and kill those phantom load powerbars before you leave the house or shut down for the night.

# The Details
These scripts are to drive a common anode RGB LED connected to a Raspberry Pi GPIO pins as follows: 
+ Red = 18
+ Green = 17
+ Blue = 22

The run.py script takes a power reading from a Neurio home energy monitor (IP must be supplied as a command line argument) and then shows the following colours on the LED:
+ 0-140W = White (140W because my "phantom load" is sitting at 142W and I want to shave off another couple of Watts!)
+ 141-250W = Turqoise
+ 251-500W = Yellow
+ 501-700W = Green
+ 701-1000W = Blue 
+ 1001-2000W = Violet 
+ 2001+ = Red (hopefully we're not here for very long!)

