import RPi.GPIO as GPIO
import datetime
import time
import spidev
import Adafruit_DHT

# temp_timer
t = 0

#humSensor init
humSensor = Adafruit_DHT.DHT11
humSensor_pin = 23

#WaterLevel Sensor init
waterLevel_pin = 24

#Motor Drive pin
A1A = 5
A1B = 6

# THRESHOLD setting
HUM_THRESHOLD = 20
HUM_MAX = 0

#spi init
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000

#GPIO init
def init():
	#MOTOR DRIVE GPIO SETTING
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(A1A, GPIO.OUT)
	GPIO.output(A1A, GPIO.LOW)
	GPIO.setup(A1B, GPIO.OUT)
	GPIO.output(A1B, GPIO.LOW)

	#WATERLEVEL Sensor GPIO Setting
	GPIO.setwarnings(False)
	
	#LED GPIO Setting
	GPIO.setup(2, GPIO.OUT)
	GPIO.setup(3, GPIO.OUT)
	GPIO.output(2, GPIO.LOW)
	GPIO.output(3, GPIO.LOW)

	#WaterLevel Sensor GPIO Setting
	GPIO.setup(waterLevel_pin, GPIO.IN)

#Soil_Hum_Sensor code
def read_spi_adc(adcChannel):
	adcValue=0
	buff=spi.xfer2([1,(8+adcChannel)<<4,0])
	adcValue = ((buff[1]&3)<<8)+buff[2]
	return adcValue

# Mapping 0 to 100  with  Analog Sensor Value
def map(value, min_adc, max_adc, min_hum, max_hum):
	adc_range = max_adc-min_adc
	hum_range = max_hum - min_hum
	scale_factor = float(adc_range)/float(hum_range)
	return value/scale_factor

# HumidTemp Sensor Function
#def humidTemp():
#	humidity, temperature = Adafruit_DHT.read_retry(humSensor, humSensor_pin)
#	now = time.localtime()

#    if humidity is not None and temperature is not None:
#		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
#		print ("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

#    else:
#		print('HumidTemp Sensor Error!')


def waterlevel(pin):
	ret = GPIO.input(pin)
	print(ret)

	return ret

#Main Code
try:
	init()
	adcChannel = 0
	while True:
		adcValue = read_spi_adc(adcChannel)
		
		hum = int(map(adcValue, HUM_MAX, 1023, 0, 100))
		now_hum = 100 - hum
		
		print(now_hum)
		if now_hum < HUM_THRESHOLD :
			GPIO.output(A1A, GPIO.HIGH)
			GPIO.output(A1B, GPIO.LOW)
		else:
			GPIO.output(A1A, GPIO.LOW)
			GPIO.output(A1B, GPIO.LOW)
		
		if waterlevel(waterLevel_pin) == 1 :
			GPIO.output(2, GPIO.HIGH)
			GPIO.output(3, GPIO.LOW)
		else :
			GPIO.output(2, GPIO.LOW)
			GPIO.output(3, GPIO.HIGH)

		t += 1

		if t >= 100 :
#humidTemp()
			t = 0
		time.sleep(0.1)

#Clean up GPIO and spi
finally:
	GPIO.cleanup()
	spi.close()

