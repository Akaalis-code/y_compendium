# Goal :
    There is an Databricks AI endpoint being served .
    Now you have to use that end point and connect to your local system .
    GENAI model is in databricks cloud , Talk to it from your local computer .


# Setup in your local system :

    - INSTALL OPENAI library :
        - Create a virtual environment for installing these libs , as System level python doesnt allow to install new libs
            > sudo apt install python3.12-venv          ## To install venv into your system
            > python3 -m venv y_AI_ENV                  ## Create an vitual env 
            > cd y_AI_ENV/bin/                          ## Your activate and deactivate files for venv are present here
            > source activate                           ## Activate the venv "my_env" 
            (my_env) > deactivate                       ## This a shell function inside activate file , to comeout of venv
    
        - Install the OPENAI lib :
            > pip install openai

# Script for using it as a chatbot :

from openai import OpenAI
import os

var_client = OpenAI(
                        api_key='1234',
                        base_url="https://adb-394592958571649.9.azuredatabricks.net/serving-endpoints"
                    )

while True:
    var_user_prompt = input("Your prompt message here: ")
    if var_user_prompt == 'y_done':
        break
    var_response = var_client.chat.completions.create   (
                                                            model="y_endpoint_2",
                                                            messages=   [
                                                                            {
                                                                                "role": "user",
                                                                                "content": var_user_prompt
                                                                            }
                                                                        ],
                                                            max_tokens=5000
                                                        )

    print(var_response.choices[0].message.content)

print('Thank you for chatting')