from PySide2.QtWidgets import *
from PySide2.QtCore import *
from entryUI import Ui_Form as Ui_EntryUI
from mainUI import Ui_Form as Ui_MainUI
from detailUI import Ui_Form as Ui_DetailUI
from otpUI import Ui_Form as Ui_Otp
from sleepUI import Ui_Form as Ui_SleepUI

import mysql.connector
import json
from datetime import datetime
import time
import sys
import os,subprocess

import RPi.GPIO as GPIO
import spidev
import Adafruit_DHT


#variable
success_acc = 0
detail_back =0
otp_back = 0

userfilepath= "./user_setting.json"
screenfilepath = '/boot/cmdline.txt'
plant_id = -1
user_data=[]
#물임계점
hum_threshold = -1
#물통 양 디지털
water_amount = 0

#recnet_watering의 크기
watering_cnt=0
temp=28
humi=30
soil=54
#파도 움직임
waveLV = 120

#취침모드
issleep=0
isfirst=0

#페이지 생성 확인용
is_detail_page = 0
is_sleep_page = 0

#센서 정보
t=0
humSensor = Adafruit_DHT.DHT11
humSensor_pin = 23
waterLV_pin=24
hum_max=0
A1A = 5
A1B = 6

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000


#watering_stop
watering_flag = 0
fromMaintoDetail =0


def sensor_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A1A, GPIO.OUT)
    GPIO.output(A1A, GPIO.LOW)
    GPIO.setup(A1B, GPIO.OUT)
    GPIO.output(A1B, GPIO.LOW)

	#WATERLEVEL Sensor GPIO Setting
    GPIO.setwarnings(False)
	
	#LED GPIO Setting
   

	#WaterLevel Sensor GPIO Setting
    GPIO.setup(waterLV_pin, GPIO.IN)


def read_spi_adc(adcChannel):
    global soil
    adcValue=0
    try:
        buff=spi.xfer2([1,(8+adcChannel)<<4,0])
        adcValue = ((buff[1]&3)<<8)+buff[2]
        soil = int(map(adcValue,hum_max,1023,0,100))
        soil = 100 - soil
    except:
        print("can\'t read spi_adc")
        return

# Mapping 0 to 100  with  Analog Sensor Value
def map(value, min_adc, max_adc, min_hum, max_hum):
	adc_range = max_adc-min_adc
	hum_range = max_hum - min_hum
	scale_factor = float(adc_range)/float(hum_range)
	return value/scale_factor

def humidTemp():
    global humi,temp
    humi,temp = Adafruit_DHT.read_retry(humSensor,humSensor_pin)
    humi = int(humi)
    temp = int(temp)


def check_waterlevel():
    global water_amount
    if water_amount != GPIO.input(waterLV_pin) : 
        water_amount = GPIO.input(waterLV_pin)
        user_data['water_amount'] = water_amount

        with open(userfilepath,"w",encoding = 'utf-8') as file:
            json.dump(user_data, file, indent = "\t",ensure_ascii=False)

#센서 측정 스레드_메인시작시 같이 시작
class sensorThread(QThread):
    global a,success_acc

    def __init__(self):
        super().__init__()
        sensor_init()

    def stop(self):
        GPIO.cleanup()
        spi.close()
        self.quit()
        self.wait(1000)

    def run(self):
        global temp,humi,waveLV,watering_flag
        t = 0
        self.send_datas=0

        screen(0)
        
        humidTemp()

        while(1):
            try:
                read_spi_adc(0)
                check_waterlevel()

                if(soil < hum_threshold):
                    GPIO.output(A1A, GPIO.HIGH)
                    GPIO.output(A1B, GPIO.LOW)
                    watering_flag = 1
                else:
                    GPIO.output(A1A, GPIO.LOW)
                    GPIO.output(A1B,GPIO.LOW)
                    if(watering_flag == 1):
                        watering()
                        watering_flag = 0
                
                t += 1
                #every 10sec
                if(t >= 100):
                    humidTemp()
                        #if 9oclock
                    self.nowtime = datetime.now().strftime("%H:%M")

                    if(self.nowtime == "09:00"):
                        if(self.send_datas == 0):
                            self.send_data()
                    elif(self.send_datas == 1):
                        self.send_datas = 0
                        
                            
                    t = 0
                #every 1sec
                if(t%10 == 0):
                    waveLV = ((100-soil)*7) + 120

                time.sleep(0.1)

            except:
                GPIO.cleanup()
                spi.close()
                break


    def send_data(self):
        try:
            self.cur = db.cursor()
            self.sql_str = "update plants_sensing set remaining_water = " +water_amount+ ", state_led= " + (1-issleep) +", moisture_level = " + soil +" where id=" + str(user_data['id']) 
            self.cur.execute(self.sql_str)
            self.cur.close()
            db.commit()
        except:
            db.reconnect()

#물줄때
def watering():
    global watering_cnt,user_data
    w_now_time = datetime.now().strftime("%y.%m.%d %H:%M")
    user_data['recent_watering'].append(w_now_time)
    watering_cnt += 1
    if(watering_cnt > 3):
        del(user_data['recent_watering'][0])
        watering_cnt = 3

    with open(userfilepath, "w", encoding='utf-8') as file:
        json.dump(user_data, file, indent="\t",ensure_ascii=False)
    
    #db update
    try:
        wcur=db.cursor()
        wsql_str = "update plants_sensing set last_watering = \"" + w_now_time + "\"  where id=" + str(user_data['id']) 
        wcur.execute(wsql_str)
        wcur.close()
        db.commit()
    except Exception as e:
        print("db update is impossible")


#Change sreensaver

def screen(screen_mode):
    #sleep_mode : 10sec
    if(screen_mode == 1):
        
        subprocess.run("sudo python3 ./led_off.py",shell=True)
        subprocess.run('xset s on',shell = True)
        subprocess.run('xset s 10',shell = True)
    else:
        #GPIO.output(LED1, GPIO.HIGH)
        #GPIO.output(LED2, GPIO.HIGH)
        subprocess.run("sudo python3 ./led_on.py",shell=True)
        subprocess.run('xset s off',shell=True)


#시작 페이지 
class EntryPage(QDialog, QWidget, Ui_EntryUI):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.dbset()

    def dbset(self):
        #db커넥트
        global db
        db = mysql.connector.connect(host="db_server",user='username', password='pw', database='db_name',buffered=True)

    def main(self):
        pass

    #새식물 등록
    def new_plant(self):

        widget.setCurrentIndex(1)

    def old_plant(self):
        global success_acc
        global plant_id,nickname,water_amount,hum_threshold
        global user_data,watering_cnt
        

        if(user_data['id'] == -1):
            msgBox = QMessageBox()
            msgBox.setText("There is no information\nPlease push NEW button")
            msgBox.exec()
        #쿼리요청
        self.cur = db.cursor()
        self.sql_str = "select is_connected from plants_myplant where id=" + str(user_data['id'])
        self.cur.execute(self.sql_str)
        

        for result in self.cur:
            # connect success 바로 메인페이지로 이동
            if(result[0] == 1):
                #connect == 1 이면 연결유지 상태 메인페이지 이동
                hum_threshold=user_data['hum_threshold']
                watering_cnt = len(user_data['recent_watering'])
                success_acc = 1
                widget.addWidget(MainPage())
                widget.setCurrentIndex(2)
            else:
                #연결이 끊기면 오류메세지
                msgBox = QMessageBox()
                msgBox.setText("There are no connected plants")
                msgBox.exec()
                #연결이 끊겨있으므로 user_data정보 지워줌

                user_data['id'] = -1
                user_data['nickname'] = ""
                user_data['hum_threshold'] = -1
                user_data['recent_watering']= []
                user_data['water_amount'] = 0
                # 수정반영
                with open(userfilepath, "w", encoding='utf-8') as file:
                    json.dump(user_data, file, indent="\t", ensure_ascii=False)

            #print(result[0])

        #다시 누를 것 대비_변경반영

        self.cur.close()
        db.commit()
#메인 페이지 _ 파도 화면
class MainPage(QDialog, QWidget, Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.now = datetime.now().strftime('%H : %M')
        self.clock.setText(self.now)
        #온습도 글씨
        humidTemp()
        self.humi_label.setText(str(humi)+"%")
        self.temp_label.setText(str(temp)+"ºC")

        #시계를 위해 5초에 한번 화면 새로고침

        self.main()

    def main(self):
        global snsth, clock_timer
        self.warn_label.hide()

        self.now = datetime.now().strftime('%H : %M')
        self.clock.setText(self.now)
        #시계 타이머
        clock_timer = QTimer(self)
        clock_timer.setInterval(5000)  # 1초 => 나중에 5초에 한번으로 바꿀거임
        clock_timer.timeout.connect(self.show_clock)
        clock_timer.start()

        #센서 스레드
        snsth = sensorThread()
        snsth.start()

    def go_detailPage(self):
        global detail_back,is_detail_page
        #화면 새로고침 필요없음
        clock_timer.stop()
        #디테일페이지 선언 및 화면 전환
        if (is_detail_page == 0):
            is_detail_page = 1
            widget.addWidget(DetailPage())
            widget.addWidget(SleepPage())
        widget.setCurrentIndex(3)
        # 뒤로가기 버튼으로 돌아왔을때

    #화면 새로고침
    def show_clock(self):
        global now_time
        #시간 00:00 형태
        self.now = datetime.now().strftime('%H : %M')
        self.clock.setText(self.now)
        #온습도 글씨
        #humidTemp()
        self.humi_label.setText(str(humi)+"%")
        self.temp_label.setText(str(temp)+"ºC")

        #파도 조절
        self.wave.setGeometry(QRect(0, waveLV , 1366, 768))
        #print(now_time)

        if(water_amount == 0):
            self.warn_label.show()
        else:
            self.warn_label.hide()



class DetailPage(QDialog, QWidget, Ui_DetailUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #최근 관수날짜 보드
        #초기화 후 채워넣음
        self.watering_board = [self.label_8, self.label_9, self.label_10]
        self.label_8.clear()
        self.label_9.clear()
        self.label_10.clear()
        self.label_11.setText(user_data['nickname'])
        self.label_4.setText(str(temp)+"ºC")
        self.label_5.setText(str(humi)+"%")
        self.label_6.setText(str(soil)+"%")

        #화면 새로고침 한번 하고 시작
        self.main()

    def main(self):
        #관수정보
        for i in range(len(user_data['recent_watering'])):
            self.watering_board[i].setText(user_data['recent_watering'][len(user_data['recent_watering'])-i-1])


        #물의 양
        if(water_amount == 1):
            self.progressBar.setStyleSheet(
                "QProgressBar::chunk { background-color : rgb(101, 128, 93) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")
            self.progressBar.setValue(80)
        else:
            self.progressBar.setStyleSheet(
                "QProgressBar::chunk { background-color : rgb(163, 77, 79) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")
            self.progressBar.setValue(40)


       
    #메인페이지로 돌아감
    def go_mainpage(self):
       
        global clock_timer
        clock_timer.start()
        widget.setCurrentIndex(2)
    #취침모드
    def sleep_mode(self):
        global issleep,is_sleep_page

        issleep = 1
       
        #취침모드에서 벗어나면 바로 메인페이지로 돌아감

        
        screen(1)
        widget.setCurrentIndex(4)

    



    #새로고침
    def redo(self):
        #관수정보
        for i in range(len(user_data['recent_watering'])):
            self.watering_board[i].setText(user_data['recent_watering'][len(user_data['recent_watering'])-i-1])

        #닉네임
        try:
            self.cur = db.cursor()
            self.sql_str = "select nickname from plants_myplant where id=" + str(user_data['id'])
            self.cur.execute(self.sql_str)

            for (res) in self.cur:
            #print(res)
            #닉네임 변경시
                if(res[0] != user_data['nickname']):
                    self.label_11.setText(res[0])
                    user_data['nickname'] = res[0]
                    with open(userfilepath, "w", encoding='utf-8') as file:
                        json.dump(user_data, file, indent="\t", ensure_ascii=False)

            self.cur.close()
            db.commit()
        except Exception as e:
            print(e)
            db.reconnect()
            

        #물의 양
        if(water_amount == 1):
            self.progressBar.setStyleSheet(
                "QProgressBar::chunk { background-color : rgb(101, 128, 93) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")
            self.progressBar.setValue(80)
        else:
            self.progressBar.setStyleSheet(
                "QProgressBar::chunk { background-color : rgb(163, 77, 79) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")
            self.progressBar.setValue(40)


        #humi,temp,soil
        self.label_5.setText(str(humi)+"%")
        self.label_4.setText(str(temp)+"ºC")
        self.label_6.setText(str(soil)+"%")

    #프로그램 및 라즈베리파이 종료
    #코드 해제를 위함
    def turnoff(self):
        global clock_timer, snsth
        clock_timer.stop()
        snsth.stop()
        GPIO.cleanup()
        spi.close()
        subprocess.run("sudo python3 ./led_off.py",shell=True)
        quit()
        #라즈베리파이 종료 
        sys.exit(0)


#otp코드
class OtpPage(QDialog, QWidget, Ui_Otp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.otp_code = ""
        self.number_label = [self.number_1, self.number_2, self.number_3, self.number_4, self.number_5, self.number_6]
        for i in range(6):
            self.number_label[i].clear()


    def check_otp(self):
        global success_acc,isfirst
        global plant_id, water_amount, hum_threshold
        self.flag=0

        #otp코드가 6자리일때
        if(len(self.otp_code) == 6):
            #self.flag = 1
            self.cur = db.cursor()

            # is otp exist?
            self.sql_str = "select A.id, A.nickname, A.otp_code, A.is_connected, B.watercycle_spring from plants_myplant A join plants_plants B on A.plant_info_id = B.id where otp_code = " + self.otp_code
            self.cur.execute(self.sql_str)
            # result = 1개
            if(self.cur.rowcount ==1):
                #id, 닉네임, 물의 양 등 저장
                for(id,name,otp,isconnect,hum_t) in self.cur:
                    #Already connect
                    #이미 연결이 되어있는 식물의 경우
                    if(isconnect == 1):
                        self.flag = 2
                        break;
                    #가져온 id(pk),name 저장
                    self.plant_id = int(id)
                    self.name = str(name)
                    self.hum_threshold = hum_t

                # Success connect!
                if(self.flag != 2):
                    self.flag = 1

                    # make otp=NULL, isconnect = 1
                    self.sql_str = "update plants_myplant set otp_code=NULL, is_connected=1 where id="+str(self.plant_id)
                    self.cur.execute(self.sql_str)

                    #json 수정

                    user_data['id'] = self.plant_id
                    user_data['nickname'] = self.name
                    user_data['recent_watering'] = []
                    user_data['water_amount']=0
                    #humuduty 정리
                    if(self.hum_threshold == "053001"):
                        hum_threshold = 80
                    elif(self.hum_threshold == "053002"):
                        hum_threshold = 60
                    elif(self.hum_threshold == "053003"):
                        hum_threshold = 40
                    elif(self.hum_threshold == "053004"):
                        hum_threshold = 20
                    else:
                        hum_threshold = 0

                    user_data['hum_threshold']=hum_threshold
                    #수정반영
                    with open(userfilepath, "w", encoding='utf-8') as file:
                        json.dump(user_data, file, indent="\t",ensure_ascii=False)

                    plant_id = self.plant_id
                    water_amount = 0
        
                    db.commit()
            else:
                self.flag = 0

        #성공했을때_db에 정보존재
        if(self.flag == 1):
            success_acc = 1
            widget.addWidget(MainPage())
            isfirst = 1
            widget.setCurrentIndex(2)
        else:
            #실패했을때
            msgBox = QMessageBox()
            if(self.flag == 2):
                msgBox.setText("Already connected")
            else:
                msgBox.setText("Wrong OTP")
            msgBox.exec()

            #실패시 otp코드 초기화
            success_acc = 0
            for i in range(6):
                self.number_label[i].clear()
            self.otp_code = ""



    def back_entry(self):
        #global otp_back
        #메인으로 다시 돌아감
        #otp_back = 1
        #self.close()
        widget.setCurrentIndex(0)

    #숫자보드 입력
    def click_pad(self):
        self.send = self.sender().text()


        if( self.send == "<"):
            if(len(self.otp_code) != 0):
                self.number_label[len(self.otp_code) - 1].clear()
                self.otp_code = self.otp_code[:-1]

        else:
            if(len(self.otp_code) < 6):
                self.otp_code += self.send
                self.number_label[len(self.otp_code)-1].setText(self.send)


#취침 화면
class SleepPage(QDialog, QWidget, Ui_SleepUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.show()
        #self.main()

    def main(self):
       #self.testlabel.setText(str(a))
       #ScreenSaver
       pass

    #화면 터치시 취침모드 종료 후 파도화면으로 돌아감
    def wakeup(self):
        global issleep
        #self.close()
        clock_timer.start()
        screen(0)
        issleep = 1
        widget.setCurrentIndex(2)


app=QApplication()
main = EntryPage()

widget = QStackedWidget()
widget.addWidget(main)
widget.addWidget(OtpPage())
#widget.setFixedHeight(768)
#widget.setFixedWidth(1366)
widget.setGeometry(0,0,1366,768)

#프로그램 실행 전 user_data 불러옴

#한글 읽기 위하여 encoding 표시
with open(userfilepath, "r", encoding="utf-8") as file:
    user_data = json.load(file)


widget.show()
app.exec_()
