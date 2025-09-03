"""
Módulo do Jogador
================

Controla movimentação, pontuação e estado do jogador.
"""

import time
import keyboard
from rich.console import Console
from rich.panel import Panel

class EstadoJogador:
    """Classe para gerenciar estado do jogador"""
    def __init__(self, nome, posicao_inicial):
        self.nome = nome
        self.posicao = posicao_inicial
        self.pontuacao = 0
        self.movimentos = 0
        self.itens_coletados = []
        self.tempo_inicio = time.time()
        self.vivo = True

def iniciar_jogador(nome, entrada):
    """
    Inicializa o jogador na posição inicial.
    
    Args:
        nome (str): Nome do jogador
        entrada (tuple): Posição inicial (x, y)
    
    Returns:
        EstadoJogador: Estado inicial do jogador
    """
    jogador = EstadoJogador(nome, entrada)
    return jogador

def mover(jogador, labirinto, direcao=None):
    """
    Move o jogador baseado na entrada do teclado ou direção especificada.
    
    Args:
        jogador: Estado do jogador
        labirinto: Matriz do labirinto
        direcao: Direção específica (para IA) ou None (para teclado)
    
    Returns:
        tuple: (nova_posicao, moveu)
    """
    x, y = jogador.posicao
    nova_posicao = (x, y)
    moveu = False
    
    # Mapeamento de direções
    movimentos = {
        'up': (-1, 0),
        'down': (1, 0), 
        'left': (0, -1),
        'right': (0, 1),
        'w': (-1, 0),
        's': (1, 0),
        'a': (0, -1),
        'd': (0, 1)
    }
    
    if direcao:
        # Movimento automático (para IA)
        if direcao in movimentos:
            dx, dy = movimentos[direcao]
            nova_x, nova_y = x + dx, y + dy
            
            if (0 <= nova_x < len(labirinto) and 
                0 <= nova_y < len(labirinto[0]) and 
                labirinto[nova_x][nova_y] == " "):
                nova_posicao = (nova_x, nova_y)
                moveu = True
    else:
        # Movimento manual
        try:
            for tecla, (dx, dy) in movimentos.items():
                if keyboard.is_pressed(tecla):
                    nova_x, nova_y = x + dx, y + dy
                    
                    if (0 <= nova_x < len(labirinto) and 
                        0 <= nova_y < len(labirinto[0]) and 
                        labirinto[nova_x][nova_y] == " "):
                        nova_posicao = (nova_x, nova_y)
                        moveu = True
                        break
        except:
            pass
    
    if moveu:
        jogador.posicao = nova_posicao
        jogador.movimentos += 1
    
    return nova_posicao, moveu

def pontuar(jogador, item_coletado=None, bonus_tempo=False, penalidade=0):
    """
    Atualiza pontuação do jogador baseado em diferentes eventos.
    
    Args:
        jogador: Estado do jogador
        item_coletado: Item coletado (dict com 'valor')
        bonus_tempo: Se deve dar bônus por tempo
        penalidade: Penalidade a aplicar
    """
    if item_coletado:
        # Pontos por item coletado
        pontos = item_coletado["valor"]
        jogador.pontuacao += pontos
        # Adiciona item à lista (armazena apenas o tipo e valor)
        jogador.itens_coletados.append({
            "tipo": item_coletado["tipo"],
            "valor": item_coletado["valor"]
        })
        return f"+{pontos} pontos por {item_coletado['tipo']}!"
    
    if bonus_tempo:
        # Bônus por completar rapidamente
        tempo_total = time.time() - jogador.tempo_inicio
        bonus = max(100 - int(tempo_total), 10)  # Mínimo 10 pontos
        jogador.pontuacao += bonus
        return f"+{bonus} pontos de bônus de tempo!"
    
    if penalidade > 0:
        # Penalidade por movimentos excessivos
        jogador.pontuacao = max(0, jogador.pontuacao - penalidade)
        return f"-{penalidade} pontos de penalidade"
    
    return ""

def exibir_status_jogador(console, jogador):
    """
    Exibe o status atual do jogador.
    
    Args:
        console: Console do Rich
        jogador: Estado do jogador
    """
    tempo_atual = time.time() - jogador.tempo_inicio
    status = f"""
🎮 Jogador: [bold blue]{jogador.nome}[/bold blue]
🏆 Pontuação: [bold yellow]{jogador.pontuacao}[/bold yellow]
👣 Movimentos: [bold white]{jogador.movimentos}[/bold white]
⏱️  Tempo: [bold green]{tempo_atual:.1f}s[/bold green]
💎 Itens: [bold cyan]{len(jogador.itens_coletados)}[/bold cyan]
    """
    
    painel = Panel(
        status.strip(),
        title="📊 Status",
        border_style="blue",
        width=25
    )
    
    return painel

def resolver_labirinto(labirinto, inicio, fim, caminho_atual=[]):
    """
    Função recursiva que encontra o caminho para resolver o labirinto.
    
    Args:
        labirinto: Matriz do labirinto
        inicio: Posição inicial (x, y)
        fim: Posição final (x, y) 
        caminho_atual: Caminho percorrido até agora
    
    Returns:
        list: Lista de movimentos para resolver ou None se impossível
    """
    x, y = inicio
    
    # Chegou ao destino
    if inicio == fim:
        return caminho_atual
    
    # Marca posição atual como visitada temporariamente
    labirinto_temp = [linha[:] for linha in labirinto]  # Cópia
    labirinto_temp[x][y] = "#"
    
    # Tenta cada direção
    direcoes = [
        ((-1, 0), 'up'),    # Cima
        ((1, 0), 'down'),   # Baixo  
        ((0, -1), 'left'),  # Esquerda
        ((0, 1), 'right')   # Direita
    ]
    
    for (dx, dy), movimento in direcoes:
        nova_x, nova_y = x + dx, y + dy
        
        # Verifica se a posição é válida e livre
        if (0 <= nova_x < len(labirinto) and 
            0 <= nova_y < len(labirinto[0]) and 
            labirinto_temp[nova_x][nova_y] == " "):
            
            # Chamada recursiva
            resultado = resolver_labirinto(
                labirinto_temp, 
                (nova_x, nova_y), 
                fim, 
                caminho_atual + [movimento]
            )
            
            if resultado is not None:
                return resultado
    
    return None  # Sem solução encontrada