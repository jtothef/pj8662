import time
import requests
import json
import keys


def lightsout():

    if keys.hue_api and keys.hue_ip:
        d = {
                'on': False
                }

        while not keys.stop_lightsout:
            p = requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/groups/0/action', json.dumps(d))
            print("sent...")
            time.sleep(3)
        keys.lightsout_running = False
    else:
        print("IP or API key not yet found")

def setColor(color):

    if keys.hue_api and keys.hue_ip:
        d = ""
        if color is "red":
            d = {"on":True,"bri":255,"sat":255,"hue":0}
        if color is "blue":
            d = {"on": True, "bri": 255, "sat": 255, "hue": 46920}
        if d:
            p = requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/groups/0/action', json.dumps(d))
            print("sent...")
            time.sleep(3)
    else:
        print("IP or API key not yet found")