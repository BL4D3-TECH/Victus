import speech_recognition as sr
import webbrowser
import subprocess
import Spotify_control
import pyautogui as pgui

r = sr.Recognizer() 
ordenes = [("victus abre google", "victus abre chrome"), "victus abre youtube", ("victus abre visual studio code", "victus abre vs code", "victus abre vscode", "victus abre visual", "victus abre visual estudio"),
("victus entra en game mode", "victus entra en modo gaming", "victus a jugar", "victus vamos a jugar"), ("victus abre spoti", "victus abre spotify"), "victus siguiente canción",
 "victus cancion anterior", ("victus para la canción", "victus para la música"), ("victus sigue la canción", "victus sigue la música"), "victus sube el volumen", "victus baja el volumen",
 ("victus apaga el pc", "victus apágate"), ("victus", "escribe")]

VScode = ""
Spotify = ""
Discord = ""
device_id, sp = Spotify_control.Spotify()

while True:
    with sr.Microphone(device_index=None) as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es")
        if text.lower() in ordenes[0]:
            webbrowser.open("https://google.com", new=1, autoraise=True)
        elif text.lower() == ordenes[1]:
            webbrowser.open("https://youtube.com", new=1, autoraise=True)
        elif text.lower() in ordenes[2]:
            subprocess.run(VScode)
        elif text.lower() in ordenes[3]:
            subprocess.run(Discord, shell=True)
            subprocess.run(Spotify)
        elif text.lower() in ordenes[4]:
            subprocess.run(Spotify)
        elif text.lower() == ordenes[5]:
            Spotify_control.next(sp, device_id)
        elif text.lower() == ordenes[6]:
            Spotify_control.previous(sp, device_id)
        elif text.lower() in ordenes[7]:
            Spotify_control.pause(sp, device_id)
        elif text.lower() in ordenes[8]:
            Spotify_control.start(sp, device_id)
        elif text.lower() == ordenes[9]:
            devices_lst = Spotify_control.devices(sp)
            volumen = Spotify_control.volume(devices_lst)
            Spotify_control.change_volume(sp, device_id, devices_lst, volumen, 5)
        elif text.lower() == ordenes[10]:
            devices_lst = Spotify_control.devices(sp)
            volumen = Spotify_control.volume(devices_lst)
            Spotify_control.change_volume(sp, device_id, devices_lst, volumen, -5)
        elif text.lower() in ordenes[11]:
            subprocess.run("shutdown /p", shell=True)
        elif ordenes[12][0] in text.lower().split(sep=" ") and ordenes[12][1] in text.lower().split(sep=" "):
            clean_list = text.split(sep=" ")
            clean_list.pop(0)
            clean_list.pop(0)
            clean_text = "".join(f"{x} " for x in clean_list)
            pgui.write(clean_text)
    except sr.exceptions.UnknownValueError:
        r = sr.Recognizer()
        continue