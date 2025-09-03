from rich.console import Console
from rich.text import Text
from rich.live import Live
import random
import time
import keyboard

# Gera labirinto com DFS (algoritmo clássico)
def gerar_labirinto(linhas, colunas):
    lab = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
    def vizinhos(x, y):
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 < nx < linhas and 0 < ny < colunas:
                yield nx, ny, dx, dy
    
    def dfs(x, y):
        lab[x][y] = " "
        viz = list(vizinhos(x, y))
        random.shuffle(viz)
        for nx, ny, dx, dy in viz:
            if lab[nx][ny] == "#":
                # Remove parede entre células
                lab[x + dx // 2][y + dy // 2] = " "
                dfs(nx, ny)
    
    dfs(1, 1)
    
    # Entrada e saída
    lab[0][1] = " "   # entrada
    lab[linhas - 1][colunas - 2] = " "  # saída
    
    return lab

# Movimento célula por célula
def mover(lab, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if 0 <= nx < len(lab) and 0 <= ny < len(lab[0]) and lab[nx][ny] == " ":
        return nx, ny
    return x, y

def main():
    console = Console()
    
    # Configurações do labirinto
    linhas, colunas = 21, 41  
    lab = gerar_labirinto(linhas, colunas)
    
    # Posição inicial
    x, y = 0, 1
    destino = (linhas - 1, colunas - 2)
    
    def renderizar():
        texto_completo = Text()
        
        for i in range(linhas):
            for j in range(colunas):
                if i == x and j == y:
                    # Player azul
                    texto_completo.append("@", style="bold blue")
                elif (i, j) == destino:
                    # Saída em vermelho
                    texto_completo.append("◉", style="bold red")
                elif lab[i][j] == "#":
                    # Paredes verdes
                    texto_completo.append("█", style="bold green")
                else:
                    # Caminhos em branco
                    texto_completo.append("·", style="white")
            
            if i < linhas - 1:
                texto_completo.append("\n")
        
        return texto_completo
    
    console.clear()
    console.print("🎮 LABIRINTO CLÁSSICO", style="bold cyan")
    console.print("Use WASD ou setas para navegar")
    console.print("@ = Você | █ = Paredes | · = Caminhos | ◉ = Saída")
    console.print("Chegue na saída vermelha! | ESC = Sair\n")
    
    with Live(renderizar(), console=console, refresh_per_second=20) as live:
        last_move_time = 0
        
        while True:
            current_time = time.time()
            
            # Verifica se chegou na saída
            if (x, y) == destino:
                live.stop()
                console.clear()
                console.print("🏆 VOCÊ VENCEU! 🏆", style="bold green", justify="center")
                console.print("Parabéns! Você encontrou a saída do labirinto!", style="bold white", justify="center")
                break
            
            # Controles de movimento fluidos
            moved = False
            try:
                if current_time - last_move_time > 0.08:
                    if keyboard.is_pressed('up') or keyboard.is_pressed('w'):
                        new_x, new_y = mover(lab, x, y, -1, 0)
                        if (new_x, new_y) != (x, y):
                            x, y = new_x, new_y
                            moved = True
                    elif keyboard.is_pressed('down') or keyboard.is_pressed('s'):
                        new_x, new_y = mover(lab, x, y, 1, 0)
                        if (new_x, new_y) != (x, y):
                            x, y = new_x, new_y
                            moved = True
                    elif keyboard.is_pressed('left') or keyboard.is_pressed('a'):
                        new_x, new_y = mover(lab, x, y, 0, -1)
                        if (new_x, new_y) != (x, y):
                            x, y = new_x, new_y
                            moved = True
                    elif keyboard.is_pressed('right') or keyboard.is_pressed('d'):
                        new_x, new_y = mover(lab, x, y, 0, 1)
                        if (new_x, new_y) != (x, y):
                            x, y = new_x, new_y
                            moved = True
                    
                    if moved:
                        last_move_time = current_time
                        
                if keyboard.is_pressed('esc'):
                    break
                    
            except:
                pass
            
            live.update(renderizar())
            time.sleep(0.03)

if __name__ == "__main__":
    print("📋 Dependências: pip install rich keyboard")
    print("Pressione Enter para iniciar o Labirinto...")
    input()
    main()