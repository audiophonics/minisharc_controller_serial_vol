# minisharc_controller_serial_vol
Python Script to Serial sync ALSA volume with Audiophonics Minisharc Controller

Works with Audiophonics I-sabre 9038Q2M driver / tested on RPI3 & Volumio

## Installation :
Remove console=serial0,115200 from /boot/cmdline.txt

Add dtoverlay=pi3-disable-bt to /boot/config.txt

It will free the RPI serial port
```
apt-get update
apt-get install python-serial 
reboot
```

Copy Python and service files. (wget or WinSCP)

Try to launch the python file :

```
python minisharc_serial_sync.py
```

You should see volume value printed in bash when changed from ALSA, and if serial is received, Minisharc Controller should update the volume value.

Then install the service so it's launched at startup :
```
cp minisharc_serial_sync.py /usr/local/bin/minisharc_serial_sync.py
chmod +x /usr/local/bin/minisharc_serial_sync.py
sudo cp minisharc_volume.service /etc/systemd/system
systemctl enable minisharc_volume.service
```
