const int analogPin = A0;
int sensorValue;
void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  sensorValue = analogRead(analogPin);
  Serial.print("Raw Analog Value: ");
  Serial.println(sensorValue);
  delay(500);
}