0) Install ARDUINO IDE in your system 

1) Install libraries required for recognizing ESP8266 from your ide:

    1.1)    FILE -> Preferences -> Additional board manager URL s (give below link )
            https://arduino.esp8266.com/stable/package_esp8266com_index.json
    
    1.2)    Tools -> Boards -> Board Manager
            Search for ESP8266 , the preference you have set in step 1.1 should have taken its effect 
            Click on Install 
    
    1.3)    You can select board from tools :
            Tools -> Board -> esp8266 -> Nodemcu 1.0
            Now you should be able to upload your code to esp8266


2) Now run the "y_hello_world" program to check basic LED blink
    Note : the built in LED turns on when LOW , turns off when HIGH 
