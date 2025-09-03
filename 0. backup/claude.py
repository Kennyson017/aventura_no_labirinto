# from rich.console import Console
# from rich.text import Text
# from rich.live import Live
# import random
# import time
# import keyboard

# # Gera labirinto com DFS e corredores verticais mais largos
# def gerar_labirinto(linhas, colunas):
#     lab = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
#     def vizinhos(x, y):
#         for dx, dy in [(-2, 0), (2, 0), (0, -3), (0, 3)]:  # Verticais mais largos (3 ao invés de 2)
#             nx, ny = x + dx, y + dy
#             if 0 < nx < linhas and 0 < ny < colunas:
#                 yield nx, ny, dx, dy
    
#     def dfs(x, y):
#         lab[x][y] = " "
#         viz = list(vizinhos(x, y))
#         random.shuffle(viz)
#         for nx, ny, dx, dy in viz:
#             if lab[nx][ny] == "#":
#                 # Remove parede intermediária
#                 if dx != 0:  # Movimento horizontal
#                     lab[x + dx // 2][y] = " "
#                 else:  # Movimento vertical - remove mais células para corredor largo
#                     for i in range(1, abs(dy)):
#                         lab[x][y + (dy // abs(dy)) * i] = " "
#                 dfs(nx, ny)
    
#     dfs(1, 1)
    
#     # Entrada e saída com corredores mais largos
#     lab[0][1] = " "
#     lab[0][2] = " "  # Entrada mais larga
#     lab[linhas - 1][colunas - 2] = " "
#     lab[linhas - 1][colunas - 3] = " "  # Saída mais larga
    
#     return lab

# # Movimento contínuo até a parede
# def mover(lab, x, y, dx, dy):
#     while True:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx >= len(lab) or ny < 0 or ny >= len(lab[0]) or lab[nx][ny] == "#":
#             break
#         x, y = nx, ny
#     return x, y

# def main():
#     console = Console()
    
#     # Configurações do labirinto
#     linhas, colunas = 21, 61  # Mais colunas para acomodar corredores largos
#     lab = gerar_labirinto(linhas, colunas)
    
#     # Posição inicial
#     x, y = 0, 1
#     destino = (linhas - 1, colunas - 2)
    
#     def renderizar():
#         texto_completo = Text()
        
#         for i in range(linhas):
#             linha = ""
#             for j in range(colunas):
#                 if i == x and j == y:
#                     # Adiciona o texto da linha atual
#                     texto_completo.append(linha)
#                     # Adiciona o @ azul
#                     texto_completo.append("@", style="bold blue")
#                     linha = ""
#                 else:
#                     linha += lab[i][j]
            
#             # Adiciona o resto da linha e quebra
#             texto_completo.append(linha)
#             if i < linhas - 1:
#                 texto_completo.append("\n")
        
#         return texto_completo
    
#     console.clear()
#     console.print("Use as setas para mover. O @ se move até encontrar uma parede!")
#     console.print("Chegue até a saída no canto inferior direito.\n")
    
#     with Live(renderizar(), console=console, refresh_per_second=10) as live:
#         while True:
#             # Verifica se chegou na saída
#             if (x, y) == destino:
#                 live.stop()
#                 console.clear()
#                 vitoria = Text("VOCÊ VENCEU!", style="bold green")
#                 console.print(vitoria, justify="center")
#                 break
            
#             # Lê tecla pressionada
#             try:
#                 if keyboard.is_pressed('up'):
#                     x, y = mover(lab, x, y, -1, 0)
#                     time.sleep(0.1)  # Evita movimento muito rápido
#                 elif keyboard.is_pressed('down'):
#                     x, y = mover(lab, x, y, 1, 0)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('left'):
#                     x, y = mover(lab, x, y, 0, -1)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('right'):
#                     x, y = mover(lab, x, y, 0, 1)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('esc'):
#                     break
#             except:
#                 pass
            
#             # Atualiza a renderização
#             live.update(renderizar())
#             time.sleep(0.05)

# if __name__ == "__main__":
#     print("Instalando dependências necessárias...")
#     print("\nPressione Enter para continuar...")
#     input()
#     main()

# from rich.console import Console
# from rich.text import Text
# from rich.live import Live
# import random
# import time
# import keyboard

# # Gera labirinto com DFS e corredores verticais mais largos
# def gerar_labirinto(linhas, colunas):
#     lab = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
#     def vizinhos(x, y):
#         for dx, dy in [(-2, 0), (2, 0), (0, -3), (0, 3)]:  # Verticais mais largos (3 ao invés de 2)
#             nx, ny = x + dx, y + dy
#             if 0 < nx < linhas and 0 < ny < colunas:
#                 yield nx, ny, dx, dy
    
#     def dfs(x, y):
#         lab[x][y] = " "
#         viz = list(vizinhos(x, y))
#         random.shuffle(viz)
#         for nx, ny, dx, dy in viz:
#             if lab[nx][ny] == "#":
#                 # Remove parede intermediária
#                 if dx != 0:  # Movimento horizontal
#                     lab[x + dx // 2][y] = " "
#                 else:  # Movimento vertical - remove mais células para corredor largo
#                     for i in range(1, abs(dy)):
#                         lab[x][y + (dy // abs(dy)) * i] = " "
#                 dfs(nx, ny)
    
#     dfs(1, 1)
    
#     # Entrada e saída com corredores mais largos
#     lab[0][1] = " "
#     lab[0][2] = " "  # Entrada mais larga
#     lab[linhas - 1][colunas - 2] = " "
#     lab[linhas - 1][colunas - 3] = " "  # Saída mais larga
    
#     return lab

# # Movimento contínuo até a parede
# def mover(lab, x, y, dx, dy):
#     while True:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx >= len(lab) or ny < 0 or ny >= len(lab[0]) or lab[nx][ny] == "#":
#             break
#         x, y = nx, ny
#     return x, y

# def main():
#     console = Console()
    
#     # Configurações do labirinto
#     linhas, colunas = 21, 61  # Mais colunas para acomodar corredores largos
#     lab = gerar_labirinto(linhas, colunas)
    
#     # Posição inicial
#     x, y = 0, 1
#     destino = (linhas - 1, colunas - 2)
    
#     def renderizar():
#         texto_completo = Text()
        
#         for i in range(linhas):
#             for j in range(colunas):
#                 if i == x and j == y:
#                     # Adiciona o @ azul
#                     texto_completo.append("@", style="bold blue")
#                 elif lab[i][j] == "#":
#                     # Paredes verdes
#                     texto_completo.append("#", style="bold green")
#                 else:
#                     # Espaços vazios (corredores)
#                     texto_completo.append(" ")
            
#             # Quebra de linha
#             if i < linhas - 1:
#                 texto_completo.append("\n")
        
#         return texto_completo
    
#     console.clear()
#     console.print("Use as setas para mover. O @ se move até encontrar uma parede!")
#     console.print("Chegue até a saída no canto inferior direito.\n")
    
#     with Live(renderizar(), console=console, refresh_per_second=10) as live:
#         while True:
#             # Verifica se chegou na saída
#             if (x, y) == destino:
#                 live.stop()
#                 console.clear()
#                 vitoria = Text("VOCÊ VENCEU!", style="bold green")
#                 console.print(vitoria, justify="center")
#                 break
            
#             # Lê tecla pressionada
#             try:
#                 if keyboard.is_pressed('up'):
#                     x, y = mover(lab, x, y, -1, 0)
#                     time.sleep(0.1)  # Evita movimento muito rápido
#                 elif keyboard.is_pressed('down'):
#                     x, y = mover(lab, x, y, 1, 0)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('left'):
#                     x, y = mover(lab, x, y, 0, -1)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('right'):
#                     x, y = mover(lab, x, y, 0, 1)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('esc'):
#                     break
#             except:
#                 pass
            
#             # Atualiza a renderização
#             live.update(renderizar())
#             time.sleep(0.05)

# if __name__ == "__main__":
#     print("Instalando dependências necessárias...")
#     print("Execute: pip install rich keyboard")
#     print("\nPressione Enter para continuar...")
#     input()
#     main()

# from rich.console import Console
# from rich.text import Text
# from rich.live import Live
# import random
# import time
# import keyboard

# # Gera labirinto com DFS e corredores verticais mais largos
# def gerar_labirinto(linhas, colunas):
#     lab = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
#     def vizinhos(x, y):
#         for dx, dy in [(-2, 0), (2, 0), (0, -3), (0, 3)]:  # Verticais mais largos (3 ao invés de 2)
#             nx, ny = x + dx, y + dy
#             if 0 < nx < linhas and 0 < ny < colunas:
#                 yield nx, ny, dx, dy
    
#     def dfs(x, y):
#         lab[x][y] = " "
#         viz = list(vizinhos(x, y))
#         random.shuffle(viz)
#         for nx, ny, dx, dy in viz:
#             if lab[nx][ny] == "#":
#                 # Remove parede intermediária
#                 if dx != 0:  # Movimento horizontal
#                     lab[x + dx // 2][y] = " "
#                 else:  # Movimento vertical - remove mais células para corredor largo
#                     for i in range(1, abs(dy)):
#                         lab[x][y + (dy // abs(dy)) * i] = " "
#                 dfs(nx, ny)
    
#     dfs(1, 1)
    
#     # Entrada e saída com corredores mais largos
#     lab[0][1] = " "
#     lab[0][2] = " "  # Entrada mais larga
#     lab[linhas - 1][colunas - 2] = " "
#     lab[linhas - 1][colunas - 3] = " "  # Saída mais larga
    
#     return lab

# # Movimento contínuo até a parede
# def mover(lab, x, y, dx, dy):
#     while True:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx >= len(lab) or ny < 0 or ny >= len(lab[0]) or lab[nx][ny] == "#":
#             break
#         x, y = nx, ny
#     return x, y

# def main():
#     console = Console()
    
#     # Configurações do labirinto
#     linhas, colunas = 21, 61  # Mais colunas para acomodar corredores largos
#     lab = gerar_labirinto(linhas, colunas)
    
#     # Posição inicial
#     x, y = 0, 1
#     destino = (linhas - 1, colunas - 2)
    
#     def renderizar():
#         texto_completo = Text()
        
#         for i in range(linhas):
#             for j in range(colunas):
#                 if i == x and j == y:
#                     # Adiciona o @ azul
#                     texto_completo.append("@", style="bold blue")
#                 elif lab[i][j] == "#":
#                     # Paredes verdes
#                     texto_completo.append("#", style="bold green")
#                 else:
#                     # Espaços vazios (corredores)
#                     texto_completo.append(" ")
            
#             # Quebra de linha
#             if i < linhas - 1:
#                 texto_completo.append("\n")
        
#         return texto_completo
    
#     console.clear()
#     console.print("Use as setas para mover. O @ se move até encontrar uma parede!")
#     console.print("Chegue até a saída no canto inferior direito.\n")
    
#     with Live(renderizar(), console=console, refresh_per_second=10) as live:
#         while True:
#             # Verifica se chegou na saída
#             if (x, y) == destino:
#                 live.stop()
#                 console.clear()
#                 vitoria = Text("VOCÊ VENCEU!", style="bold green")
#                 console.print(vitoria, justify="center")
#                 break
            
#             # Lê tecla pressionada
#             try:
#                 if keyboard.is_pressed('up'):
#                     x, y = mover(lab, x, y, -1, 0)
#                     time.sleep(0.1)  # Evita movimento muito rápido
#                 elif keyboard.is_pressed('down'):
#                     x, y = mover(lab, x, y, 1, 0)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('left'):
#                     x, y = mover(lab, x, y, 0, -1)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('right'):
#                     x, y = mover(lab, x, y, 0, 1)
#                     time.sleep(0.1)
#                 elif keyboard.is_pressed('esc'):
#                     break
#             except:
#                 pass
            
#             # Atualiza a renderização
#             live.update(renderizar())
#             time.sleep(0.05)

# if __name__ == "__main__":
#     print("Instalando dependências necessárias...")
#     print("Execute: pip install rich keyboard")
#     print("\nPressione Enter para continuar...")
#     input()
#     main()

########################################################################################################

from rich.console import Console
from rich.text import Text
from rich.live import Live
import random
import time
import keyboard

# Gera labirinto com DFS e corredores verticais mais largos
def gerar_labirinto(linhas, colunas):
    lab = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
    def vizinhos(x, y):
        for dx, dy in [(-2, 0), (2, 0), (0, -3), (0, 3)]:  # Verticais mais largos (3 ao invés de 2)
            nx, ny = x + dx, y + dy
            if 0 < nx < linhas and 0 < ny < colunas:
                yield nx, ny, dx, dy
    
    def dfs(x, y):
        lab[x][y] = " "
        viz = list(vizinhos(x, y))
        random.shuffle(viz)
        for nx, ny, dx, dy in viz:
            if lab[nx][ny] == "#":
                # Remove parede intermediária
                if dx != 0:  # Movimento horizontal
                    lab[x + dx // 2][y] = " "
                else:  # Movimento vertical - remove mais células para corredor largo
                    for i in range(1, abs(dy)):
                        lab[x][y + (dy // abs(dy)) * i] = " "
                dfs(nx, ny)
    
    dfs(1, 1)
    
    # Entrada e saída com corredores mais largos
    lab[0][1] = " "
    lab[0][2] = " "  # Entrada mais larga
    lab[linhas - 1][colunas - 2] = " "
    lab[linhas - 1][colunas - 3] = " "  # Saída mais larga
    
    return lab

# Movimento contínuo até a parede
def mover(lab, x, y, dx, dy):
    while True:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(lab) or ny < 0 or ny >= len(lab[0]) or lab[nx][ny] == "#":
            break
        x, y = nx, ny
    return x, y

def main():
    console = Console()
    
    # Configurações do labirinto
    linhas, colunas = 21, 61  # Mais colunas para acomodar corredores largos
    lab = gerar_labirinto(linhas, colunas)
    
    # Posição inicial
    x, y = 0, 1
    destino = (linhas - 1, colunas - 2)
    
    def renderizar():
        texto_completo = Text()
        
        for i in range(linhas):
            for j in range(colunas):
                if i == x and j == y:
                    # Adiciona o @ azul
                    texto_completo.append("@", style="bold blue")
                elif lab[i][j] == "#":
                    # Paredes verdes
                    texto_completo.append("#", style="bold green")
                else:
                    # Espaços vazios (corredores)
                    texto_completo.append(" ")
            
            # Quebra de linha
            if i < linhas - 1:
                texto_completo.append("\n")
        
        return texto_completo
    
    console.clear()
    console.print("Use as setas para mover. O @ se move até encontrar uma parede!")
    console.print("Chegue até a saída no canto inferior direito.\n")
    
    with Live(renderizar(), console=console, refresh_per_second=10) as live:
        while True:
            # Verifica se chegou na saída
            if (x, y) == destino:
                live.stop()
                console.clear()
                vitoria = Text("VOCÊ VENCEU!", style="bold green")
                console.print(vitoria, justify="center")
                break
            
            # Lê tecla pressionada
            try:
                if keyboard.is_pressed('up'):
                    x, y = mover(lab, x, y, -1, 0)
                    time.sleep(0.1)  # Evita movimento muito rápido
                elif keyboard.is_pressed('down'):
                    x, y = mover(lab, x, y, 1, 0)
                    time.sleep(0.1)
                elif keyboard.is_pressed('left'):
                    x, y = mover(lab, x, y, 0, -1)
                    time.sleep(0.1)
                elif keyboard.is_pressed('right'):
                    x, y = mover(lab, x, y, 0, 1)
                    time.sleep(0.1)
                elif keyboard.is_pressed('esc'):
                    break
            except:
                pass
            
            # Atualiza a renderização
            live.update(renderizar())
            time.sleep(0.05)

if __name__ == "__main__":
    print("Instalando dependências necessárias...")
    print("Execute: pip install rich keyboard")
    print("\nPressione Enter para continuar...")
    input()
    main()