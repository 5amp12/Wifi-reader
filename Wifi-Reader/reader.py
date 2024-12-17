#!/usr/bin/python3

import subprocess
import re
import time

def get_wifi_signal():

    while True:
        cmd = 'netsh wlan show interfaces'
        output = subprocess.check_output(cmd, shell=True).decode()
        signal_output = re.search(r'Signal\s*:\s*(\d+)%', output)
        BSSID_output = re.search(r'BSSID\s*:\s*(.*)', output)
        signal_number = signal_output.group(1)
        BSSID_number = BSSID_output.group(1)
        dbm = ((int(signal_number) / 2) - 100)
        if (dbm <= -30) and (dbm >= -50):
            print(f"{dbm} dBm : Excellent           BSSID : {BSSID_number}")
        elif (dbm <= -51) and (dbm >= -60):
            print(f"{dbm} dBm : Good                BSSID : {BSSID_number}")
        elif (dbm <= -61) and (dbm >= -70):
            print(f"{dbm} dBm : Moderate            BSSID : {BSSID_number}")
        elif(dbm <= -71) and (dbm >= -80):
            print(f"{dbm} dBm : Weak                BSSID : {BSSID_number}")
        elif (dbm <= -81) and (dbm >= -90):
            print(f"{dbm} dBm : Very Poor           BSSID : {BSSID_number}")

        time.sleep(3)



    


get_wifi_signal()

