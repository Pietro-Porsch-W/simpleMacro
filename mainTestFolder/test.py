#base imports to be used when creating the Macros module
#import pyautogui          # To locate pixels in the screen
from pyautogui import *   # A lot of things
import time               # To be able to give delay between actions
import keyboard           # To be able to Use the keyboard actions
import random             # To give random values, may have a more human apearance for certain actions that requiere it
import tkinter as tk 
import win32api #pip install py
import win32con 
 
# Lista global para armazenar os cliques e teclas salvas (x, y, botão, teclas)
cliques_salvos = []
recording = True  # Variável de controle para captura de eventos

def lclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def rclick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def move_mouse_erratic(x, y):
    current_x, current_y = win32api.GetCursorPos()
    while abs(current_x - x) > 2 or abs(current_y - y) > 2:
        current_x += random.randint(-3, 3)
        current_y += random.randint(-3, 3)
        win32api.SetCursorPos((current_x, current_y))
        time.sleep(0.01)
    win32api.SetCursorPos((x, y))

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
    global cliques_salvos, recording
    coordinates_label.config(text="Gravação em andamento... Pressione Left Alt + ESC para parar.")
    print("Gravação em andamento... Pressione Left Alt + ESC para parar.")
    recording = True
    
    while recording:
        x, y = win32api.GetCursorPos()
        pressed_keys = get_pressed_keys()
        
        if win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0:
            cliques_salvos.append((x, y, 'left', pressed_keys))
            print(f"Clique Esquerdo Salvo: ({x}, {y}) com {pressed_keys}")
            time.sleep(0.2)
        
        if win32api.GetAsyncKeyState(win32con.VK_RBUTTON) < 0:
            cliques_salvos.append((x, y, 'right', pressed_keys))
            print(f"Clique Direito Salvo: ({x}, {y}) com {pressed_keys}")
            time.sleep(0.2)
        
        for key in pressed_keys:
            cliques_salvos.append((None, None, 'key', key))
            print(f"Tecla Salva: {key}")
            time.sleep(0.2)

def stop_recording(event):
    global recording
    recording = False
    print("Gravação encerrada.")
    coordinates_label.config(text="Gravação encerrada.")

def click_saved_coordinates():
    try:
        min_delay = int(min_delay_entry.get()) / 1000  # Converte para segundos
        max_delay = int(max_delay_entry.get()) / 1000
    except ValueError:
        min_delay, max_delay = 1, 1  # Padrão de 1000ms
    
    erratic = erratic_var.get()
    
    for x, y, action, keys in cliques_salvos:
        if action == 'key':
            win32api.keybd_event(getattr(win32con, f'VK_{keys.upper()}'), 0, 0, 0)
            time.sleep(random.uniform(min_delay, max_delay))
            win32api.keybd_event(getattr(win32con, f'VK_{keys.upper()}'), 0, win32con.KEYEVENTF_KEYUP, 0)
        elif action in ['left', 'right']:
            if erratic:
                move_mouse_erratic(x, y)
            else:
                win32api.SetCursorPos((x, y))
            if action == 'left':
                lclick(x, y)
            else:
                rclick(x, y)
        time.sleep(random.uniform(min_delay, max_delay))

def clear_saved_clicks():
    global cliques_salvos
    cliques_salvos = []
    coordinates_label.config(text="Todos os cliques foram apagados")
    print("Lista de cliques apagada.")

keyboard.add_hotkey("alt+esc", stop_recording)

# Criando a interface
top = tk.Tk()
top.title("Macro de Cliques")

delay_label = tk.Label(top, text="Delay entre cliques (ms) (mín - máx):")
delay_label.pack()

delay_frame = tk.Frame(top)
delay_frame.pack()

min_delay_entry = tk.Entry(delay_frame, width=6)
min_delay_entry.insert(0, "1000")
min_delay_entry.pack(side=tk.LEFT)

max_delay_entry = tk.Entry(delay_frame, width=6)
max_delay_entry.insert(0, "1000")
max_delay_entry.pack(side=tk.LEFT)

erratic_var = tk.BooleanVar()
erratic_checkbox = tk.Checkbutton(top, text="Movimento Errático", variable=erratic_var)
erratic_checkbox.pack()

save_button = tk.Button(top, text="Iniciar Gravação", command=save_coordinates)
save_button.pack(pady=5)

click_button = tk.Button(top, text="Executar Cliques Salvos", command=click_saved_coordinates)
click_button.pack(pady=5)

clear_button = tk.Button(top, text="Limpar Cliques Salvos", command=clear_saved_clicks)
clear_button.pack(pady=5)

coordinates_label = tk.Label(top, text="Pressione 'Iniciar Gravação' para começar")
coordinates_label.pack()

top.mainloop()
