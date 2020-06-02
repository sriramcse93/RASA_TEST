import speech_recognition as speech

recog = speech.Recognizer()
with speech.Microphone() as sourcetext:
    print("Speech something...")
    audio = recog.listen(sourcetext)
    try:
        text = recog.recognize_google(audio)
        print("You Said{}: ".format(text) )
    except:
        print("Sorry can't get you")

