import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

matrix = [ 	[1,2,3,'A'],
		 	[4,5,6,'B'],
		 	[7,8,9,'C'],
		 	['*',0,'#','D'] ]

row = [4,17,27,22] #first 4 pins
col = [19,6,13,26] #last 4 pins

for j in range(4):
	print j
	GPIO.setup(col[j], GPIO.OUT)
	GPIO.output(col[j], 1)

for i in range(4):
	GPIO.setup(row[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
	while 1:
		### Put code here ###
		for j in range(4):
			GPIO.output(col[j], 0)

			for i in range(4):
				if GPIO.input(row[i]) == 0:
					print matrix[i][j]
					while(GPIO.input(row[i]) == 0):
						pass
					time.sleep(0.2)

			GPIO.output(col[j], 1)

except KeyboardInterrupt:
	GPIO.cleanup()
