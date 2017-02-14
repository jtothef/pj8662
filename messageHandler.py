import threading

import hueController
import huescanner
import keys
import twitterSender

huescanthread = threading.Thread(target=huescanner.scan)
lightsoutthread = threading.Thread(target=hueController.lightsout)
ttrthread = threading.Thread(target=hueController.ttr)

def handlemessage(message):
    if 'how are you' in message:
        twitterSender.sendmessage("hey, I'm good!")
    elif 'do you have any candy' in message:
        if "" is keys.hue_api:
            twitterSender.sendmessage("No, I don't have any yet.")
        if "" is not keys.hue_api:
            twitterSender.sendmessage("yeah, I have some skittles.")
    elif 'buy me some skittles' in message:

        if keys.hue_scanner_running:
            twitterSender.sendmessage("Hold your horses! I'm still looking for some!")
        elif "" is keys.hue_api:
            twitterSender.sendmessage("okay, I'll try to pick up some skittles.")
            keys.hue_scanner_running = True
            huescanthread.start()
        else:
            twitterSender.sendmessage("I already have some")
    elif 'the red ones' in message:
        if keys.hue_ip and keys.hue_api:
            hueController.setColor("red")
            twitterSender.sendmessage("Nice! I like red too :)")
        else:
            twitterSender.sendmessage("I can't help you with that")
    elif 'the blue ones' in message:
        if keys.hue_ip and keys.hue_api:
            hueController.setColor("blue")
            twitterSender.sendmessage("Nice! I like blue too :)")
        else:
            twitterSender.sendmessage("I can't help you with that")
    elif 'the black ones' in message:
        if keys.hue_ip and keys.hue_api and not keys.lightsout_running:
            keys.stop_lightsout = False
            keys.lightsout_running = True
            twitterSender.sendmessage("Black skittles it is! ;)")
            lightsoutthread.start()
        else:
            twitterSender.sendmessage("I can't help you with that")
    elif 'the white ones' in message:
        if keys.hue_ip and keys.hue_api:
            keys.stop_lightsout = True
            twitterSender.sendmessage("White it is!")
        else:
            twitterSender.sendmessage("I can't help you with that")
    elif 'taste the rainbow' in message:
        if keys.hue_ip and keys.hue_api and not keys.ttr_running:
            keys.stop_ttr = False
            keys.ttr_running = True
            twitterSender.sendmessage("Yummy yummy yummy time :)")
            ttrthread.start()
        else:
            twitterSender.sendmessage("I can't help you with that")
    elif 'sunny day' in message:
        if keys.hue_ip and keys.hue_api:
            keys.stop_ttr = True
            twitterSender.sendmessage("Not even a cloud in the sky!")
        else:
            twitterSender.sendmessage("I can't help you with that")


