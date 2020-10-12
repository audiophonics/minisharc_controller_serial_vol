#!/usr/bin/python2
# coding: utf-8
# AUDIOPHONICS Minisharc Serial Sync script
# 
# Linked to ALSA card #1
# Change card number if needed
# The I2S audio data must not be affected by ALSA value

import time , serial
import subprocess
import os

#ALSA / Volumio Volume Value
def Getvolume():
#       amixervol = "amixer -c 1 | tail -1 | cut -d'[' -f2 | cut -d '%' -f1"
        amixervol = "volumio volume"
        process = subprocess.Popen(amixervol, stdout=subprocess.PIPE , shell=True)
        os.waitpid(process.pid, 0)[1]
        volcut = process.stdout.read().strip()
        volume = volcut[0:12]
        return (volume)



if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyAMA0', 2400)
        save = Getvolume()

        try:
                while True:
                        volume = Getvolume()
                        send = str(volume) + "-"
                        if save != volume:
                                ser.write(send.encode('utf-8'))
                                save = volume
                                print(send)
                        time.sleep(0.1)
        except KeyboardInterrupt:
                time.sleep(0.1)
time.sleep(0.1)
