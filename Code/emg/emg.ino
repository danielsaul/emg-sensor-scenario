/* emg-sensor-scenario */

const uint8_t LED_STATUS = 13;
const uint8_t LED_PULSE = 11;
const uint8_t BTN_A = 2;
const uint8_t BTN_B = 3;
const uint8_t INPUT = A5;

long value = 0;

long zero_value = 0;

char mode = 0;

void setup() {

  Serial.begin(115200);
  Serial.println("EMG Sensor");

  pinMode(LED_STATUS, OUTPUT);
  digitalWrite(STATUS_LED_PIN, HIGH);

  pinMode(BTN_A, INPUT);
  pinMode(BTN_B, INPUT);

  delay(1000);

  for(i=0;i++;i<10;){
    zero_value += analogRead(INPUT);
    delay(100);
  }

  zero_value = zero_value/10;

}

void loop() {

  /*
  for(i=0;i++;i<10;){
    value += analogRead(INPUT);
    delay(10);
  }
  value = value/10;
  */

  value = analogRead(INPUT);

  if(value > zero_value){
    value = value - zero_value;
  }

  analogWrite(LED_PULSE, value/4);

  if(mode){

      MIDI_TX(144,value/10,127);
      delay(100);
      MIDI_TX(128,value/10,127);

  }else{

    Serial.println(value);

  }

  if(digitalRead(BTN_A)){
    mode = 0;
  }

  if(digitalRead(BTN_B)){
    mode = 1;
  }

  delay(100);

}

void MIDI_TX(unsigned char MESSAGE, unsigned char PITCH, unsigned char VELOCITY)
{
  Serial.print(MESSAGE);
  Serial.print(PITCH);
  Serial.print(VELOCITY);
}
