import time
from random import randint

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

def ttr():

    if keys.hue_api and keys.hue_ip:
        d = {"on": True, "transitiontime":0, "bri": 255, "sat": 255, "hue": randint(0, 65280)}
        requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/groups/0/action', json.dumps(d))
        # groups are slower than individual lights. Using a group to turn on all lights only

        while not keys.stop_ttr:
            requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/lights/1/state', json.dumps(randomColor()))
            requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/lights/2/state', json.dumps(randomColor()))
            requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/lights/3/state', json.dumps(randomColor()))
            requests.put('http://' + keys.hue_ip + '/api/' + keys.hue_api + '/lights/4/state', json.dumps(randomColor()))
            #need to repeat for all lights, I just went up to 4
            print("sent...")
            time.sleep(0.05)
        keys.ttr_running = False
    else:
        print("IP or API key not yet found")

def randomColor():
    return {"on": True, "transitiontime":0, "bri": 255, "sat": 255, "hue": randint(0, 65280)}