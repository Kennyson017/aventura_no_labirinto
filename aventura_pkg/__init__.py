"""
Pacote Aventura no Labirinto
==========================

Um jogo de labirinto interativo com Rich e controles fluidos.

Módulos:
- labirinto: Geração e impressão de labirintos
- jogador: Controle do jogador e pontuação  
- utils: Funções utilitárias e interface
"""

__version__ = "1.0.0"
__author__ = "Aventureiro do Código"

from .labirinto import criar_labirinto, imprimir_labirinto
from .jogador import iniciar_jogador, mover, pontuar, resolver_labirinto
from .utils import imprime_instrucoes, mostrar_menu, animacao_vitoria

__all__ = [
    'criar_labirinto',
    'imprimir_labirinto', 
    'iniciar_jogador',
    'mover',
    'pontuar',
    'resolver_labirinto',
    'imprime_instrucoes',
    'mostrar_menu',
    'animacao_vitoria'
]