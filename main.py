import time.sleep as sleep 
import subprocess 
import RPi.GPIO as gpio
import time
import board
import adafruit_dht
import psutil

gpio.setwarnings(true)
gpio.setmode(gpio.BCM)

# motor pins
# r1,r2 right side motor terminals
# l1,l2 left side motor terminals


def dht():
	# https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi/

		# We first check if a libgpiod process is running. If yes, we kill it!
	for proc in psutil.process_iter():
	    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
		proc.kill()
	sensor = adafuit_dht.DHT11(board.D23)

	temp = sensor.temperature
	humidity = sensor.humidity
	##	print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
	except RuntimeError as error:
		print(error.args[0])
# time.sleep(2.0)
		continue
	except Exception as error:
		sensor.exit()
		raise error
	return humidity,temp

class  motor:
	def __init___(self,r1,r2,l1,l2):
		gpio.setup(r1,gpio.OUT)
		gpio.setup(r2,gpio.OUT)
		gpio.setup(l1,gpio.OUT)
		gpio.setup(l2,gpio.OUT)
		
		def forward(self,r1,r2):
			gpio.output(r1,gpio.HIGH)
			gpio.output(r2,gpio.LOW)
			gpio.output(l1,gpio.HIGH)
			gpio.output(l2,gpio.LOW)

		def backward(self,r1,r2):
			gpio.output(r1,gpio.LOW)
			gpio.output(r2,gpio.HIGH)
			gpio.output(l1,gpio.LOW)
			gpio.output(l2,gpio.HIGH)
			
		def right_turn(self,r1,r2):
			gpio.output(r1,gpio.HIGH)
			gpio.output(r2,gpio.LOW)
			gpio.output(l1,gpio.LOW)
			gpio.output(l2,gpio.HIGH)
			
		def left_turn(self,r1,r2):
			gpio.output(r1,gpio.LOW)
			gpio.output(r2,gpio.HIGH)
			gpio.output(l1,gpio.HIGH)
			gpio.output(l2,gpio.LOW)

class Dist:
	def __init__(self,trig,echo):
		self.trig = trig
		self.echo = echo


	def distance(self,trig,echo):
		GPIO.output(self.trig, True)

# set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(self.trig, False)

		StartTime = time.time()
		StopTime = time.time()

# save StartTime
		while GPIO.input(self.echo) == 0:
		StartTime = time.time()

# save time of arrival
		while GPIO.input(self.echo) == 1:
		StopTime = time.time()

# time difference between start and arrival
		TimeElapsed = StopTime - StartTime
# multiply with the sonic speed (34300 cm/s)
# and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2

		return distance

fl_ul = Dist.distance(tr,ech)
br_ul = Dist.distance(tr,ech)
ff_ul = Dist.distance(tr,ech)
bb_ul = Dist.distance(tr,ech)
fr_ul = Dist.distance(tr,ech)
bl_ul = Dist.distance(tr,ech)

min_dist = 50 

if min_dist > fl_ul:
	motor.right_turn()


elif  min_dist > fr_ul:
	motor.left_turn()
	
elif min_dist > fl_ul:
	motor.right_turn()
	
else  min_dist > fl_ul:
	motor.right_turn()

humidity,temp = dht();

print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
