import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

def Spotify():
    '''
    Returns a sp object and an device_id string
    (device_id, sp)
    '''
    client_id = "fd64c6589c264871912e94e8542edd60"
    client_secret = "8370b736b8224a10b9de1044bc4bb9da"
    redirect_uri = "http://localhost:8888/callback"
    scope = ["user-read-playback-state", "user-modify-playback-state", "user-read-currently-playing"]
    device_id = "ede8504eff57e8da64c3dcda52530d6e72567cc9"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri, 
                                                   scope=scope))
    return device_id, sp

def devices(sp):
    devices_lst = sp.devices()
    return devices_lst
def pause(sp, device_id):
    try:
        sp.pause_playback(device_id=device_id)
    except:
        pass
def start(sp, device_id):
    try:
        sp.start_playback(device_id=device_id)
    except:
        pass
def next(sp, device_id):
    sp.next_track(device_id=device_id)
def previous(sp, device_id):
    sp.previous_track(device_id=device_id)
def volume(devices):
    volumen = devices['devices'][0]['volume_percent']
    return volumen
def change_volume(sp, device_id, devices_lst, volumen, change):
    volume_percent = volumen + change
    sp.volume(volume_percent, device_id)