#include <AccelStepper.h>
#include <ArduinoJson.h>
#include <EEPROM.h>

// Define motor pins
#define MOTOR_A_STEP_PIN 5
#define MOTOR_A_DIR_PIN 3
#define MOTOR_B_STEP_PIN 4
#define MOTOR_B_DIR_PIN 2

// Define hall sensor pins
#define HALL_SENSOR_A_PIN 7
#define HALL_SENSOR_B_PIN 6

// Define LED pin
#define LED_PIN 9

// Define button pin
#define BUTTON_PIN 8

// Create AccelStepper objects for both motors
AccelStepper motorA(AccelStepper::DRIVER, MOTOR_A_STEP_PIN, MOTOR_A_DIR_PIN);
AccelStepper motorB(AccelStepper::DRIVER, MOTOR_B_STEP_PIN, MOTOR_B_DIR_PIN);

// Motor positions A and B (will be stored in EEPROM)
long motorPositionA;
long motorPositionB;

// Assign EEPROM addresses to store motor positions
constexpr int addrMotorPositionA = 1*sizeof(long);
constexpr int addrMotorPositionB = 2*sizeof(long);

// Variables to track homing status
volatile bool homingCompleteA = false;
volatile bool homingCompleteB = false;

// Variables for LED flashing
unsigned long previousMillis = 0;
const long interval = 500; // interval for 1Hz flashing

// Variables for button press
unsigned long buttonPressTime = 0;
bool buttonPressed = false;
bool buttonHeld = false;

//EEPROM function for reset, read and write. 
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

// Interrupt Service Routines (ISR) for hall sensors
void hallSensorA_ISR() {
  motorA.stop();
  motorA.setCurrentPosition(0);
  saveToEEPROM(addrMotorPositionA, 0);
  homingCompleteA = true;
  detachInterrupt(digitalPinToInterrupt(HALL_SENSOR_A_PIN));
}

void hallSensorB_ISR() {
  motorB.stop();
  motorB.setCurrentPosition(0);
  saveToEEPROM(addrMotorPositionB, 0);
  homingCompleteB = true;
  detachInterrupt(digitalPinToInterrupt(HALL_SENSOR_B_PIN));
}

// Home the motors by moving them until the hall sensor is triggered
void homeMotors() {
  Serial.print("> Homing Motors..");
  homingCompleteA = false;
  homingCompleteB = false;

  // Motor speed and accel are set in the setup.
  motorA.moveTo(-1000000); // Move a large number of steps anticlockwise
  motorB.moveTo(-1000000); // Move a large number of steps anticlockwise

  // Attach interrupts to hall sensors
  attachInterrupt(digitalPinToInterrupt(HALL_SENSOR_A_PIN), hallSensorA_ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(HALL_SENSOR_B_PIN), hallSensorB_ISR, FALLING);

  // set the motors to home one at a time.
  while (!homingCompleteA) {
    motorA.run();
  }
  while (!homingCompleteB) {
    motorB.run();
  }
  // reset positions in EEPROM after Homing.
  saveToEEPROM(addrMotorPositionA, 0);
  saveToEEPROM(addrMotorPositionB, 0);

  // Ensure the LED is off after homing
  digitalWrite(LED_PIN, LOW);
  Serial.println("Done");
}

void setup() {
  // Initialize serial communication
  Serial.begin(115200);

  // Set hall sensor pins as input pullup
  pinMode(HALL_SENSOR_A_PIN, INPUT_PULLUP);
  pinMode(HALL_SENSOR_B_PIN, INPUT_PULLUP);

  // Set LED and button pins
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Serial.println();Serial.println();Serial.println();
  Serial.println("> **********Dual Stepper Motor Driver*********RoR24");
  Serial.println("> JSON Commands: {\"stepsA\": X, \"stepsB\": Y, \"Home\": 0}");
  Serial.println("> Pressing flashing button on front of device will stop movement.");

  // Read current motor position from EEPROM
  readFromEEPROM(addrMotorPositionA, motorPositionA);
  readFromEEPROM(addrMotorPositionB, motorPositionB);

  Serial.print("> Stored EEPROM positions: ");
  Serial.print(motorPositionA);
  Serial.print(", ");
  Serial.println(motorPositionB);

  // set positions in Motor object.
  motorA.setCurrentPosition(motorPositionA);
  motorB.setCurrentPosition(motorPositionB);
  
  // These need to be set or the motors wont move. Used to be in home motors which ran automatically. 
  motorA.setMaxSpeed(500);
  motorA.setAcceleration(500);
  motorB.setMaxSpeed(500);
  motorB.setAcceleration(500);
}

void loop() {

  // read current position from storage
  // readFromEEPROM(addrMotorPositionA, motorPositionA);
  // readFromEEPROM(addrMotorPositionB, motorPositionB);

  // Check for button press
  if (digitalRead(BUTTON_PIN) == LOW) {
    if (!buttonPressed) {
      buttonPressed = true;
      motorA.stop();
      motorB.stop();
      Serial.println("> Emergency Stop");
    }
  } else {
    buttonPressed = false;
  }

  // Check for serial input and parse JSON
  if (Serial.available() > 0) {
    String jsonString = Serial.readStringUntil('\n');
    StaticJsonDocument<200> doc;
    DeserializationError error = deserializeJson(doc, jsonString);

    if (!error) {
      int stepsA = doc["stepsA"];
      int stepsB = doc["stepsB"];
      int homeFlag = doc["Home"];
      int motorSpeed = doc["motorSpeed"];
      int motorAccel = doc["motorAccel"];

      // can optionally update the motor speed and accel, might want to do a slow moving exposure. 
      if (motorSpeed > 0) {
        motorA.setMaxSpeed(motorSpeed);
        motorB.setMaxSpeed(motorSpeed);
        if (motorAccel > 0) {
          motorA.setAcceleration(motorAccel);
          motorB.setAcceleration(motorAccel);
        }
      }
      // Homing Motors
      if (homeFlag > 0) {
        homeMotors();
        stepsA = 500;
        stepsB = 500;
      }

      // moving motors to new positions. After homing this will be 500, 500 -> else sent position.
      motorA.moveTo(stepsA);
      motorB.moveTo(stepsB);
      
      // update tracked position
      motorPositionA = stepsA;
      motorPositionB = stepsB;
      
      Serial.print("> Moving Motors: ");
      Serial.println(jsonString);
    } else {
      Serial.println("> Failed to parse JSON");
    }
  }

  bool motorsMoving = motorA.distanceToGo() != 0 || motorB.distanceToGo() != 0;

  // Run the motors to their target positions
  motorA.run();
  motorB.run();

  // Flash the LED at 1Hz when motors are moving
  if (motorsMoving) {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    }
  } else {
    // Ensure the LED is off when motors are not moving
    digitalWrite(LED_PIN, LOW);
  }
  
  motorA.setCurrentPosition(motorPositionA);
  motorB.setCurrentPosition(motorPositionB);

  Serial.print(motorA.currentPosition());Serial.print(", ");Serial.println(motorPositionB);
  
  // save new motor positions to EEPROM AFTER it has finished moving.
  saveToEEPROM(addrMotorPositionA, motorPositionA);
  saveToEEPROM(addrMotorPositionB, motorPositionB);
}
