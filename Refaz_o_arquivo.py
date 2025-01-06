import time
import pyautogui
import keyboard

# Caminho do arquivo de entrada
saida_path = r"C:\Users\pietr\OneDrive\Documentos\GitHub\simpleMacro\saida.txt"



# Variável de controle para movimentos do mouse
executar_movimentos_mouse = True  # True para executar movimentos, False para ignorar




# Tempo para suavizar a movimentação (em segundos)
duracao_movimento = 0.2  # Ajuste este valor para controlar a fluidez

def executar_acao(acao):
    """Executa uma ação com base na string da ação."""
    try:
        if acao.startswith("Mouse movido para:"):
            # Extrai a posição
            _, posicao = acao.split(": ")
            x, y = eval(posicao)  # Transforma em tupla
            
            if executar_movimentos_mouse:
                pyautogui.moveTo(x, y, duration=duracao_movimento)  # Movimenta o mouse suavemente

        elif "Mouse Pressionado" in acao:
            # Extrai o botão e a posição
            botao = "left" if "Botão esquerdo" in acao else "right" if "Botão direito" in acao else "middle"
            posicao = acao.split("Posição: ")[1]
            x, y = eval(posicao)
            pyautogui.mouseDown(x, y, button=botao)

        elif "Mouse Liberado" in acao:
            # Extrai o botão e a posição
            botao = "left" if "Botão esquerdo" in acao else "right" if "Botão direito" in acao else "middle"
            posicao = acao.split("Posição: ")[1]
            x, y = eval(posicao)
            pyautogui.mouseUp(x, y, button=botao)

        elif acao.startswith("Tecla"):
            # Identifica a tecla pressionada ou liberada
            if "pressionada" in acao:
                _, tecla = acao.split("Tecla ")
                tecla = tecla.replace(" pressionada", "").strip()
                keyboard.press(tecla)
            elif "liberada após" in acao:
                _, resto = acao.split("Tecla ")
                tecla, _ = resto.split(" liberada após ")
                tecla = tecla.strip()
                keyboard.release(tecla)
    except Exception as e:
        print(f"Erro ao executar ação: {acao} - {e}")

def reproduzir_acoes():
    """Lê o arquivo e reproduz as ações."""
    try:
        with open(saida_path, "r") as file:
            linhas = file.readlines()

        for i, linha in enumerate(linhas):
            linha = linha.strip()
            if not linha:
                continue

            # Adiciona pausa entre ações se necessário
            if i > 0:
                tempo_anterior = float(linhas[i - 1].split()[-2]) if "segundos" in linhas[i - 1] else None
                tempo_atual = float(linha.split()[-2]) if "segundos" in linha else None
                if tempo_anterior is not None and tempo_atual is not None:
                    pausa = tempo_atual - tempo_anterior
                    if pausa > 0:
                        time.sleep(pausa)

            print(f"Executando: {linha}")
            executar_acao(linha)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {saida_path}")
    except Exception as e:
        print(f"Erro ao reproduzir ações: {e}")

if __name__ == "__main__":
    reproduzir_acoes()
