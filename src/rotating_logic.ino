#include <Servo.h>

Servo motorPan;  // Pin 9 (Stanga-Dreapta)
Servo motorTilt; // Pin 10 (Sus-Jos)

void setup() {
  Serial.begin(9600); // Deschidem comunicarea cu PC-ul
  motorPan.attach(9);
  motorTilt.attach(10);
  
  motorPan.write(90);
  motorTilt.write(90);

  pinMode(13, OUTPUT);    
  digitalWrite(13, HIGH);
}

void loop() {
  // Daca primim un mesaj prin cablul USB
  if (Serial.available() > 0) {
    // Citim mesajul (are formatul "X90Y120")
    String date = Serial.readStringUntil('\n');
    
    int indexX = date.indexOf('X');
    int indexY = date.indexOf('Y');
    
    if (indexX != -1 && indexY != -1) {
      // Extragem unghiurile
      int valX = date.substring(indexX + 1, indexY).toInt();
      int valY = date.substring(indexY + 1).toInt();
      
      // Filtru de siguranta absolut:
      valX = constrain(valX, 0, 180);
      valY = constrain(valY, 45, 125); 
      
      // Mutam motoarele
      motorPan.write(valX);
      motorTilt.write(valY);
    }
  }
}