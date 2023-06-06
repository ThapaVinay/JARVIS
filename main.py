'''
We need the following packages to start -> 
1. speechrecognition
2. wikipedia
3. openai
4. pyaudio  {for this first install portaudio}

'''


import speech_recognition as sr
import os
import webbrowser
import openaitext as ai
import datetime
import openai
from config import apikey

chatStr = ""
def chat(query):

    global chatStr
    openai.api_key = apikey

    chatStr += f"Harry : {query} \n Jarvis :"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= chatStr,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    try:
        chatStr += f"{response['choices'][0]['text']}\n"
        print(chatStr)
        say(response['choices'][0]['text'])
        return response['choices'][0]['text']

    except Exception as e:
        print("Error occured !", e)


def say(text):
    os.system(f'say "{text}"')   # say command is used to convert text to speech , we need to install it

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something ...")
        r.pause_threshold = 0.5   # 0.8 is default
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Sorry I didn't catch that."



if __name__ == '__main__':  # it will only be executed when this file is directly run
    say("JARVIS A.I")
    while True :
        print("Listening ..... ")
        query = takeCommand()

        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["animepahe", "https://animepahe.org"]]

        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]} sir ..")
                webbrowser.open(site[1])
        
        if "open music" in query.lower():
            musicPath = "/home/lonewolf/Downloads/AnimePahe_One_Piece_-_972_720p_SubsPlease.mp4"
            os.system(f"open {musicPath}")

        elif "time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        elif "artificial intelligence" in query.lower():
            ai.ai(query)

        elif "jarvis stop" in query.lower():
            exit()
        
        elif "reset chat" in query.lower():
            chatStr = ""

        elif "sorry" in query.lower():
            say(query)

        else:
            print("Chatting")
            chat(query)