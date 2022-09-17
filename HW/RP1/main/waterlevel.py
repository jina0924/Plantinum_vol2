  1 #import RPi.GPIO as GPIO
  2 #import time

  4 #GPIO.setwarnings(False)
  5 #GPIO.setmode(GPIO.BCM)
  6 #pin = 23
  7 #GPIO.setup(pin, GPIO.IN)

def waterlevel(pin):
    input = GPIO.input(pin)
    print(input)
    # 물 있으면 0, 없으면 1
    time.sleep(0.5)
