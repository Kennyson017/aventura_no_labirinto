"""
Módulo de Labirinto
==================

Funções para criar e imprimir labirintos com itens coletáveis.
"""

import random
from rich.text import Text
from rich.console import Console

def criar_labirinto(linhas=21, colunas=41, dificuldade=1):
    """
    Cria um labirinto usando algoritmo DFS.
    
    Args:
        linhas (int): Número de linhas do labirinto
        colunas (int): Número de colunas do labirinto
        dificuldade (int): 1=Fácil, 2=Médio, 3=Difícil
    
    Returns:
        tuple: (labirinto, itens, entrada, saida)
    """
    # Ajusta dimensões por dificuldade
    if dificuldade == 1:  # Fácil
        linhas, colunas = 15, 31
        num_itens = 3
    elif dificuldade == 2:  # Médio  
        linhas, colunas = 21, 41
        num_itens = 5
    else:  # Difícil
        linhas, colunas = 25, 51
        num_itens = 8
    
    # Garante dimensões ímpares para DFS
    if linhas % 2 == 0:
        linhas += 1
    if colunas % 2 == 0:
        colunas += 1
    
    # Inicializa labirinto como paredes
    lab = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
    def vizinhos(x, y):
        """Retorna vizinhos válidos para DFS"""
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 < nx < linhas - 1 and 0 < ny < colunas - 1:
                yield nx, ny, dx, dy
    
    def dfs(x, y):
        """Algoritmo DFS para gerar labirinto"""
        lab[x][y] = " "
        viz = list(vizinhos(x, y))
        random.shuffle(viz)
        for nx, ny, dx, dy in viz:
            if lab[nx][ny] == "#":
                # Remove parede entre células
                lab[x + dx // 2][y + dy // 2] = " "
                dfs(nx, ny)
    
    # Gera labirinto começando de posição ímpar
    dfs(1, 1)
    
    # Define entrada e saída
    entrada = (0, 1)
    saida = (linhas - 1, colunas - 2)
    lab[entrada[0]][entrada[1]] = " "
    lab[saida[0]][saida[1]] = " "
    
    # Conecta entrada
    if entrada[0] + 1 < linhas:
        lab[entrada[0] + 1][entrada[1]] = " "
    
    # Conecta saída
    if saida[0] - 1 >= 0:
        lab[saida[0] - 1][saida[1]] = " "
    
    # Adiciona itens coletáveis em posições aleatórias
    itens = {}
    espacos_livres = []
    
    # Encontra espaços livres (exceto entrada e saída)
    for i in range(linhas):
        for j in range(colunas):
            if lab[i][j] == " " and (i, j) not in [entrada, saida]:
                # Evita colocar items muito perto da entrada
                if abs(i - entrada[0]) + abs(j - entrada[1]) > 3:
                    espacos_livres.append((i, j))
    
    # Coloca itens aleatoriamente
    for _ in range(min(num_itens, len(espacos_livres))):
        pos = random.choice(espacos_livres)
        espacos_livres.remove(pos)
        itens[pos] = {
            "tipo": "$",  # Usa apenas $ para evitar problemas com emojis
            "valor": random.randint(10, 50)
        }
    
    return lab, itens, entrada, saida

def imprimir_labirinto(console, lab, jogador_pos, itens, itens_coletados, cor_tema="green"):
    """
    Imprime o labirinto com jogador e itens usando caracteres ASCII simples.
    
    Args:
        console: Console do Rich
        lab: Matriz do labirinto
        jogador_pos: Posição atual do jogador (x, y)
        itens: Dicionário de itens no labirinto
        itens_coletados: Set de posições de itens coletados
        cor_tema: Cor tema das paredes
    """
    texto_completo = Text()
    
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            pos = (i, j)
            
            if pos == jogador_pos:
                # Jogador - usa @ simples
                texto_completo.append("@", style="bold blue")
                
            elif pos in itens and pos not in itens_coletados:
                # Item não coletado - usa $ simples
                texto_completo.append("$", style="bold yellow")
                
            elif pos == (len(lab) - 1, len(lab[0]) - 2):
                # Saída - usa X simples
                texto_completo.append("X", style="bold red")
                
            elif lab[i][j] == "#":
                # Paredes - usa caractere block
                texto_completo.append("█", style=f"bold {cor_tema}")
                
            else:
                # Caminhos
                if pos in itens_coletados:
                    # Local onde havia item coletado
                    texto_completo.append(".", style="dim yellow")
                else:
                    # Caminho vazio
                    texto_completo.append(" ", style="white")
        
        # Adiciona quebra de linha (exceto na última linha)
        if i < len(lab) - 1:
            texto_completo.append("\n")
    
    return texto_completo

def verificar_item_coletado(jogador_pos, itens, itens_coletados):
    """
    Verifica se jogador coletou algum item na posição atual.
    
    Args:
        jogador_pos: Posição do jogador (x, y)
        itens: Dicionário de itens
        itens_coletados: Set de posições coletadas
    
    Returns:
        dict ou None: Item coletado ou None
    """
    # Só retorna item se não foi coletado ainda
    if jogador_pos in itens and jogador_pos not in itens_coletados:
        return itens[jogador_pos]
    return None