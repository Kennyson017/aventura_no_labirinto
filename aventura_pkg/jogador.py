"""
Módulo do Jogador
================

Controla movimentação, pontuação e estado do jogador.
"""

import time
import keyboard
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

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
    ...
    """
    x, y = jogador.posicao
    nova_posicao = (x, y)
    moveu = False
    dx, dy = 0, 0 # Inicializa delta
    
    if direcao:
        # Movimento automático (para IA) - Perfeito para match ... case
        match direcao:
            case 'up' | 'w':
                dx, dy = (-1, 0)
            case 'down' | 's':
                dx, dy = (1, 0)
            case 'left' | 'a':
                dx, dy = (0, -1)
            case 'right' | 'd':
                dx, dy = (0, 1)
            case _:
                dx, dy = (0, 0) # Direção inválida
        
        if (dx, dy) != (0, 0):
            nova_x, nova_y = x + dx, y + dy
            if (0 <= nova_x < len(labirinto) and 
                0 <= nova_y < len(labirinto[0]) and 
                labirinto[nova_x][nova_y] == " "):
                nova_posicao = (nova_x, nova_y)
                moveu = True
    else:
        # Movimento manual (if/elif é mais adequado aqui que match ... case)
        # Mapeamento de direções
        movimentos = {
            'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1),
            'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)
        }
        
        try:
            # Prioridade: WASD primeiro, depois setas
            teclas_prioridade = ['w', 'a', 's', 'd', 'up', 'left', 'down', 'right']
            
            for tecla in teclas_prioridade:
                if keyboard.is_pressed(tecla):
                    dx, dy = movimentos[tecla]
                    nova_x, nova_y = x + dx, y + dy
                    
                    # Verifica limites e se é espaço livre
                    if (0 <= nova_x < len(labirinto) and 
                        0 <= nova_y < len(labirinto[0]) and 
                        labirinto[nova_x][nova_y] == " "):
                        nova_posicao = (nova_x, nova_y)
                        moveu = True
                        break  # Para no primeiro movimento válido
        except Exception:
            # Ignora erros de teclado
            pass
    
    # Atualiza posição apenas se moveu
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
        
    Returns:
        str: Mensagem sobre a pontuação
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
        return f"+{bonus} pontos de bonus de tempo!"
    
    if penalidade > 0:
        # Penalidade por movimentos excessivos
        jogador.pontuacao = max(0, jogador.pontuacao - penalidade)
        return f"-{penalidade} pontos de penalidade"
    
    return ""

def exibir_status_jogador(console, jogador):
    """
    Exibe o status atual do jogador sem emojis.
    
    Args:
        console: Console do Rich
        jogador: Estado do jogador
        
    Returns:
        Panel: Painel com status do jogador
    """
    tempo_atual = time.time() - jogador.tempo_inicio
    
    # Cria texto do status sem emojis
    status = Text()
    status.append("Jogador: ", style="white")
    status.append(f"{jogador.nome}\n", style="bold blue")
    status.append("Pontuacao: ", style="white")
    status.append(f"{jogador.pontuacao}\n", style="bold yellow")
    status.append("Movimentos: ", style="white")
    status.append(f"{jogador.movimentos}\n", style="bold white")
    status.append("Tempo: ", style="white")
    status.append(f"{tempo_atual:.1f}s\n", style="bold green")
    status.append("Itens: ", style="white")
    status.append(f"{len(jogador.itens_coletados)}", style="bold cyan")
    
    painel = Panel(
        status,
        title="Status",
        border_style="blue",
        width=25
    )
    
    return painel

def resolver_labirinto(labirinto, inicio, fim, caminho_atual=None, visitados=None):
    """
    Função recursiva que encontra o caminho para resolver o labirinto.
    
    Args:
        labirinto: Matriz do labirinto
        inicio: Posição inicial (x, y)
        fim: Posição final (x, y) 
        caminho_atual: Caminho percorrido até agora
        visitados: Set de posições já visitadas
    
    Returns:
        list: Lista de movimentos para resolver ou None se impossível
    """
    if caminho_atual is None:
        caminho_atual = []
    if visitados is None:
        visitados = set()
    
    x, y = inicio
    
    # Chegou ao destino
    if inicio == fim:
        return caminho_atual
    
    # Marca posição atual como visitada
    visitados.add(inicio)
    
    # Tenta cada direção
    direcoes = [
        ((-1, 0), 'up'),    # Cima
        ((1, 0), 'down'),   # Baixo  
        ((0, -1), 'left'),  # Esquerda
        ((0, 1), 'right')   # Direita
    ]
    
    for (dx, dy), movimento in direcoes:
        nova_x, nova_y = x + dx, y + dy
        nova_pos = (nova_x, nova_y)
        
        # Verifica se a posição é válida, livre e não visitada
        if (0 <= nova_x < len(labirinto) and 
            0 <= nova_y < len(labirinto[0]) and 
            labirinto[nova_x][nova_y] == " " and
            nova_pos not in visitados):
            
            # Chamada recursiva
            resultado = resolver_labirinto(
                labirinto, 
                nova_pos, 
                fim, 
                caminho_atual + [movimento],
                visitados.copy()  # Cria nova cópia para cada ramo
            )
            
            if resultado is not None:
                return resultado
    
    return None  # Sem solução encontrada