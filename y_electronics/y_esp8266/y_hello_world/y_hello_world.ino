void setup() {
  // Initialize digital pin LED_BUILTIN as an output.
  // On NodeMCU, LED_BUILTIN usually maps to GPIO 2.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, LOW);   // Turn the LED on (LOW because it's usually active-low)
  delay(5000);                      // Wait for a second
  digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED off
  delay(2000);                      // Wait for a second
}