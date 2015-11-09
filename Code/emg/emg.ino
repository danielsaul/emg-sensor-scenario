/* emg-sensor-scenario */
/* Daniel Saul */

//#include <MIDI.h>

//MIDI_CREATE_DEFAULT_INSTANCE();

const uint8_t LED_STATUS = 13;
const uint8_t LED_PULSE = 11;
const uint8_t BTN_A = 2;
const uint8_t BTN_B = 3;
const uint8_t INPUTPIN = A5;

long value = 0;

long zero_value = 0;

char mode = 0;

void setup() {

  Serial.begin(57600);
  Serial.println("EMG Sensor");

  //MIDI.begin(4);

  pinMode(LED_STATUS, OUTPUT);
  digitalWrite(LED_STATUS, HIGH);

  pinMode(BTN_A, INPUT);
  pinMode(BTN_B, INPUT);

  delay(1000);

  for(int i=0;i++;i<10){
    zero_value += analogRead(INPUTPIN);
    delay(10);
  }

  zero_value = zero_value/10;

}

void loop() {


/*  for(int i=0;i++;i<10){
    value += analogRead(INPUTPIN);
    delay(10);
  }
  value = value/10;
  */


  value = analogRead(INPUTPIN);

  if(value > zero_value){
    value = value - zero_value;
  }else{
    value = 0;
  }

  analogWrite(LED_PULSE, value/4);

  // MIDI Mode
  if(mode){

      //MIDI.sendNoteOn(value/10,127,1);
      //delay(100);
      //MIDI.sendNoteOff(value/10,127,1);

  // Serial Mode
  }else{

    Serial.println(value);

  }

  if(digitalRead(BTN_A)){
    // Serial mode
    mode = 0;
  }

  if(digitalRead(BTN_B)){
    // MIDI mode
    mode = 1;
  }


}
