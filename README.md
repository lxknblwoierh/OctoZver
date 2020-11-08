# OctoZver
App for controlling 3D printer. Work on RPI, Windows, Linux  
  
Hello there. Because i didn't find any suitable app for controlling my printer with Octoprint and RPI 3B+ i wrote myself.  
App is writen in Python 3.8.3 with Kivy 2.0.0rc4 and packed with pyinstaller for one file.  
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
