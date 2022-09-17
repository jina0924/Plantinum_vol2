 #import Adafruit_DHT

 #sensor = Adafruit_DHT.DHT11
 #pin = 23

def humidTemp():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('값을 읽을 수 없습니다.')
