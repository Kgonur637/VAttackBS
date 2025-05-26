import sys
from ppadb.client import Client as AdbClient

# Connect to ADB
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

#Mapping commands to one or two-letter inputs decreases input delay. If you want to decrease it further, then lower the delay between keys in VoiceAttack

#left, right, up, down, uleft, urignt, dleft, dright, shoot(attack), super, aimed attack (for tutorial)
tap_map = {
    'l': (358,804, 300, 804),
    'r': (358,804, 408, 804),
    'u':(358,804, 358, 756),
    'd':(358,804, 358, 855),
    'ul':(358,804,300,756),
    'ur':(358,804,408,756),
    'dl':(358,804,300,855),
    'dr':(358,804,408,855),
    'a':(1955,655),
    's': (1642,784),
    'ps': (1642,784,1642,850)


}
while True:
    command = input()
    if command in tap_map:
        try:
            x1, y1, x2, y2= tap_map[command]
            print("swipe")
            device.input_swipe(x1,y1,x2,y2,2000)
        except:
            x1, y1 = tap_map[command]
            print("tap")
            device.input_tap(x1, y1)
    else:
        print(f"Unknown command: {command}")
