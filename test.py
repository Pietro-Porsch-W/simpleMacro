#base imports to be used when creating the Macros module
#import pyautogui          # To locate pixels in the screen
from pyautogui import *   # A lot of things
import time               # To be able to give delay between actions
import keyboard           # To be able to Use the keyboard actions
import random             # To give random values, may have a more human apearance for certain actions that requiere it
import tkinter as tk 
import win32api #pip install py
import win32con 

# Lista global para armazenar os cliques salvos (x, y, botão, teclas)
cliques_salvos = []

def lclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def rclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def get_pressed_keys():
    keys = []
    if win32api.GetAsyncKeyState(win32con.VK_SHIFT):
        keys.append("Shift")
    if win32api.GetAsyncKeyState(win32con.VK_CONTROL):
        keys.append("Ctrl")
    if win32api.GetAsyncKeyState(win32con.VK_MENU):  # Alt
        keys.append("Alt")
    return keys

def save_coordinates():
    global cliques_salvos
    coordinates_label.config(text="Aguardando próximo clique...")
    print("Aguardando próximo clique...")
    
    while True:
        x, y = win32api.GetCursorPos()
        pressed_keys = get_pressed_keys()
        
        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0:
            cliques_salvos.append((x, y, 'left', pressed_keys))
            coordinates_label.config(text=f"Clique Esquerdo Salvo: ({x}, {y}) com {pressed_keys}")
            print(f"Clique Esquerdo Salvo: ({x}, {y}) com {pressed_keys}")
            break
        
        if win32api.GetAsyncKeyState(win32con.VK_RBUTTON) < 0:
            cliques_salvos.append((x, y, 'right', pressed_keys))
            coordinates_label.config(text=f"Clique Direito Salvo: ({x}, {y}) com {pressed_keys}")
            print(f"Clique Direito Salvo: ({x}, {y}) com {pressed_keys}")
            break

def click_saved_coordinates():
    try:
        delay = int(delay_entry.get()) / 1000  # Converte para segundos
    except ValueError:
        delay = 1  # Se não for número, usa o padrão de 1000ms (1s)
    
    for x, y, button, keys in cliques_salvos:
        # Pressionar teclas antes do clique
        for key in keys:
            if key == "Shift":
                win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
            elif key == "Ctrl":
                win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
            elif key == "Alt":
                win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
        
        # Realizar o clique
        if button == 'left':
            lclick(x, y)
        else:
            rclick(x, y)
        
        # Soltar as teclas após o clique
        for key in keys:
            if key == "Shift":
                win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif key == "Ctrl":
                win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
            elif key == "Alt":
                win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)
        
        time.sleep(delay)

def clear_saved_clicks():
    global cliques_salvos
    cliques_salvos = []
    coordinates_label.config(text="Todos os cliques foram apagados")
    print("Lista de cliques apagada.")

# Criando a interface
top = tk.Tk()
top.title("Macro de Cliques")

delay_label = tk.Label(top, text="Delay entre cliques (ms):")
delay_label.pack()

delay_entry = tk.Entry(top)
delay_entry.insert(0, "1000")  # Delay padrão de 1000ms
delay_entry.pack()

save_button = tk.Button(top, text="Salvar Próximo Clique", command=save_coordinates)
save_button.pack(pady=5)

click_button = tk.Button(top, text="Executar Cliques Salvos", command=click_saved_coordinates)
click_button.pack(pady=5)

clear_button = tk.Button(top, text="Limpar Cliques Salvos", command=clear_saved_clicks)
clear_button.pack(pady=5)

coordinates_label = tk.Label(top, text="Nenhum clique salvo ainda")
coordinates_label.pack()

top.mainloop()
