#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int analogPin = A0;
int led = 13;
int data = 0;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}

void loop(){
  int data = analogRead(analogPin);

  if(isnan(data)){
    Serial.println("Failed to read from rain_drop sensor");
  }
  
  else if(data<800){
    digitalWrite(led, HIGH);
  }
  else{
    digitalWrite(led, LOW);
  }
  show(data);
  delay(500);
}

void show(int val){
  lcd.init();
  Serial.println((int)val);
  String text = "Rain value";

  lcd.setCursor(0,0);
  lcd.print(text);

  lcd.setCursor(0,1);
  lcd.print(val);
}
