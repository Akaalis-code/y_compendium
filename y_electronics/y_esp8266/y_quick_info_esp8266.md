
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


3) BLYNK setup in ARDUINO IDE :

        Sketches -> Include libraries -> manage lirary
        Search for "Blynk"
        select the one with "volodymyr" in the name
        Install

4) WI-FI functionalities of ESP8266 :

        There are two modes here :

            Station Mode (STA):
                In this case your Board acts as a device like laptop or mobile phone which wants to connect to Internet 
                through your home wifi router.
                Once you connect to WIFI router you can read or send data to cloud or to outside world .

            Access Point Mode (AP) (or) Soft Access Point (SoftAP):
                In this mode you can make your ESP8266 as a mini router , 
                which can even host its own WEBSITE( this is one of its use cases)

            Station + Access Point Mode (STA+AP):
                This is combination of above two methods ,
                You can connect to Home router while also turing your bvoard as a router (need to check on this further)




        4.1) For Handling ID and Passwords follow below method : (Below approach is just my work around , its not a industry standard solution)

                Instead of directly giving ID and password details in .ino file ,
                Create a header file in "ARDUINO LIBRARIES" folder .
                To find where "ARDUINO LIBRARIES" folder is , follow below path :
                    File -> Preferences -> Sketchbook location
                Create a folder structure like below :
                    .                                           // Folder ( "." represents what ever folder that existed )
                        .                                       // Folder
                            .                                   // Folder
                                Arduino                         // Folder
                                    libraries                   // Folder
                                        y_my_library            // Folder
                                            y_my_library.h      // File

                Inside the .h file the content should be like this

                    #ifndef Y_SEC_H
                    #define Y_SEC_H

                    const char* MY_SSID = "what ever info";
                    const char* MY_PWD = "what ever info";

                    #endif 

                Import that header file in your .ino file and you can access them directly as variables
