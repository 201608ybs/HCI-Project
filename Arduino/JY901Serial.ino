#include <JY901.h>
#include <JY901_dfs.h>
#include <SoftwareSerial.h>
#define FINGERNUM 5
SoftwareSerial serial0(10, 11); //RX,TX
SoftwareSerial serial1(12, 13);
SoftwareSerial serial2(A8, A9);
SoftwareSerial serial3(50, 51);
SoftwareSerial serial4(52, 53);
SoftwareSerial serials[FINGERNUM] = {serial0, serial1, serial2, serial3, serial4};
CJY901 JY901s[FINGERNUM] = {JY901_0, JY901_1, JY901_2, JY901_3, JY901_4};
int pins[5] = {A0, A1, A2, A3, A4};


void setup() 
{
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  int i = 0;
  for (i = 0; i < FINGERNUM; ++i){
    serials[i].begin(9600);
    JY901s[i].attach(serials[i]);
  }
}

void loop() 
{
  int i = 0;
  for (i = 0; i < FINGERNUM; ++i){
    serials[i].listen();
    delay(80);
    JY901s[i].receiveSerialData();
    Serial.print(JY901s[i].getRoll());
    Serial.print(",");
    Serial.print(JY901s[i].getPitch());
    Serial.print(",");
    Serial.print(JY901s[i].getYaw());
    Serial.print(",");
  }
  delay(25);

  for (i = 0; i < FINGERNUM; ++i){
    int flexSensorReading = analogRead(pins[i]);
    Serial.print(flexSensorReading);
    if (i == FINGERNUM - 1){
      Serial.print("\n");
    }
    else{
      Serial.print(",");
    }
  }
  
  delay(50);
}
