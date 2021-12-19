import gpiozero
import subprocess 
import RPi.GPIO as gpio
import time
import Adafruit_DHT
import psutil

gpio.cleanup()
gpio.setwarnings(True)
gpio.setmode(gpio.BCM)

# gpio setmode 

gpio_out_list = [2,17,10,0,6,19]
gpio_in_list = [3,27,9,5,13,26]

for i in range(6):
	gpio.setup(gpio_out_list[i],gpio.OUT)
	gpio.setup(gpio_in_list[i],gpio.IN)

gpio.setup(15,gpio.OUT)
# motor pins
# r1,r2 right side motor terminals
# l1,l2 left side motor terminals


def dht():
# https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi/

		# We first check if a libgpiod process is running. If yes, we kill it!
	for proc in psutil.process_iter():
		if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
			proc.kill()
	sensor = adafuit_dht.DHT11(16)

	temp = sensor.temperature
	humidity = sensor.humidity
##	print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
# 	except RuntimeError as error:
#		print(error.args[0])
## time.sleep(2.0)
#		continue
#	except Exception as error:
#		sensor.exit()
#		raise error
	return humidity,temp

class  motor:
	def __init___(self,r1,r2,l1,l2):
                self.r1 = r1
                self.r2 = r2
                self.l1 = l1 
                self.l2 = l2
		gpio.setup(self.r1,gpio.OUT)
		gpio.setup(self.r2,gpio.OUT)
		gpio.setup(self.l1,gpio.OUT)
		gpio.setup(self.l2,gpio.OUT)
		
		def forward(self,r1,r2):
			gpio.output(self.r1,gpio.HIGH)
			gpio.output(self.r2,gpio.LOW)
			gpio.output(self.l1,gpio.HIGH)
			gpio.output(self.l2,gpio.LOW)

		def backward(self,r1,r2):
			gpio.output(self.r1,gpio.LOW)
			gpio.output(self.r2,gpio.HIGH)
			gpio.output(self.l1,gpio.LOW)
			gpio.output(self.l2,gpio.HIGH)
			
		def right_turn(self,r1,r2):
			gpio.output(self.r1,gpio.HIGH)
			gpio.output(self.r2,gpio.LOW)
			gpio.output(self.l1,gpio.LOW)
			gpio.output(self.l2,gpio.HIGH)
			
		def left_turn(self,r1,r2):
			gpio.output(self.r1,gpio.LOW)
			gpio.output(self.r2,gpio.HIGH)
			gpio.output(self.l1,gpio.HIGH)
			gpio.output(self.l2,gpio.LOW)
# 
# class Dist:
# 	def __init__(self,trig,echo):
# 		self.trig = trig
# 		self.echo = echo
# 
# 
# 	def distance(self):
# 		gpio.output(self.trig, True)
# 
# # set Trigger after 0.01ms to LOW
# 		time.sleep(0.00001)
# 		gpio.output(self.trig,True )
# 
# 		StartTime = time.time()
# 		StopTime = time.time()
# 
# # save StartTime
# 		while gpio.input(self.echo) == 0:
# 			StartTime = time.time()
# 
# # save time of arrival
# 		while gpio.input(self.echo) == 1:
# 			StopTime = time.time()
# 
# # time difference between start and arrival
# 		TimeElapsed = StopTime - StartTime
# # multiply with the sonic speed (34300 cm/s)
# # and divide by 2, because there and back
# 		distance = (TimeElapsed * 34300) / 2
# 
# 		return distance
	


# fr_ul = gpiozero.DistanceSensor(2,3)
fl_ul = gpiozero.DistanceSensor(17,27)
ff_ul = gpiozero.DistanceSensor(10,9)
br_ul = gpiozero.DistanceSensor(0,5)
bb_ul = gpiozero.DistanceSensor(6,13)
bl_ul = gpiozero.DistanceSensor(19,26)



drive  = motor(20,21,7,1)

def loop():

		
	min_dist = 50 

	if min_dist > fl_ul:
		motor.right_turn()


	elif  min_dist > fr_ul:
		motor.left_turn()
		
	elif min_dist > fl_ul:
		motor.right_turn()
		
	else  :
		motor.right_turn()

	humidity,temp = dht();

	print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
print("fn")
while True:
        
	print("in loop")	
	time.sleep(2)
        # gpio.output(15,gpio.HIGH)
        drive.forward()
	time.sleep(2)
	print("fl-end")



