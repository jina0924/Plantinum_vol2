// 참고자료 : 라즈베리 파이를 이용한 자동 수위 관리 모듈 시스템
// https://damdam-e-1993.tistory.com/10?category=795623

#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>

#define TRIG 5 //GPIO 24
#define ECHO 4 //GPIO 23
#define SERVO 1 //GPIO 18
#define LED 22 //GPIO 6
#define btn 21 //GPIO 5 // 수위 조절
#define btn2 23 //GPIO 13 // 수동 모드 시 셋팅모드/실행모드
#define btn3 24 //GPIO 19 // 자동/수동 셋팅

// 메뉴 활성 및 유저 선택 함수

int modeSelect(){
 unsigned int preval‎ue=0; 
 unsigned int modeselect=0;

 printf("========================\n");
 printf("[MODE SELECT]\n");
 printf("[1] -> 'AUTO MODE'\n");
 printf("[2] -> 'MANUAL MODE'\n");
 printf("[3] -> 'TEST MODE'\n");
 printf("[4] -> 'EXIT'\n");
 printf("========================\n");

 while(digitalRead(btn2)==0){
  if(digitalRead(btn3)==1){
   modeselect +=1;
   delay(250);
   if(modeselect>4){
    modeselect = 1;
   }
   if(modeselect!=preval‎ue){
    switch(modeselect){
     case 1:
      printf("[1] AUTO MODE\n");
      break;
     case 2:
      printf("[2] MANUAL MODE\n");
      break;
     case 3:
      printf("[3] TEST MODE\n");
      break;
     case 4:
      printf("[4] EXIT\n");
      break;
    };
    //printf("[%d]\n",modeselect);
   }
   preval‎ue = modeselect;
  }
 }
 return modeselect;
}


int main(void)
{
 int distance=0; // 센서-> 수위 체크, 단위: Cm
 unsigned int m_count=2; //수동모드(Manual) count
 unsigned int a_count=0; //자동모드(Auto) count
 unsigned int m_pre=0; //수동모드(Manual) 출력문 잠금장치(무한루프출력방지)
 unsigned int a_pre=0; //자동모드(Auto) 출력문 잠금장치(무한루프출력방지)
 unsigned int m_run=0; //수동모드(Manual) 실행 제어 변수
 unsigned int a_run=0; //자동모드(Auto) 실행 제어 변수
 unsigned int modechange=0; //수동모드(Manual)에서 모드 변경 변수
 unsigned int mode=0; //[1]~[4]모드 선택 변수
 
  char str; //Power On/Off contorl variable
 
 if(wiringPiSetup() == -1)
  return -1;
 
 pinMode(TRIG, OUTPUT);
 pinMode(ECHO, INPUT);
 
 pinMode(btn,INPUT); //수위 높이 카운터
 pinMode(LED,OUTPUT); //버튼 눌림 알림
 
 pinMode(btn2,INPUT); //실행 및 셋팅모드
 pinMode(btn3,INPUT); //자동/수동 모드 선택

  softPwmCreate(SERVO,0,200); //Servo Motor Pwm Create

 while(1){

  //Power On/Off contorl

  fputs("SELECT\n", stdout);
  printf("[o]:RUN\t\n[x]:EXIT\t\n=>");
  scanf("%c",&str);
  getchar();

  //System Activation
  while(1){
   if((str=='o')){
    mode=0;
    if((mode==0)){
     mode = modeSelect(); //Mode Selection
    }
    switch(mode){
     case 1: //Auto Mode
      printf("[AUTO MODE]\t*Start:Btn2*\n");
      printf("Second pressed Btn2: Menu\n"); //btn2 토글 시 모드변경
      delay(500);
      while(1){
       if(digitalRead(btn2)==1){ //Auto Mode Run control(On/Off)
        a_run += 1;
        delay(250);
       }
       if((a_run%2)==0){ //메뉴로 나가기 전 초기화
        if(a_run!=a_pre){
         a_run = 0;
         break;
         a_pre=a_run;
        }
       }
       if(a_run){
        digitalWrite(TRIG, LOW);
        usleep(2);
        digitalWrite(TRIG, HIGH);
        usleep(20);
        digitalWrite(TRIG, LOW);
      
        //Ultra Sonic Sensor Activation(get distance)

        while(digitalRead(ECHO) == LOW);
        long startTime = micros();
        while(digitalRead(ECHO) == HIGH);
        long travelTime = micros() - startTime;
         
        distance = travelTime/58;
        printf("Distance : %dcm\n", distance);
    
        delay(250);
        
        printf("\t\t\t\t[MODE:AUTO]\n");
    
        if(distance<4){ //최고 수위 도달 시 수문개방
         if(distance<=5){
          softPwmWrite(SERVO,15);
         }
        }
        else if(distance>5 && distance<=6){ //최저 수위 도달 시 수문폐쇄(일정수위유지)
         softPwmWrite(SERVO,24);
        }
       }
      }
      break;
     case 2: //Manual Mode
      printf("[MANUAL MODE]\tMenu:btn2->btn1(count:10)\n");
      printf("========================\n");
      delay(500);
      while(1){
        if(digitalRead(btn2)==1){ //Auto Mode Run control(On/Stop)
         m_run += 1;
         delay(250);
        }    
        if((m_run%2)==0){ //수위 셋팅모드
         m_run = 0;
         if(digitalRead(btn)==1){
          digitalWrite(LED,1);
          m_count+= 1;
          modechange++; //Manual Mode -> Menu Change Varialbe
          if(modechange%10==0){ //btn2 count value: 10 -> Mode Change
           m_count=2;
           modechange=0;
           digitalWrite(LED,0);
           break;
          }
          //m_count 2~5 셋팅 값 사이클
          if(m_count>5){
           m_count=2;
          }
          delay(250);
          }else{
           digitalWrite(LED,0);
          }
          if(m_count!=m_pre){ //count value 무한루프 출력방지장치
           printf("%d",m_count);
           printf("\t[Max_Sensor_Distance:%dcm , Min_Sensor_Distance:%dcm]\n",m_count+3,m_count);
           m_pre=m_count;
          } 
        }
        if(m_run){
         modechange=0;
         digitalWrite(TRIG, LOW);
         usleep(2);
         digitalWrite(TRIG, HIGH);
         usleep(20);
         digitalWrite(TRIG, LOW);
       
         while(digitalRead(ECHO) == LOW);
         long startTime = micros();
         while(digitalRead(ECHO) == HIGH);
         long travelTime = micros() - startTime;
          
         distance = travelTime/58;
         printf("Distance : %dcm\n", distance);
         delay(250);
         
         printf("\t\t\t\t[MODE:MANUAL]\n");
         대
         if(distance<m_count){ //세팅 값의 센서거리의 최소 값(최대수위), 수문개방
          if(distance<=(m_count+3)){
           softPwmWrite(SERVO,15);
          }
         }else if(distance>(m_count+3) && distance<=(m_count+4)){ //세팅 값의 센서거리의 최 값(최저수위), 수문폐쇄
          softPwmWrite(SERVO,24);
         }
        }
      }
      break;
     case 3: //Test Mode
      delay(350);
      printf("[TEST MODE]\t*Btn2:Open/Close*\n");
      while(1){
       if(digitalRead(btn)==1){
        softPwmWrite(SERVO,15);
        delay(500);
        printf("[OPEN]\n");
       }else if(digitalRead(btn3)==1){
        break;
       }
       else{
        softPwmWrite(SERVO,24);
        delay(500);
        printf("[CLOSE]\n");
       }
      }
      
      break;
     case 4: //System deActivation
      return 0;
      break;
     };
   }
   else if(str=='x') return 0;
   else break;
  }
 } 
}