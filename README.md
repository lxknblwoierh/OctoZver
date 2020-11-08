# OctoZver
Minimalistic, powerfull and good looking app for controlling 3D printer. Work on RPI with 3.5' LCDs to 7', with Windows and with Linux  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/start_screen.png?raw=true" width="600" height="400" />  
</p>  
Hello there. Because i didn't find any suitable app without glitches and bugs for controlling my printer with Octoprint and RPI 3B+ i wrote my own app.  
App is writen in Python 3.8.3 with Kivy 2.0.0rc4 and packed with pyinstaller for one exe file.  
Because .exe must be decompressed from --onefile, app startup with slower PC-s can be up to 10-20s  
  
### Install:  
#### Windows:  
Copy .exe and config.cfg to folder (C:\Program Files\OctoZver) or desktop (exe and cfg MUST be in same folder) and start app with double click (or make shortcut to desktop)  
#### Rpi:  
#### Ubuntu:  

### Requirements and imports:  
--- You need to install ---  
[Octoprint](https://github.com/OctoPrint/OctoPrint) with [DisplayLayerProgress plugin](https://github.com/OllisGit/OctoPrint-DisplayLayerProgress)  
    
--- You don't need to install packages bellow ---  
[Python 3.8.3](https://www.python.org/downloads/release/python-383/)  
[Kivy 2.0.0rc4](https://pypi.org/project/Kivy/2.0.0rc4/)  
[matplotlib=3.3.2](https://pypi.org/project/matplotlib/3.3.2/)  
[numpy==1.19.3](https://pypi.org/project/numpy/1.19.3/)  
[pandas=1.1.4](https://pypi.org/project/pandas/1.1.4/)  
  
#### Notes  
You need working octoprint and online connection. If your octoprint not working then app will also not work.  
Because i want provide to everyone latest version with bugfixes i implement code that connect to my server and check version.  
For now updater not work automatic and will you remind that you need newer version.  
```
def Version(self):
    link = "http://webpoint.si/version.txt"
    f = requests.get(link)
    if f.text != version:
        print("version not match")
```
Values set in config.cfg files is applyed only for work with this app. If you have diferent feed rates set in slicer then for printing will octoprint use settings from g-code!!  
  
## Print Screens with instruction  
  
This is first screen. There you select what do you want with app. You can select files for print, start heating heat bead or hotend, turn on fans, extrude and retract some filament, exit app and emergency stop printer motherboard. **If you click on Emergency Button** in top right corner then **you need reset printer** (try with reset button on printer motherboard and reconnect to octoprint or restart complete printer **with power switch**) and **restart app** because it will crash.  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/start_screen.png?raw=true" width="600" height="400" />  
</p>  
  
There you have files screen. If you had uploaded files to octoprint, there you can double click/double tap for start printing.  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/files_screen.png?raw=true" width="600" height="400" />  
</p>  
  
There you have extrude filament screen. You can extrude or retract filament if you have enough heated hotend. In top right corner is Fast/Slow icon. With icon you change extruder feed rate for faster or slower extrusion/retraction.  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/extrude_screen.png?raw=true" width="600" height="400" />  
</p>  
  
There you have extrude Control screen. You can control your printer. First you select one of 4 available distance (1mm, 10mm, 50mm, 100mm, default is 1mm) and then you can move bed to front or back, left and right and z axis up and down with click on icon. On middle is icon for homing (g28). For BLTouch is in right bottom corner mesh bed leveling (g29 command) and in right top corner you have reset BLTouch icon if you accidently screw up something with sensor.  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/control_screen.png?raw=true" width="600" height="400" />  
</p>  
  
There you have Hotend temperature screen. Function is same like with control screen but instead of distance you select one from 4 available temperature steps. Default is 1°C. With temperature up icon and temperature down icon you select temperature which is then displayed in middle of middle icon and with press on that icon you send temperature to octoprint. **If you not click on icon between temp up/temp down, then temperature is not send to printer!**  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/hote_temp_screen.png?raw=true" width="600" height="400" />  
</p>  
  
There you have Bed temperature screen. Function is same like Hotend temperature screen. **If you not click on icon between temp up/temp down, then temperature is not send to printer!**  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/bed_temp_screen.png?raw=true" width="600" height="400" />  
</p>  
  
There you have Fan speed screen. If you click one of 6 icon then you set percentage of printing fan.  
<p align="center">  
<img src="https://github.com/Matejz90/OctoZver/blob/main/print_screen/fan_screen.png?raw=true" width="600" height="400" />  
</p>  
  
