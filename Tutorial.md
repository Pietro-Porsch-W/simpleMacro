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
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
```
> Caso de erro ao pegar a posição do mouse instale o pillow
>
> Pynput verifica se o mouse foi pressionado

```
pip install Pillow 
pip install pynput
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