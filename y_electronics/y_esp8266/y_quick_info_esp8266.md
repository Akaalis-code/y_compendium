ESP8266 is a "EMBEDDED SYSTEM" , meaning its a combnation of microprocessor and RAM which has specific purpose , rather than
general purpose like general USER COMPUTERS 

--------- RESUME WORK INFO-- Start ----------------------------------------------------

Last time where I left off , I made ESP8266 as "ACCESS POINT" and host a website 
and loaded a sound file into the board  and websites's buttons should use that sound file when button is clicked .
and it was working fine with some delays when buttons were clicked , have to resume from there .

--------- RESUME WORK INFO-- Start ----------------------------------------------------

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
                Create a folder structure like below : (WINDOWS OS SETUP)
                    .                                           // Folder ( "." represents what ever folder that existed )
                        .                                       // Folder
                            .                                   // Folder (Come untill your sketch book location)
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


5) STORAGE in ESP8266 :

        Official document : https://arduino-esp8266.readthedocs.io/en/latest/filesystem.html

        It has FLASH memory (Non volatile) and RAM (Volatile) .
        Flash memory is where your code gets stored , from FLASH it will be loaded to RAM while running .
        Flash memory has a limitation on number of times we WRITE on it , after that it becomes useless , so better practice is 
        limit the number of times you write on to it .

        If you want to store some sounds or some text files in your FLASH memory , we have two file systems on esp8266 :
            SPIFFS (Serial Peripheral Interface Flash File System) : Old and depricated 
            LIFFS
        
        Tool or plugin that helps to acheive this is :
            ESP8266FS

        SPIFFS is depricated , so we will work on setting up LIFFS .

        LIFFS related plugin setup : (WINDOWS OS SETUP)
            C
                users
                    <your user name folder>
                        .arduinoIDE
                            plugins                                     // Create this folder if its not already existing 
                                arduino-littlefs-upload-1.5.4.vsix      // Download this file from below link
                                (https://github.com/earlephilhower/arduino-littlefs-upload/releases)

        Now in "Command Palette" you should be able to see the tool , press "CTRL+SHIFT+P" to open cmd pallet.

        Folder where your sketch book resides (typically the folder will also be with same name) create a "data" folder,
        inside that folder place your data file or mp3 file for sound.
        
        In cmd pallet type "Upload LittleFS to .." and click on it , that will upload the file inside data folder into 
        esp8266 flash memory .