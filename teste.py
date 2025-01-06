import mouse
import keyboard
a = 0
while True:
    if keyboard.is_pressed('q'):
        print("Tecla 'q' foi pressionada. Programa encerrado.")
        break

    if mouse.is_pressed(button='left'):  
        a += 1    
        print("\nClique com o botão esquerdo detectado! ", a)
