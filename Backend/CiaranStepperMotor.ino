#include <AccelStepper.h>
#include <ArduinoJson.h>

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

// Interrupt Service Routines (ISR) for hall sensors
void hallSensorA_ISR() {
  motorA.stop();
  motorA.setCurrentPosition(0);
  homingCompleteA = true;
  detachInterrupt(digitalPinToInterrupt(HALL_SENSOR_A_PIN));
}

void hallSensorB_ISR() {
  motorB.stop();
  motorB.setCurrentPosition(0);
  homingCompleteB = true;
  detachInterrupt(digitalPinToInterrupt(HALL_SENSOR_B_PIN));
}

// Home the motors by moving them until the hall sensor is triggered
void homeMotors() {
  Serial.print("> Homing Motors..");
  
  homingCompleteA = false;
  homingCompleteB = false;

  motorA.setMaxSpeed(500);
  motorA.setAcceleration(500);
  motorA.moveTo(-1000000); // Move a large number of steps anticlockwise

  motorB.setMaxSpeed(500);
  motorB.setAcceleration(500);
  motorB.moveTo(-1000000); // Move a large number of steps anticlockwise

  // Attach interrupts to hall sensors
  attachInterrupt(digitalPinToInterrupt(HALL_SENSOR_A_PIN), hallSensorA_ISR, FALLING);
  attachInterrupt(digitalPinToInterrupt(HALL_SENSOR_B_PIN), hallSensorB_ISR, FALLING);

  while (!homingCompleteA || !homingCompleteB) {
    if (!homingCompleteA) {
      motorA.run();
    }
    if (!homingCompleteB) {
      motorB.run();
    }

    // Flash the LED at 1Hz while homing
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    }
  }

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

  Serial.println(); Serial.println(); Serial.println();
  Serial.println("> **********Dual Stepper Motor Driver*********");
  Serial.println("> RoR 2024");
  Serial.println("> After the motors home, set position using JSON: {\"stepsA\": X, \"stepsB\": Y}");
  Serial.println("> Pressing flashing button on front of device will stop movement in the event of an emergency. Holding for 5 seconds will force both motors to home");
 
  // Home the motors at startup
  homeMotors();
}

void loop() {
  // Check for button press
  if (digitalRead(BUTTON_PIN) == LOW) {
    if (!buttonPressed) {
      buttonPressed = true;
      buttonPressTime = millis();
    } else if (millis() - buttonPressTime > 3000) {
      buttonHeld = true;
      homeMotors();
      buttonHeld = false;
    }
  } else {
    if (buttonPressed && !buttonHeld) {
      // Single short press action: halt motion
      motorA.stop();
      motorB.stop();
      Serial.println("> Emergency Stop");
    }
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

      motorA.moveTo(stepsA);
      motorB.moveTo(stepsB);

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
}
