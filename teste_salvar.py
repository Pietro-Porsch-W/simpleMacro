import keyboard
import ctypes
from ctypes import wintypes
import time
import threading

# Caminho do arquivo de saída
saida_path = r"C:\Users\pietr\OneDrive\Documentos\GitHub\simpleMacro\saida.txt"

# Variável de controle do loop
rodando = True

# Estruturas e funções da API do Windows para o mouse
class POINT(ctypes.Structure):
    _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]

user32 = ctypes.WinDLL('user32', use_last_error=True)

def get_mouse_position():
    point = POINT()
    user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

def monitorar_mouse():
    global rodando
    ultimo_estado = {"botao_esquerdo": False, "botao_direito": False, "botao_meio": False}
    ultima_posicao = get_mouse_position()

    while rodando:
        # Captura posição atual do mouse
        posicao_atual = get_mouse_position()

        # Detecta movimento
        if posicao_atual != ultima_posicao:
            texto = f"Mouse movido para: {posicao_atual}"
            with open(saida_path, "a") as file:
                file.write(texto + "\n")
            print(texto)
            ultima_posicao = posicao_atual

        # Verifica clique esquerdo
        botao_esquerdo = user32.GetAsyncKeyState(0x01) & 0x8000 != 0
        if botao_esquerdo != ultimo_estado["botao_esquerdo"]:
            tipo = "Pressionado" if botao_esquerdo else "Liberado"
            texto = f"Mouse {tipo} - Botão esquerdo - Posição: {posicao_atual}"
            with open(saida_path, "a") as file:
                file.write(texto + "\n")
            print(texto)
            ultimo_estado["botao_esquerdo"] = botao_esquerdo

        # Verifica clique direito
        botao_direito = user32.GetAsyncKeyState(0x02) & 0x8000 != 0
        if botao_direito != ultimo_estado["botao_direito"]:
            tipo = "Pressionado" if botao_direito else "Liberado"
            texto = f"Mouse {tipo} - Botão direito - Posição: {posicao_atual}"
            with open(saida_path, "a") as file:
                file.write(texto + "\n")
            print(texto)
            ultimo_estado["botao_direito"] = botao_direito

        # Verifica clique do botão do meio
        botao_meio = user32.GetAsyncKeyState(0x04) & 0x8000 != 0
        if botao_meio != ultimo_estado["botao_meio"]:
            tipo = "Pressionado" if botao_meio else "Liberado"
            texto = f"Mouse {tipo} - Botão do meio - Posição: {posicao_atual}"
            with open(saida_path, "a") as file:
                file.write(texto + "\n")
            print(texto)
            ultimo_estado["botao_meio"] = botao_meio

        time.sleep(0.01)  # Pequeno intervalo para não sobrecarregar

def monitorar_teclado():
    global rodando
    teclas_pressionadas = {}

    while rodando:
        evento = keyboard.read_event()
        if evento.event_type == 'down':
            tecla = evento.name
            if tecla not in teclas_pressionadas:
                teclas_pressionadas[tecla] = time.time()
                texto = f"Tecla {tecla} pressionada"
                with open(saida_path, "a") as file:
                    file.write(texto + "\n")
                print(texto)

        elif evento.event_type == 'up':
            tecla = evento.name
            if tecla in teclas_pressionadas:
                duracao = time.time() - teclas_pressionadas.pop(tecla, 0)
                texto = f"Tecla {tecla} liberada após {duracao:.2f} segundos"
                with open(saida_path, "a") as file:
                    file.write(texto + "\n")
                print(texto)

            # Finaliza o loop se F12 for pressionado
            if tecla == 'f12':
                rodando = False
                return

        time.sleep(0.01)

def main():
    global rodando
    open(saida_path, "w").close()  # Limpa o arquivo de saída no início

    # Criação de threads para mouse e teclado
    mouse_thread = threading.Thread(target=monitorar_mouse)
    teclado_thread = threading.Thread(target=monitorar_teclado)

    mouse_thread.start()
    teclado_thread.start()

    while rodando:
        time.sleep(0.1)

    mouse_thread.join()
    teclado_thread.join()

if __name__ == "__main__":
    main()
