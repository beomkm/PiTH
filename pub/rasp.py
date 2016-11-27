import RPi.GPIO as GPIO
import dht11
import time
import datetime
import threading

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(5, GPIO.OUT) #2
GPIO.setup(6, GPIO.OUT) #5
GPIO.setup(13, GPIO.OUT) #1
GPIO.setup(19, GPIO.OUT) #3
GPIO.setup(26, GPIO.OUT) #4
GPIO.setup(12, GPIO.OUT) #6
GPIO.setup(16, GPIO.OUT) #9
GPIO.setup(20, GPIO.OUT) #7
GPIO.setup(21, GPIO.OUT) #8

map = {}
map[1] = 13
map[2] = 5
map[3] = 19
map[4] = 26
map[5] = 6
map[6] = 12
map[7] = 20
map[8] = 21
map[9] = 16

seg = [[1,4,3,8,7,6],[3,8],[4,3,9,6,7],
	[4,3,9,8,7],[1,9,3,8],[4,1,9,8,7],
	[4,1,9,8,7,6], [1,4,3,8],
	[4,1,3,9,6,7,8],[1,4,3,9,8,7]]


def printNum(digit, num):

	for i in range(1, 10):
		if(i == 2 and i == 5):
			GPIO.output(map[i], False)
		else:
			GPIO.output(map[i], True)


	if(digit == 0):
		GPIO.output(map[2], True)
		GPIO.output(map[5], False)
	else:
		GPIO.output(map[2], False)
		GPIO.output(map[5], True)

	for i in range(len(seg[num])):
		GPIO.output(map[seg[num][i]], False)
	
num = 0
tFlag = 1

def handler():
	while tFlag:
		printNum(0, num/10%10)
		time.sleep(0.01)
		printNum(1, num%10)
		time.sleep(0.01)


th = threading.Thread(target=handler)
th.start()


	
# read data using pin 17
instance = dht11.DHT11(pin = 17)

try:
	while True:
		result = instance.read()
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %d C" % result.temperature)
			num = result.temperature
			print("Humidity: %d %%" % result.humidity)

		time.sleep(0.5)

except KeyboardInterrupt:
	tFlag = 0
	th.join()
	GPIO.cleanup()


