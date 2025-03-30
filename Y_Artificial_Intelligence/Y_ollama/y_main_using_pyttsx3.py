################################ Summary when I come back ##

    # pyttsx3 is cutiing off the last word 

    # speech_recognition is also having an issue  like below error messages
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.surround71
        # ALSA lib setup.c:547:(add_elem) Cannot obtain info for CTL elem (MIXER,'IEC958 Playback Default',0,0,0): No such file or directory
        # ALSA lib setup.c:547:(add_elem) Cannot obtain info for CTL elem (MIXER,'IEC958 Playback Default',0,0,0): No such file or directory
        # ALSA lib setup.c:547:(add_elem) Cannot obtain info for CTL elem (MIXER,'IEC958 Playback Default',0,0,0): No such file or directory
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
        # ALSA lib pcm.c:2721:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
        # Cannot connect to server socket err = No such file or directory
        # Cannot connect to server request channel
    
    # Trying OPENAI s whisper










# from whisper_mic import WhisperMic

# mic = WhisperMic()
# result = mic.listen()
# print(result)


# from ollama import chat
# from ollama import ChatResponse

# import time


# import pyttsx3
# var_mouth = pyttsx3.init()
# var_mouth.setProperty('rate' , 120)
# var_mouth.say(" I am working properly and everything is good  ")
# var_mouth.runAndWait()

# time.sleep(5) # Wait for 1 second
# var_mouth.stop()


# import pyttsx3
 
# speaker = pyttsx3.init (debug=True)
# voices = speaker.getProperty('voices')
# speaker.setProperty('voice', 'english+f1')
# #speaker.setProperty('voice',voices[0].id)
# speaker.setProperty ('rate', 120)
# speaker.say ("I am working properly and everything is good in the situation very good")
# speaker.runAndWait ()
# speaker.stop()



# voices = var_mouth.getProperty('voices')
# for index, voice in enumerate(voices): 
#     #if 'english' in voice.name.lower():
#     print(f"Voice {index}: {voice.name}, ID: {voice.id}")
#     var_mouth.setProperty('voice', voice.id)
#     var_mouth.say(" Hello everyone")
#     var_mouth.runAndWait()


# def mth_ask_for_response(para_question):
#     response: ChatResponse = chat(model='llama3.2', messages=[
#                                                                 {
#                                                                     'role': 'user',
#                                                                     'content': 'In short , '+str(para_question),
#                                                                 },
#                                                             ]
#                                 )
#     return response



######################## To recognize audio input devices ## start #########################################################

# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

######################## To recognize audio input devices ## end #########################################################


# import speech_recognition
# var_ear = speech_recognition.Recognizer()
# var_ear.energy_threshold = 1568 

# with speech_recognition.Microphone(device_index=2) as var_mic: 
#     var_ear.adjust_for_ambient_noise(var_mic,duration = 0.2)
#     while True:
#         try: 
#             print("listening...")
#             audio_data = var_ear.listen(var_mic) 
            
#             print("Recognizing...") 
#             print(audio_data)
#             text = var_ear.recognize_google(audio_data) 
#             print(f"Recognized text: {text}") 
#         except Exception as e: 
#             print(f" error; {e}")
#             var_ear = speech_recognition.Recognizer()

## Solution  at the end by Luban6887 
    ## ref :- https://github.com/Uberi/speech_recognition/issues/100

# for i in range(5):
#     var_user_ask = input("--->>> : ")
#     var_user_ask = 'Respond in one sentence .'+ str(var_user_ask)
#     var_resp = mth_ask_for_response(str(var_user_ask))
#     #print(var_resp['message']['content'])
#     var_mouth.say(str(var_resp['message']['content']))
#     var_mouth.runAndWait()


