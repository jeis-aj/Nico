import time.sleep as sleep 
import RPi.GPIO as gpio


#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# motor pins
# r1,r2 right side motor terminals
# l1,l2 left side motor terminals

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



def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

gpio.setwarnings(true)
gpio.setmode(gpio.BCM)

