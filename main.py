#!/usr/bin/env python3
"""
AVENTURA NO LABIRINTO
====================

Jogo interativo de labirinto com Rich, controles fluidos e itens coletáveis.

Uso:
    python main.py --name "Seu Nome" [opções]

Exemplo:
    python main.py --name "João" --color blue --dificuldade 2
"""

import argparse
import time
import sys
import os
import keyboard
from rich.console import Console  
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text

# Importa módulos do pacote
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto, verificar_item_coletado
from aventura_pkg.jogador import iniciar_jogador, mover, pontuar, exibir_status_jogador, resolver_labirinto
from aventura_pkg.utils import (imprime_instrucoes, mostrar_menu, mostrar_resultado_final, 
                               animacao_vitoria, escolher_dificuldade, cores_disponiveis)

def criar_parser():
    """Cria parser CLI com argumentos obrigatórios e opcionais."""
    parser = argparse.ArgumentParser(
        description="Aventura no Labirinto - Um jogo interativo!",
        epilog="Divirta-se explorando labirintos e coletando tesouros!",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Argumentos obrigatórios
    parser.add_argument(
        "--name", 
        required=True,
        help="Nome do jogador (obrigatório)"
    )
    
    # Argumentos opcionais
    parser.add_argument(
        "--color", 
        choices=cores_disponiveis(),
        default="green",
        help="Cor principal do jogo (padrão: green)"
    )
    
    parser.add_argument(
        "--dificuldade",
        type=int,
        choices=[1, 2, 3], 
        help="Nível de dificuldade: 1=Fácil, 2=Médio, 3=Difícil"
    )
    
    parser.add_argument(
        "--disable-sound",
        action="store_true",
        help="Desabilita efeitos sonoros do jogo"
    )
    
    parser.add_argument(
        "--auto-play",
        action="store_true", 
        help="Inicia diretamente o jogo sem menu"
    )
    
    return parser

def executar_jogo(console, nome, dificuldade, cor_tema, som_habilitado):
    """
    Executa o loop principal do jogo.
    
    Args:
        console: Console do Rich
        nome: Nome do jogador
        dificuldade: Nível de dificuldade
        cor_tema: Cor do tema
        som_habilitado: Se som está habilitado
    """
    # Cria labirinto e inicializa jogador
    labirinto, itens, entrada, saida = criar_labirinto(dificuldade=dificuldade)
    jogador = iniciar_jogador(nome, entrada)
    
    # Estado do jogo
    last_move_time = 0
    venceu = False
    itens_coletados = set()  # Usa set para rastrear posições coletadas
    
    def renderizar_jogo():
        """Renderiza o jogo completo"""
        # Layout principal
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body"),
            Layout(name="footer", size=4)
        )
        
        # Header com título
        titulo = Text()
        titulo.append("AVENTURA NO LABIRINTO", style=f"bold {cor_tema}")
        titulo.append(f" - Nivel {dificuldade}", style="dim")
        
        layout["header"].update(
            Panel(titulo, style=f"bold {cor_tema}")
        )
        
        # Body com labirinto e status
        layout["body"].split_row(
            Layout(name="maze", ratio=3),
            Layout(name="status", ratio=1)
        )
        
        # Labirinto
        maze_text = imprimir_labirinto(
            console, labirinto, jogador.posicao, 
            itens, itens_coletados, cor_tema
        )
        layout["maze"].update(
            Panel(maze_text, title="Labirinto", border_style=cor_tema)
        )
        
        # Status do jogador
        status_panel = exibir_status_jogador(console, jogador)
        layout["status"].update(status_panel)
        
        # Footer com controles
        controles = Text()
        controles.append("Controles: ", style="dim")
        controles.append("WASD", style="bold white")
        controles.append(" ou ", style="dim")
        controles.append("Setas", style="bold white") 
        controles.append(" = Mover | ", style="dim")
        controles.append("ESC", style="bold white")
        controles.append(" = Sair", style="dim")
        
        layout["footer"].update(Panel(controles, style="dim"))
        
        return layout
    
    console.clear()
    console.print(f"[bold {cor_tema}]Iniciando jogo para {nome}...[/bold {cor_tema}]")
    time.sleep(1)
    
    # Renderização inicial
    current_layout = renderizar_jogo()
    console.clear()
    console.print(current_layout)
    
    # Loop principal sem Live para evitar flickering
    while True:
        current_time = time.time()
        
        # Verifica vitória
        if jogador.posicao == saida:
            venceu = True
            break
        
        # Controle de movimento com throttling
        moved = False
        try:
            if current_time - last_move_time > 0.15:  # Throttle mais alto
                _, moved = mover(jogador, labirinto)
                if moved:
                    last_move_time = current_time
                    
                    # Verifica se coletou item APENAS quando se move
                    item_coletado = verificar_item_coletado(jogador.posicao, itens, itens_coletados)
                    if item_coletado:
                        itens_coletados.add(jogador.posicao)  # Marca como coletado
                        mensagem_pontos = pontuar(jogador, item_coletado)
                        # Som opcional aqui
                    
                    # Re-renderiza apenas quando há movimento
                    console.clear()
                    console.print(renderizar_jogo())
            
            if keyboard.is_pressed('esc'):
                break
                
        except:
            pass
        
        # Sleep menor para responsividade
        time.sleep(0.05)
    
    # Calcula pontuação final
    if venceu:
        pontuar(jogador, bonus_tempo=True)
    
    return venceu, jogador

def demonstrar_solucao(console, nome, dificuldade, cor_tema):
    """
    Demonstra a solução automática do labirinto.
    """
    console.clear()
    console.print(f"[bold {cor_tema}]Calculando solucao automatica...[/bold {cor_tema}]")
    
    # Cria labirinto menor para demonstração
    labirinto, itens, entrada, saida = criar_labirinto(linhas=15, colunas=31, dificuldade=1)
    
    # Calcula solução
    solucao = resolver_labirinto(labirinto, entrada, saida)
    
    if not solucao:
        console.print("[bold red]Nao foi possivel encontrar uma solucao![/bold red]")
        input("\nPressione Enter para continuar...")
        return
    
    console.print(f"[bold green]Solucao encontrada com {len(solucao)} movimentos![/bold green]")
    console.print("[dim]Pressione Enter para ver a demonstracao...[/dim]")
    input()
    
    # Cria jogador virtual
    jogador_ai = iniciar_jogador("IA", entrada)
    
    console.clear()
    for i, movimento in enumerate(solucao):
        mover(jogador_ai, labirinto, movimento)
        
        # Renderiza sem emojis
        maze_text = imprimir_labirinto(console, labirinto, jogador_ai.posicao, {}, set(), cor_tema)
        titulo = f"IA Resolvendo - Movimento {i+1}/{len(solucao)}"
        panel = Panel(maze_text, title=titulo, border_style=cor_tema)
        
        console.clear()
        console.print(panel)
        time.sleep(0.3)  # Pausa para visualização
    
    console.print("\n[bold green]IA completou o labirinto![/bold green]")
    input("Pressione Enter para continuar...")

def main():
    """Função principal do jogo."""
    console = Console()
    
    try:
        # Parse dos argumentos CLI
        parser = criar_parser()
        args = parser.parse_args()
        
        # Extrai argumentos
        nome = args.name
        cor_tema = args.color
        som_habilitado = not args.disable_sound
        auto_play = args.auto_play
        dificuldade = args.dificuldade
        
        # Mensagem de boas-vindas
        console.clear()
        console.print(f"[bold {cor_tema}]Bem-vindo ao Aventura no Labirinto, {nome}![/bold {cor_tema}]")
        
        if som_habilitado:
            console.print("[dim]Som habilitado[/dim]")
        else:
            console.print("[dim]Som desabilitado[/dim]")
        
        time.sleep(1)
        
        # Se dificuldade não foi especificada, pergunta
        if not dificuldade:
            dificuldade = escolher_dificuldade(console, cor_tema)
        
        # Se for auto-play, inicia jogo diretamente
        if auto_play:
            venceu, jogador_final = executar_jogo(console, nome, dificuldade, cor_tema, som_habilitado)
            mostrar_resultado_final(console, jogador_final, venceu, cor_tema)
            if venceu:
                animacao_vitoria(console)
            return
        
        # Loop principal do menu
        while True:
            opcao = mostrar_menu(console, nome, cor_tema)
            
            match opcao:
                case "1":  # Jogar
                    venceu, jogador_final = executar_jogo(console, nome, dificuldade, cor_tema, som_habilitado)
                    mostrar_resultado_final(console, jogador_final, venceu, cor_tema)
                    if venceu:
                        animacao_vitoria(console)
                    input("\nPressione Enter para continuar...")
                    
                case "2":  # Instruções
                    imprime_instrucoes(console, cor_tema)
                    input()
                    
                case "3":  # Demonstração IA
                    demonstrar_solucao(console, nome, dificuldade, cor_tema)
                    
                case "4":  # Ranking (em breve)
                    console.clear()
                    console.print("[bold yellow]Sistema de ranking em desenvolvimento![/bold yellow]")
                    input("Pressione Enter para continuar...")
                    
                case "5":  # Sair
                    console.clear()
                    console.print(f"[bold {cor_tema}]Obrigado por jogar, {nome}![/bold {cor_tema}]")
                    console.print("[dim]Ate a proxima aventura![/dim]")
                    break  # Sai do loop while
                    
                case _:  # Caso padrão (substitui o 'else')
                    console.print("[bold red]Opcao invalida! Tente novamente.[/bold red]")
                    time.sleep(1)
    
    except KeyboardInterrupt:
        console.clear()
        console.print("\n[bold red]Jogo interrompido pelo usuario.[/bold red]")
        console.print("[dim]Obrigado por jogar![/dim]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[bold red]Erro inesperado: {e}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()