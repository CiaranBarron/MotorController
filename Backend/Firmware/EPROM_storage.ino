#include <EEPROM.h>

long motor_position_x;
long motor_position_y;

// Assigning EEPROM addresses to each storable variable
constexpr int address_motor_position_x = 1*sizeof(long);
constexpr int address_motor_position_y = 2*sizeof(long);


void setup() {

  // <- might need to use this when things don't work properly
  // wipeEEPROM();  

  // Read variables from EEPROM
  readFromEEPROM(address_motor_position_x, motor_position_x);
  readFromEEPROM(address_motor_position_y, motor_position_y);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  // moveMotorX(10);
  // new motor position x now 10
  saveToEEPROM(address_motor_position_x, motor_position_x);  
}


void wipeEEPROM() {
  for (int i = 0; i < EEPROM.length(); i++) {
    EEPROM.write(i, 0);
  }
}

void readFromEEPROM(int address, long &value) {
  EEPROM.get(address, value);
}

void saveToEEPROM(int address, long value) {
  EEPROM.put(address, value);
}
