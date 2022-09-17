import RPi.GPIO as GPIO

led = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

while 1:
    GPIO.output(led,True)
