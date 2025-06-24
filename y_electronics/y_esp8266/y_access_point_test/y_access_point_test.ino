#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <y_sec.h> // this is my custom library

// Set your Access Point's SSID and password
const char* ap_ssid = MY_SSID;
const char* ap_pwd = MY_PWD; 


// Serving websites section // START
ESP8266WebServer server(80);

void handleRoot()
{
  String html = "<html><head>";
  // *** NEW: Viewport Meta Tag - Crucial for mobile scaling ***
  html += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">";
  html += "<title>ESP8266 LED Control</title>"; // Added a title for the page
  html += "<style>";
  // *** NEW: Basic CSS for sizing and styling ***
  html += "body { font-family: Arial, sans-serif; text-align: center; margin: 20px; background-color: #f0f0f0; }";
  html += "h1 { font-size: 2.5em; color: #333; margin-bottom: 30px; }";
  html += "p { font-size: 1.8em; color: #555; margin-bottom: 20px; }";
  html += "button {";
  html += "  display: inline-block;"; // Make buttons behave like blocks for easier styling
  html += "  padding: 20px 40px;"; // Larger padding for bigger buttons
  html += "  font-size: 2em;"; // Larger font size for button text
  html += "  margin: 15px;"; // Spacing between buttons
  html += "  cursor: pointer;";
  html += "  border: none;";
  html += "  border-radius: 10px;";
  html += "  background-color: #007bff;";
  html += "  color: white;";
  html += "  box-shadow: 0 4px 6px rgba(0,0,0,0.1);";
  html += "  transition: background-color 0.3s ease;"; // Smooth transition on hover
  html += "}";
  html += "button:hover { background-color: #0056b3; }";
  html += "a { text-decoration: none; }"; // Remove underline from links inside buttons
  html += "</style>";
  html += "</head><body>"; // Close head, open body

  html += "<h1>ESP8266 LED Control</h1>";
  html += "<p>LED is ";
  // Corrected logic for active-low LED_BUILTIN status display
  if (digitalRead(LED_BUILTIN) == LOW)
  {
    html += "ON";
  } else
  {
    html += "OFF";
  }
  html += "</p>";
  html += "<a href=\"/on\"><button>TURN ON</button></a> "; // Use escaped quotes for href
  html += "<a href=\"/off\"><button>TURN OFF</button></a>"; // Use escaped quotes for href
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
    Serial.print("Setting up Access Point: ");
    Serial.println(ap_ssid);

    // Set the ESP8266 to Access Point mode
    WiFi.mode(WIFI_AP);
    // Start the Access Point
    if (WiFi.softAP(ap_ssid, ap_pwd))
    {
      Serial.println("Access Point created successfully!");
      Serial.print("AP IP Address: ");
      Serial.println(WiFi.softAPIP());
      Serial.print("SSID: ");
      Serial.println(ap_ssid);
      Serial.print("Pwd: ");
      Serial.println(ap_pwd);
    } else
    {
      Serial.println("Failed to create Access Point.");
    }
    server.on("/", handleRoot);
    server.on("/on", handleOn);
    server.on("/off", handleOff);

    server.begin();
    Serial.println("HTTP server started");
}

void loop()
{
  server.handleClient();
}