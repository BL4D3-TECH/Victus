import speech_recognition as sr
import webbrowser
import subprocess
import Spotify_control
import pyautogui as pgui

r = sr.Recognizer() 
ordenes = [("lara abre google", "lara abre chrome"), "lara abre youtube", ("lara abre visual studio code", "lara abre vs code", "lara abre vscode", "lara abre visual", "lara abre visual estudio"),
("lara entra en game mode", "lara entra en modo gaming", "lara a jugar", "lara vamos a jugar"), ("lara abre spoti", "lara abre spotify"), "lara siguiente canción",
 "lara cancion anterior", ("lara para la canción", "lara para la música"), ("lara sigue la canción", "lara sigue la música"), ("lara", "sube", "el", "volumen"), ("lara", "baja", "el", "volumen"),
 ("lara apaga el pc", "lara apágate"), ("lara", "escribe")]

VScode = "C:/Users/Alberto/AppData/Local/Programs/Microsoft VS Code"
Spotify = "C:/Users/Alberto/AppData/Roaming/Spotify/Spotify.exe"
Discord = "C:/Users/Alberto/AppData/Local/Discord/Update.exe --processStart Discord.exe"
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
        elif text.lower().split()[0] == ordenes[10][0] and text.lower().split()[1] == ordenes[10][1] and text.lower().split()[2] == ordenes[10][2] and text.lower().split()[3] == ordenes[10][3]:
            devices_lst = Spotify_control.devices(sp)
            volumen = Spotify_control.volume(devices_lst)
            Spotify_control.change_volume(sp, device_id, devices_lst, volumen, 0 - int(text.split()[-1]))
        elif text.lower() in ordenes[11]:
            subprocess.run("shutdown /p", shell=True)
        elif ordenes[12][0] in text.lower().split(sep=" ") and ordenes[12][1] in text.lower().split(sep=" "):
            clean_list = text.split(sep=" ")
            clean_list.pop(0)
            clean_list.pop(0)
            clean_text = "".join(f"{x} " for x in clean_list)
            pgui.write(clean_text)
        print(text)
    except sr.exceptions.UnknownValueError:
        r = sr.Recognizer()
        print("not understanded")
        continue