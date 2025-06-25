#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <LittleFS.h> // <--- RE-ADDED: Include LittleFS library
#include <y_sec.h>    // this is my custom library

// Access Point (AP) Configuration - for the network the ESP8266 creates
const char* ap_ssid = MY_SSID;
const char* ap_pwd = MY_PWD;

// Station (STA) Configuration - for connecting to your home Wi-Fi
const char* sta_ssid = STA_SSID;
const char* sta_pwd = STA_PWD;

// Serving websites section // START
ESP8266WebServer server(80);

void handleRoot()
{
  String html = "<html><head>";
  html += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">";
  html += "<title>ESP8266 LED Control</title>";
  html += "<style>";
  html += "body { font-family: Arial, sans-serif; text-align: center; margin: 20px; background-color: #f0f0f0; }";
  html += "h1 { font-size: 2.5em; color: #333; margin-bottom: 30px; }";
  html += "p { font-size: 1.8em; color: #555; margin-bottom: 20px; }";
  html += "button {";
  html += "   display: inline-block;";
  html += "   padding: 20px 40px;";
  html += "   font-size: 2em;";
  html += "   margin: 15px;";
  html += "   cursor: pointer;";
  html += "   border: none;";
  html += "   border-radius: 10px;";
  html += "   background-color: #007bff;";
  html += "   color: white;";
  html += "   box-shadow: 0 4px 6px rgba(0,0,0,0.1);";
  html += "   transition: background-color 0.3s ease;";
  html += "}";
  html += "button:hover { background-color: #0056b3; }";
  html += "a { text-decoration: none; }";
  html += "</style>";

  // JavaScript for playing sound from the NodeMCU's filesystem
  html += "<script>";
  html += "var clickSound = new Audio('/y_simple_button_1.mp3');"; // Path to file on NodeMCU's filesystem
  html += "function playClickSound() {";
  html += "  clickSound.currentTime = 0;"; // Rewind to start if already playing
  html += "  clickSound.play()";
  html += "  .then(() => console.log('Sound played successfully'))"; // <--- Add for console feedback
  html += "  .catch(e => console.error('Sound play error:', e));"; // <--- Add for console feedback
  html += "}";
  html += "</script>";

  html += "</head><body>";

  html += "<h1>ESP8266 LED Control</h1>";
  html += "<p>LED is ";
  if (digitalRead(LED_BUILTIN) == LOW)
  {
    html += "ON";
  } else
  {
    html += "OFF";
  }
  html += "</p>";
  html += "<a href=\"/on\"><button onclick=\"playClickSound()\">TURN ON</button></a> ";
  html += "<a href=\"/off\"><button onclick=\"playClickSound()\">TURN OFF</button></a>";
  html += "<br><br>"; // Add some spacing

  // <--- NEW: Test Sound Button (no redirect)
  html += "<button onclick=\"playClickSound()\">TEST SOUND ONLY</button>";
  html += "<br><br>"; // Add some spacing

  html += "<p>AP IP: ";
  html += WiFi.softAPIP().toString();
  html += "</p>";
  html += "<p>STA IP: ";
  html += WiFi.localIP().toString();
  html += "</p>";
  html += "</body></html>";
  server.send(200, "text/html", html);
}

void handleOn()
{
  digitalWrite(LED_BUILTIN, LOW); // LOW turns active-low LED ON
  server.sendHeader("Location", "/"); // Redirect back to the root page
  server.send(303); // HTTP 303 See Other
}

void handleOff()
{
  digitalWrite(LED_BUILTIN, HIGH); // HIGH turns active-low LED OFF
  server.sendHeader("Location", "/"); // Redirect back to the root page
  server.send(303); // HTTP 303 See Other
}
//Serving websites section // END

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT); // Set LED pin as output
  digitalWrite(LED_BUILTIN, HIGH); // Set initial state to OFF (for active-low LED)

  Serial.begin(9600);
  delay(2000); // Give Serial some time to initialize
  Serial.println();

  // Initialize LittleFS filesystem
  if (!LittleFS.begin()) { // <--- RE-ADDED: Initialize LittleFS
    Serial.println("An Error has occurred while mounting LittleFS");
    return; // Stop if filesystem fails to mount
  }
  Serial.println("LittleFS mounted successfully");


  // Set the ESP8266 to Access Point + Station mode
  Serial.println("Setting up WiFi in AP+STA mode...");
  WiFi.mode(WIFI_AP_STA);

  // --- Start Station (STA) Mode Connection ---
  Serial.print("Connecting to STA: ");
  Serial.println(sta_ssid);
  WiFi.begin(sta_ssid, sta_pwd);

  int retries = 0;
  while (WiFi.status() != WL_CONNECTED && retries < 20) { // Try to connect for ~10 seconds
    delay(500);
    Serial.print(".");
    retries++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnected to STA successfully!");
    Serial.print("STA IP Address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nFailed to connect to STA. Will proceed with AP only.");
  }

  // --- Start Access Point (AP) Mode ---
  Serial.print("Setting up Access Point: ");
  Serial.println(ap_ssid);
  if (WiFi.softAP(ap_ssid, ap_pwd))
  {
    Serial.println("Access Point created successfully!");
    Serial.print("AP IP Address: ");
    Serial.println(WiFi.softAPIP());
    Serial.print("AP SSID: ");
    Serial.println(ap_ssid);
    Serial.print("AP Pwd: ");
    Serial.println(ap_pwd);
  } else
  {
    Serial.println("Failed to create Access Point.");
  }

  server.on("/", handleRoot);
  server.on("/on", handleOn);
  server.on("/off", handleOff);

  // <--- RE-ADDED: Handler for the sound file from LittleFS
  server.on("/y_simple_button_1.mp3", HTTP_GET, [](){
    if(LittleFS.exists("/y_simple_button_1.mp3")){
      File soundFile = LittleFS.open("/y_simple_button_1.mp3", "r");
      server.streamFile(soundFile, "audio/mpeg"); // Use audio/mpeg for MP3
      soundFile.close();
    } else {
      server.send(404, "text/plain", "y_simple_button_1.mp3 not found on ESP8266");
    }
  });


  server.begin();
  Serial.println("HTTP server started");
}

void loop()
{
  server.handleClient();
}