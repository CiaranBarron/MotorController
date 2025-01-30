// MCU is Sparkfun Pro Micro (Select 5V version in Tools!!!). 
// V3.0 Robin O'Reilly Jan 2025

/*
>>> Command Summary <<<
<H,*>              : This help file 
<RED_I_SET,VALUE>  : Set RED current to VALUE (mA)
<RED_I_GET,*>      : Get RED current (mA)
<UV_I_SET,VALUE>   : Set UV current to VALUE (mA)
<UV_I_GET,*>       : Get UV current (mA)
<UV_T_SET,VALUE>   : Set UV On Time to VALUE & turn on for value (secs) {MAX 300 secs} [VALUE = -1: On Indefinitely, VALUE = 0: Off]
<UV_T_GET,*>       : Get UV On Time (secs)
<CAM_SET,0>        : Disable camera
<CAM_SET,1>        : Enable camera
<CAM_GET,*>        : Query camera state
<ALL,0>            : Turn off both RED and UV

> Example: <RED_I_SET,100> to set RED current to 100mA
> Example: <UV_I_SET,200> to set UV current to 200mA
> Example: <CAM,1> to enable camera
> Example: <ALL,0> to turn off both RED and UV

Baudrate doesn't matter

*/

#include <MCP48xx.h>

const int relay = 9;
const int camPin = 7;
const int RED = 1;
const int UV = 0;
const int ENABLE = 1;
const int DISABLE = 0;
const int UV_TIME_MAX = 300; // Max UV timer on time secs
const int I_MAX = 500; // Max current mA

// DAC CS is pin 18
MCP4822 dac(18);  

// Default current values
int current_uv = 0;
int current_red = 30; // Default to 30mA at boot

// Default UV on time
int uv_on_time = 0;

// Default relay states
int relay_state = RED; // RED, UV
int cam_state = DISABLE; // ENABLE, DISABLE

void setup() { 
    pinMode(relay, OUTPUT);
    digitalWrite(relay, relay_state); 
    pinMode(camPin, OUTPUT);
    digitalWrite(camPin, cam_state); 
    
    // Initialise the DAC
    dac.init();         
    dac.turnOnChannelA();
    
    // Start Serial Communication
    Serial.begin(9600);
}

void loop() {
    // Check if there is available data to read from the Serial
    if (Serial.available() > 0) {
        
        String command = Serial.readStringUntil('\n'); // Read the full command till newline
        handleCommand(command);  // Process the command
    }
}

void handleCommand(String command) {
    command.trim();  // Remove leading and trailing spaces

    // Check if the command has the correct format (e.g., <RED, 100>)
    if (command.startsWith("<") && command.endsWith(">")) {
        command.remove(0, 1);  // Remove leading "<"
        command.remove(command.length() - 1, 1);  // Remove trailing ">"

        int commaPos = command.indexOf(',');
        if (commaPos != -1) {
            String parameter = command.substring(0, commaPos);
            int value = command.substring(commaPos + 1).toInt();
            
            // Call the appropriate function based on the command
            if (parameter == "RED_I_SET") {
                redCurrentSet(value);
            } else if (parameter == "RED_I_GET") {
                redCurrentGet();
            } else if (parameter == "UV_I_SET") {
                uvCurrentSet(value);
            } else if (parameter == "UV_I_GET") {
                uvCurrentGet();
            } else if (parameter == "UV_T_SET") {
                uvTimerSet(value);
            } else if (parameter == "UV_T_GET") {
                uvTimerGet();
            } else if (parameter == "CAM_SET" && (value == 0 || value == 1)) {
                cameraSet(value);
            } else if (parameter == "CAM_GET") {
                cameraGet();
            } else if (parameter == "ALL" && value == 0) {
                bothOff();
            } else if (parameter=="H"){
                printCommandSummary();
            } else {
                Serial.println("> Invalid command");
            }
        }
    } else {
        Serial.println("> Invalid command format. Use <H,*> for help");
    }
}

void redCurrentSet(int current) {

    current_red = current;
    if (relay_state == RED) setCurrent(current_red);
}

void redCurrentGet() { 

    Serial.print("> RED set to ");
    Serial.print(current_red);
    Serial.println(" mA");
}

void uvCurrentSet(int current) {

    current_uv = current;
    if (relay_state == UV) setCurrent(current_uv);
}

void uvCurrentGet() { 

    Serial.print("> UV set to ");
    Serial.print(current_uv);
    Serial.println(" mA");
}

void uvTimerSet(int time) {

    uv_on_time = time;

    if (uv_on_time == 0 && uv_on_time > UV_TIME_MAX) { // Turn UV off

        setCurrent(0); // Turn off current
        setRelay(RED); // Switch to RED
        setCurrent(current_red); // Turn on current
    }
    else if (uv_on_time >= -1) { // -1: Turn UV on indefinitely 

        if (RED)  // If RED on, switch to UV
        {
            setCurrent(0); // Turn off current
            setRelay(UV); // Switch to UV
            setCurrent(current_uv); // Turn on current
        }
        if (uv_on_time > 0) {

            delay(uv_on_time*1000); // Leave UV on for uv_on_time seconds

            setCurrent(0); // Turn off current
            setRelay(RED); // Switch to RED
            setCurrent(current_red); // Turn on current
            Serial.println("FIN");
        }
    }
}

void uvTimerGet() { 

    Serial.print("> UV on-time set to ");
    Serial.print(uv_on_time);
    Serial.println(" secs");
}

void cameraSet(int state) {

    cam_state = state;
    digitalWrite(camPin, cam_state);
}

void cameraGet() {

    if (cam_state == DISABLE) {
        Serial.println("> Camera Disabled");
    } else if (cam_state == ENABLE) {
        Serial.println("> Camera Enabled");
    }
}

void bothOff() {
    // Turn off both RED and UV
    setCurrent(0); // Turn off current
    setRelay(RED); // Set to the default, RED
    Serial.println("> Both RED and UV turned off");
}

void printCommandSummary() {
    Serial.println("\n>>> Command Summary <<<");
    Serial.println("<H,*>              : This help file ");
    Serial.println("<RED_I_SET,VALUE>  : Set RED current to VALUE (mA)");
    Serial.println("<RED_I_GET,*>      : Get RED current (mA)");
    Serial.println("<UV_I_SET,VALUE>   : Set UV current to VALUE (mA)");
    Serial.println("<UV_I_GET,*>       : Get UV current (mA)");
    Serial.println("<UV_T_SET,VALUE>   : Set UV On Time to VALUE & turn on for value (secs) {MAX 300 secs}\n[VALUE = -1: On Indefinitely, VALUE = 0: Off]");
    Serial.println("<UV_T_GET,*>       : Get UV On Time (secs)");
    Serial.println("<CAM_SET,0>        : Disable camera");
    Serial.println("<CAM_SET,1>        : Enable camera");
    Serial.println("<CAM_GET,*>        : Query camera state");
    Serial.println("<ALL,0>            : Turn off both RED and UV");

    Serial.println("> Commands are received over Serial.");
    Serial.println("> Example: <RED_I_SET,100> to set RED current to 100 mA");
    Serial.println("> Example: <UV_I_SET,200> to set UV current to 200 mA");
    Serial.println("> Example: <UV_T_SET,60> to turn on UV for 60 secs");
    Serial.println("> Example: <CAM,1> to enable camera");
    Serial.println("> Example: <ALL,0> to turn off both RED and UV\n");
}

void setCurrent(int current) {

    dac.setVoltageA(current);
    dac.updateDAC();
    delay(10);
    
}

void setRelay(int state) {

    relay_state = state;
    digitalWrite(relay, relay_state);
    delay(10);

}
