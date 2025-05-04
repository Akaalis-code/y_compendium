
from ollama import chat
from ollama import ChatResponse


def mth_ask_for_response(para_question):
    response: ChatResponse = chat(model='llama3.2', messages=[
                                                                {
                                                                    'role': 'user',
                                                                    'content': 'In short , '+str(para_question),
                                                                },
                                                            ]
                                )
    return response

###############################################################################################################################################

from gtts import gTTS
import pygame
import io

pygame.mixer.init()

language = 'en'


def mth_speak(para_text_to_be_spoken):

    speech = gTTS(text=para_text_to_be_spoken, lang=language, slow=False ,tld="co.in")

    speech_fp = io.BytesIO()
    speech.write_to_fp(speech_fp)
    speech_fp.seek(0)

    pygame.mixer.music.load(speech_fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue



for i in range(5):
    var_user_ask = input("--->>> : ")
    var_user_ask = 'Respond with concise answer .'+ str(var_user_ask)
    var_resp = mth_ask_for_response(str(var_user_ask))
    #print(var_resp['message']['content'])
    mth_speak(str(var_resp['message']['content']))