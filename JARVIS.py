import pyttsx3


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__=="__main__":
    speak("helo")
"""def wishme():
    speak("hello swarupam this is jarvis")"""