## This is a Tutorial

---

> This used "Kian Brose" [_video as a base_](https://www.youtube.com/watch?v=YRAIUA-Oc1Y).

This is a tutorial for installing and using the code, shall be used in your own risk.

---

1. First install [_Python_](https://www.python.org/downloads/).

> Mark the "add python.exe to PATH"

![alt text](Python_download.png)

2. Open CMD with ADM privilege to instal with PIP command, list below:
```
pip install pyinstaller
pip install pyautogui
pip install time
pip install pyinstaller
pip install keyboard
pip install random
pip install pywin32
```
> if you get any error, install pillow
>
> Pynput verify if the mouse was pressed

```
pip install Pillow 
pip install pynput
```
3. You can also create .exe file with the following code:

```
pyinstaller --onefile YOUR_ARCHIVE.py
```

4. Or you can run locally:
```
python YOUR_ARCHIVE.py
```

> Can update python pip if wanted, but not required, command will be: python.exe ```-m pip install```  ```--upgrade pip```

3. After this, you shall use the rest of the code or just do whatever you want with it.

4. To use the libraries you installed above:

```
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
```