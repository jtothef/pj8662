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

cycles = 100
endTime = 0.00
beginTime = 0.00
totalTime = 0.00
oneCycle = 0.00
for i in range(cycles):
    beginTime = time.time()
    requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(on))
    print
    "turning bulb on.."
    time.sleep(0.03)
    requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(off))
    print
    "turning bulb off.."
    time.sleep(0.03)
    endTime = time.time()
    oneCycle = endTime - beginTime
    print
    "seconds passed: "
    print
    oneCycle
    totalTime = oneCycle + totalTime
print
"Total seconds elapsed: "
print
totalTime
print
"Total cycles: "
print
cycles
