#include <Servo.h>

Servo motorPan;  // Pinul 9 (Stanga-Dreapta)
Servo motorTilt; // Pinul 10 (Sus-Jos)

void setup() {
  motorPan.attach(9);
  motorTilt.attach(10);
}

void loop() {
 
  
  motorPan.write(0);
  delay(1500);
  
  motorPan.write(180);
  delay(1500);
  
  motorPan.write(90); 
  delay(1000);


  
  
  motorTilt.write(45);
  delay(1500);
  
  motorTilt.write(120);
  delay(1500);
  
  motorTilt.write(90); 
  delay(1000);
}