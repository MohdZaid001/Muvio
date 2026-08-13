import speech_recognition as sr

def voice_input():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Background noise filteration
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)  
        try:
            text = recognizer.recognize_google(audio, language="en-IN")
            return text
            
        except sr.UnknownValueError:
            #print("Please type or speak something to continue.")
            return " "
        except sr.RequestError:
            print("Please, Check your internet connection,")
            return " "
