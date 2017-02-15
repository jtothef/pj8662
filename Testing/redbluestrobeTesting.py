#!/usr/bin/env python
import requests
import json
import time

hue_ip = ""
api_key = ""

# turn lights off or on variables
on = {
    "on": True, "transitiontime": 0, "bri": 254
}
off = {
    "on": False, "transitiontime": 0, "bri": 254
}
red = {"on":True, "transitiontime": 0,"bri":255,"sat":255,"hue":0}
blue= {"on": True ,"transitiontime": 0, "bri": 255, "sat": 255, "hue": 46920}
isRed = False

cycles = 100
endTime = 0.00
beginTime = 0.00
totalTime = 0.00
oneCycle = 0.00
for i in range(cycles):
    beginTime = time.time()
    if isRed:
        requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(blue))
        #requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/2/state', json.dumps(blue))
        isRed = False
    else:
        requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(red))
        #requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/2/state', json.dumps(red))
        isRed = True

    print("turning bulb on..")
    time.sleep(0.03)
    requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(off))
    #requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/2/state', json.dumps(off))

    print("turning bulb off..")
    time.sleep(0.03)
    endTime = time.time()
    oneCycle = endTime - beginTime
    print("seconds passed: ")
    print(oneCycle)
    totalTime = oneCycle + totalTime
print("Total seconds elapsed: ")
print(totalTime)
print("Total cycles: ")
print(cycles)
