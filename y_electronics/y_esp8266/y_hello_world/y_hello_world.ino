void setup() 
{
  // Initialize digital pin LED_BUILTIN as an output.
  // On NodeMCU, LED_BUILTIN usually maps to GPIO 2.
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() 
{
  Serial.println(LED_BUILTIN);
  Serial.println("test");
  digitalWrite(2, LOW);   // Turn the LED on (LOW because it's usually active-low)
  delay(5000);                      // Wait for a second
  digitalWrite(2, HIGH);  // Turn the LED off
  delay(2000);                      // Wait for a second
}