#!/usr/bin/env python
import requests
import json
import time

hue_ip = ""
api_key = ""


#turn lights off or on variables
#transitiontime needed to create strobe effect. It might be removed by Philips later.
on = {
		"on": True, "transitiontime":0, "bri": 254
	}
off = {
		"on": False, "transitiontime":0, "bri": 254
	}

#Making this into a class later. First phase of discomfort:

for i in range(9):

	requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(on))
	print "turning on.."
	time.sleep(0.05)
	
	requests.put('http://' + hue_ip + '/api/' + api_key + '/lights/3/state', json.dumps(off))
	print "turning off.."
	time.sleep(0.05)
