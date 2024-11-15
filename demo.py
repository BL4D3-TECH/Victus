import speech_recognition as sr
r = sr.Recognizer()
while True:
    with sr.Microphone(device_index=1) as source:
        print("setting")
        audio = r.listen(source)
        print("setted")
    text = r.recognize_google(audio, language="es")
    print("recibido:", text)