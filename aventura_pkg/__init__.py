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
__author__ = "PD017 Kennyson Chaves"

from .labirinto import criar_labirinto, imprimir_labirinto, verificar_item_coletado
from .jogador import iniciar_jogador, mover, pontuar, resolver_labirinto, exibir_status_jogador
from .utils import (imprime_instrucoes, mostrar_menu, animacao_vitoria, 
                   escolher_dificuldade, cores_disponiveis, mostrar_resultado_final)

__all__ = [
    'criar_labirinto',
    'imprimir_labirinto',
    'verificar_item_coletado',
    'iniciar_jogador',
    'mover',
    'pontuar',
    'resolver_labirinto',
    'exibir_status_jogador',
    'imprime_instrucoes',
    'mostrar_menu',
    'animacao_vitoria',
    'escolher_dificuldade',
    'cores_disponiveis',
    'mostrar_resultado_final'
]