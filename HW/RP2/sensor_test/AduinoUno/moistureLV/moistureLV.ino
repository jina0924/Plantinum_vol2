
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  
  int Soil_moisture = analogRead(A0);  
  Serial.println(Soil_moisture);        
  delay(500);
}
