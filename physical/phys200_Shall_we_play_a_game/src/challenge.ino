#include "Arduino.h"
#include "Keypad.h"
#include <Wire.h>
#include <Adafruit_RGBLCDShield.h>
#include <utility/Adafruit_MCP23017.h>

int toggle_1 = 52;
int toggle_2 = 50;
//int toggle_3 = 51;
int toggle_4 = 48;
int toggle_5 = 46;

int red_button = 26;
int blue_button = 23;
int white_button = 22;
int green_button = 24;
int yellow_button = 25;

int reset_switch = 2;

int key_1 = 38;
int key_2 = 40;

void run_challenge();
void init_challenge();
void selector_1();
void authcode();
void selector_2();
void shutdownseq();
void selector_3();
void keyturn();
void flag();

int ON = 1;
int OFF = 0;

int SWITCH_ON = 0;
int SWITCH_OFF = 1;

bool RESET_CHALLENGE = false;
bool RUN_CHALLENGE = true;

enum stage_enum { INIT, SELECTOR1, AUTHCODE, SELECTOR2, SHUTDOWNSEQ, SELECTOR3, KEYTURN, FLAG };
uint8_t state = INIT;

Adafruit_RGBLCDShield lcd = Adafruit_RGBLCDShield();
#define RED 0x1
#define YELLOW 0x3
#define GREEN 0x2
#define TEAL 0x6
#define BLUE 0x4
#define VIOLET 0x5
#define WHITE 0x7

int val = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(reset_switch, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(reset_switch), reset_challenge, CHANGE);
  
  pinMode(toggle_1, INPUT_PULLUP);   
  pinMode(toggle_2, INPUT_PULLUP);   
  //pinMode(toggle_3, INPUT_PULLUP);   
  pinMode(toggle_4, INPUT_PULLUP);   
  pinMode(toggle_5, INPUT_PULLUP);  
  
  pinMode(red_button, INPUT);   
  pinMode(blue_button, INPUT);  
  pinMode(white_button, INPUT);  
  pinMode(green_button, INPUT);   
  pinMode(yellow_button, INPUT); 

  pinMode(key_1, INPUT);
  pinMode(key_2, INPUT);

  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);

  if(digitalRead(reset_switch) ==  SWITCH_ON) {
    RUN_CHALLENGE = true;
  }
  

  Serial.println("In setup");
}

void reset_challenge() {
  static unsigned long last_interrupt_time = 0;
  unsigned long interrupt_time = millis();
  if (interrupt_time - last_interrupt_time > 200) {
    if(digitalRead(reset_switch) ==  SWITCH_OFF) {
            RUN_CHALLENGE = false;
            state = INIT;
            RESET_CHALLENGE = true;
            Serial.println("Turning off");
    } else {
            RUN_CHALLENGE = true;
            Serial.println("Turning on");
    }
  }
  last_interrupt_time = interrupt_time;
  
  
}

void loop() {
  // put your main code here, to run repeatedly:
//  val = digitalRead(inPin);   // read the input pin
//  Serial.println(val);
    run_challenge();
}

void run_challenge() {
  switch(state)
  {
    case INIT:
      init_challenge();
      break;
    case SELECTOR1:
      selector1();
      break;
    case AUTHCODE:
      authcode();
      break;
    case SELECTOR2:
      selector2();
      break;
    case SHUTDOWNSEQ:
      shutdownseq();
      break;
    case SELECTOR3:
      selector3();
      break;
    case KEYTURN:
      keyturn();
      break;
    case FLAG:
      flag();
      break;
    
  }
  
}

void init_challenge() {
  lcd.clear();
  lcd.setBacklight(0x00);
  while(RUN_CHALLENGE == false) {
    delay(10);
  }
  RESET_CHALLENGE = false;

  lcd.setBacklight(WHITE);
  
  pinMode(toggle_1, INPUT_PULLUP);    
  pinMode(toggle_2, INPUT_PULLUP); 
  //pinMode(toggle_3, INPUT_PULLUP); // toggle 3 wire broke, don't care to fix it, it's now a dead toggle
  pinMode(toggle_4, INPUT_PULLUP); 
  pinMode(toggle_5, INPUT_PULLUP);
  while(true) {
    int toggle_1_val =  digitalRead(toggle_1);
    int toggle_2_val =  digitalRead(toggle_2);
    //int toggle_3_val =  digitalRead(toggle_3);
    int toggle_4_val =  digitalRead(toggle_4);
    int toggle_5_val =  digitalRead(toggle_5);
  
    if (toggle_1_val == ON||
    toggle_2_val == ON ||
    //toggle_3_val == ON ||
    toggle_4_val == ON ||
    toggle_5_val == ON) {    
      lcd.clear();
      lcd.print("RESET SELECTOR");
      lcd.setCursor(0,1);
      lcd.print("SWITCHES");
      delay(1000);
    } else {
      break;
    }
  }
  

  lcd.setCursor(0, 0);
  lcd.setBacklight(GREEN);
  lcd.print(" NUCLEAR LAUNCH");
  lcd.setCursor(0,1);
  lcd.print("  INITIALIZED!");

  Serial.println("In init");

  state = SELECTOR1;
}

void selector1() {
  int toggle_1_val =  digitalRead(toggle_1);
  int toggle_2_val =  digitalRead(toggle_2);
  //int toggle_3_val =  digitalRead(toggle_3);
  int toggle_4_val =  digitalRead(toggle_4);
  int toggle_5_val =  digitalRead(toggle_5);

  if (toggle_1_val == ON &&
    toggle_2_val == OFF &&
    //toggle_3_val == ON &&
    toggle_4_val == ON &&
    toggle_5_val == OFF) {     
      state = AUTHCODE;
      pinMode(toggle_1, INPUT);    
      pinMode(toggle_2, INPUT); 
      //pinMode(toggle_3, INPUT); 
      pinMode(toggle_4, INPUT); 
      pinMode(toggle_5, INPUT);
    }
    
}

void authcode() {
  const byte rows = 4; //four rows
  const byte cols = 3; //three columns
  char keys[rows][cols] = {
    {'1','2','3'},
    {'4','5','6'},
    {'7','8','9'},
    {'*','0','#'}
  };
  byte rowPins[rows] = {12, 7, 8, 10}; //connect to the row pinouts of the keypad
  byte colPins[cols] = {11, 13, 9}; //connect to the column pinouts of the keypad
  Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, rows, cols );

  String code = "37234596";
  String entered_code = "";

  Serial.println("Starting stage 2");

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.setBacklight(WHITE);
  lcd.print("ENTER AUTH CODE");
  lcd.setCursor(0,1);
  while(RESET_CHALLENGE == false) {
    
    if (entered_code.equals(code)) {
      lcd.clear();
      lcd.setBacklight(GREEN);
      lcd.setCursor(0,0);
      lcd.print("AUTHORIZATION");
      lcd.setCursor(0,1);
      lcd.print("ACCEPTED");
      state = SELECTOR2;
      delay(1000);
      break;
    }
        
    char key = keypad.getKey();
  
    if (key != NO_KEY){
      Serial.println(key);
      if (key == code.charAt(entered_code.length())) {
        lcd.print(key);
        entered_code += key;
      } else {
        lcd.clear();
        lcd.setBacklight(RED);
        lcd.print("INCORRECT");
        delay(1000);
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(WHITE);
        lcd.print("ENTER AUTH CODE");
        lcd.setCursor(0,1);
        entered_code = "";
      }
    }
  }
}

void selector2() {
  pinMode(toggle_1, INPUT_PULLUP);    
  pinMode(toggle_2, INPUT_PULLUP); 
  //pinMode(toggle_3, INPUT_PULLUP); // toggle 3 wire broke, don't care to fix it, it's now a dead toggle
  pinMode(toggle_4, INPUT_PULLUP); 
  pinMode(toggle_5, INPUT_PULLUP);
  
  int toggle_1_val =  digitalRead(toggle_1);
  int toggle_2_val =  digitalRead(toggle_2);
  //int toggle_3_val =  digitalRead(toggle_3);
  int toggle_4_val =  digitalRead(toggle_4);
  int toggle_5_val =  digitalRead(toggle_5);

  if (toggle_1_val == OFF &&
    toggle_2_val == ON &&
    //toggle_3_val == ON &&
    toggle_4_val == OFF &&
    toggle_5_val == ON) {     
      state = SHUTDOWNSEQ;
      pinMode(toggle_1, INPUT);    
      pinMode(toggle_2, INPUT); 
      //pinMode(toggle_3, INPUT); 
      pinMode(toggle_4, INPUT); 
      pinMode(toggle_5, INPUT);
    }
}

void shutdownseq() {
  pinMode(red_button, INPUT_PULLUP);    // sets the digital pin 7 as input
  pinMode(blue_button, INPUT_PULLUP);    // sets the digital pin 7 as input
  pinMode(white_button, INPUT_PULLUP);    // sets the digital pin 7 as input
  pinMode(green_button, INPUT_PULLUP);    // sets the digital pin 7 as input
  pinMode(yellow_button, INPUT_PULLUP);    // sets the digital pin 7 as input

  // Inverted logic for these buttons
  int BUTTON_ON = 0;
  int BUTTON_OFF = 1;

  String code = "125431";
  String entered_code = "";

  char red_char = '1';
  char blue_char = '2';
  char white_char = '3';
  char green_char = '4';
  char yellow_char = '5';

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.setBacklight(WHITE);
  lcd.print("ENTER SHUTDOWN");
  lcd.setCursor(0,1);
  lcd.print("SEQUENCE");
  
  while(RESET_CHALLENGE == false) {
    int red_val = digitalRead(red_button);
    int blue_val = digitalRead(blue_button);
    int white_val = digitalRead(white_button);
    int green_val = digitalRead(green_button);
    int yellow_val = digitalRead(yellow_button);

    if (red_val == BUTTON_ON) {
      entered_code += red_char;
      while(digitalRead(red_button) == BUTTON_ON) {
        delay(10);
      }
    }
    if (blue_val == BUTTON_ON) {
      entered_code += blue_char;
      while(digitalRead(blue_button) == BUTTON_ON) {
        delay(10);
      }
    }
    if (white_val == BUTTON_ON) {
      entered_code += white_char;
      while(digitalRead(white_button) == BUTTON_ON) {
        delay(10);
      }
    }
    if (green_val == BUTTON_ON) {
      entered_code += green_char;
      while(digitalRead(green_button) == BUTTON_ON) {
        delay(10);
      }
    }
    if (yellow_val == BUTTON_ON) {
      entered_code += yellow_char;
      while(digitalRead(yellow_button) == BUTTON_ON) {
        delay(10);
      }
    }

    if (entered_code.length() == 6 && code.equals(entered_code)) {
      lcd.clear();
      lcd.setBacklight(GREEN);
      lcd.setCursor(0,0);
      lcd.print("SHUTDOWN SEQ");
      lcd.setCursor(0,1);
      lcd.print("ACCEPTED");
      state = SELECTOR3;
      break;
    } else if (entered_code.length() == 6) {
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(RED);
        lcd.print("INCORRECT");
        delay(1000);
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(WHITE);
        lcd.print("ENTER SHUTDOWN");
        lcd.setCursor(0,1);
        lcd.print("SEQUENCE");
      entered_code = "";
    }
  
    delay(100);
  }

  pinMode(red_button, INPUT);    // sets the digital pin 7 as input
  pinMode(blue_button, INPUT);    // sets the digital pin 7 as input
  pinMode(white_button, INPUT);    // sets the digital pin 7 as input
  pinMode(green_button, INPUT);    // sets the digital pin 7 as input
  pinMode(yellow_button, INPUT);    // sets the digital pin 7 as input
}

void selector3() {
  pinMode(toggle_1, INPUT_PULLUP);    
  pinMode(toggle_2, INPUT_PULLUP); 
  //pinMode(toggle_3, INPUT_PULLUP); // toggle 3 wire broke, don't care to fix it, it's now a dead toggle
  pinMode(toggle_4, INPUT_PULLUP); 
  pinMode(toggle_5, INPUT_PULLUP);
  
  int toggle_1_val =  digitalRead(toggle_1);
  int toggle_2_val =  digitalRead(toggle_2);
  //int toggle_3_val =  digitalRead(toggle_3);
  int toggle_4_val =  digitalRead(toggle_4);
  int toggle_5_val =  digitalRead(toggle_5);

  if (toggle_1_val == ON &&
    toggle_2_val == ON &&
    //toggle_3_val == ON &&
    toggle_4_val == OFF &&
    toggle_5_val == ON) {     
      state = KEYTURN;
      pinMode(toggle_1, INPUT);    
      pinMode(toggle_2, INPUT); 
      //pinMode(toggle_3, INPUT); 
      pinMode(toggle_4, INPUT); 
      pinMode(toggle_5, INPUT);
    }
}

void keyturn() {
  pinMode(key_1, INPUT_PULLUP);
  pinMode(key_2, INPUT_PULLUP);

  int KEY_OFF = 1;
  int KEY_ON = 0;

  while(digitalRead(key_1) == KEY_ON || digitalRead(key_2) == KEY_ON) {
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.setBacklight(RED);
      lcd.print("TURN KEYS OFF");
      delay(100);
    }

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.setBacklight(WHITE);
  lcd.print("TURN ACTIVATION");
  lcd.setCursor(0,1);
  lcd.print("KEYS");

  while(RESET_CHALLENGE == false) {
    while((digitalRead(key_1) == KEY_OFF && digitalRead(key_2) == KEY_OFF) && RESET_CHALLENGE == false) {
      delay(10);
    }

    if (RESET_CHALLENGE == true) {
      return;
    }
    
    if(digitalRead(key_1) == KEY_ON) {
      unsigned long time1 = millis();
      while(digitalRead(key_2) == KEY_OFF) {
        delay(10);
      }
      unsigned long time2 = millis();

      if(time2 - time1 < 150) {
        lcd.clear();
        lcd.setBacklight(GREEN);
        lcd.setCursor(0,0);
        lcd.print("SHUTDOWN");
        lcd.setCursor(0,1);
        lcd.print("ACTIVATED!");
        delay(1000);
        state = FLAG;
        break;
      }
      else {
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(RED);
        lcd.print("KEYS NOT TURNED");
        lcd.setCursor(0,1);
        lcd.print("SIMULTANEOUSLY");
        delay(1000);
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(WHITE);
        lcd.print("TURN ACTIVATION");
        lcd.setCursor(0,1);
        lcd.print("KEYS");
      }
    }
    else if(digitalRead(key_1) == KEY_ON) {
      unsigned long time1 = millis();
      while(digitalRead(key_1) == KEY_OFF) {
        delay(10);
      }
      unsigned long time2 = millis();

      if(time2 - time1 < 150) {
        lcd.clear();
        lcd.setBacklight(GREEN);
        lcd.setCursor(0,0);
        lcd.print("SHUTDOWN");
        lcd.setCursor(0,1);
        lcd.print("ACTIVATED!");
        delay(5000);
        state = FLAG;
        break;
      }
      else {
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(RED);
        lcd.print("KEYS NOT TURNED");
        lcd.setCursor(0,1);
        lcd.print("SIMULTANEOUSLY");
        delay(1000);
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.setBacklight(WHITE);
        lcd.print("TURN ACTIVATION");
        lcd.setCursor(0,1);
        lcd.print("KEYS");
      }
    }

    while(digitalRead(key_1) == KEY_ON || digitalRead(key_2) == KEY_ON) {
      delay(100);
    }
  }
}

void flag() {
    String flag = "BSidesPDX{Is_thi5_Re4l_or_iS_i7_a_gAm?3}";
    lcd.setCursor(0,0);
    lcd.setBacklight(WHITE);

    int charOverflow = flag.length() - 16;
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Flag:");
    
    while(RESET_CHALLENGE == false) {
      lcd.setCursor(0,1);
      lcd.print(flag.substring(0, 16));
      delay(1000);
      for(int i = 0; i <= charOverflow; i++) {
        lcd.setCursor(0,1);
        lcd.print(flag.substring(i, i+16));
        delay(500);

        if(RESET_CHALLENGE == true) {
          return;
        }
      }
      delay(1000);
    }
    
}
