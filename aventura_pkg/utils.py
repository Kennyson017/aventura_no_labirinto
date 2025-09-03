"""
Módulo de Utilidades
===================

Funções utilitárias para interface, menus e animações.
"""

import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.columns import Columns

def imprime_instrucoes(console, cor_tema="green"):
    """
    Imprime as instruções do jogo formatadas.
    
    Args:
        console: Console do Rich
        cor_tema: Cor do tema
    """
    instrucoes = f"""
[bold {cor_tema}]🎮 COMO JOGAR[/bold {cor_tema}]

[bold blue]Objetivo:[/bold blue]
• Navegue pelo labirinto até encontrar a saída ◉
• Colete itens pelo caminho para ganhar pontos
• Complete o mais rápido possível para bônus!

[bold blue]Controles:[/bold blue]
• [bold white]W, A, S, D[/bold white] ou [bold white]Setas[/bold white]: Mover
• [bold white]ESC[/bold white]: Sair do jogo

[bold blue]Símbolos:[/bold blue]
• [bold blue]@[/bold blue] = Você (jogador)
• [bold {cor_tema}]█[/bold {cor_tema}] = Paredes
• [bold white]·[/bold white] = Caminhos
• [bold red]◉[/bold red] = Saída
• [bold yellow]💎⭐🗝️💰🏆[/bold yellow] = Itens coletáveis

[bold blue]Pontuação:[/bold blue]
• Cada item vale entre 10-50 pontos
• Bônus de tempo ao completar
• Menos movimentos = mais pontos

[dim]Pressione qualquer tecla para continuar...[/dim]
    """
    
    painel = Panel(
        instrucoes.strip(),
        title="📚 Instruções",
        border_style=cor_tema,
        width=60
    )
    
    console.clear()
    console.print(Align.center(painel))

def mostrar_menu(console, nome_jogador, cor_tema="green"):
    """
    Mostra o menu principal do jogo.
    
    Args:
        console: Console do Rich
        nome_jogador: Nome do jogador
        cor_tema: Cor do tema
    
    Returns:
        str: Opção escolhida
    """
    titulo = Text("🏰 AVENTURA NO LABIRINTO 🏰", style=f"bold {cor_tema}")
    
    if nome_jogador:
        saudacao = Text(f"Bem-vindo(a), {nome_jogador}!", style="bold blue")
    else:
        saudacao = Text("Bem-vindo(a), Aventureiro!", style="bold blue")
    
    menu_options = """
[bold white]1.[/bold white] 🎮 Jogar
[bold white]2.[/bold white] 📚 Instruções  
[bold white]3.[/bold white] 🤖 Ver Solução Automática
[bold white]4.[/bold white] 🏆 Ranking (em breve)
[bold white]5.[/bold white] ❌ Sair

[dim]Digite o número da opção desejada:[/dim]
    """
    
    painel = Panel(
        menu_options.strip(),
        title="📋 Menu Principal",
        border_style=cor_tema,
        width=40
    )
    
    console.clear()
    console.print(Align.center(titulo))
    console.print()
    console.print(Align.center(saudacao))
    console.print()
    console.print(Align.center(painel))
    
    return input("\n> ").strip()

def mostrar_resultado_final(console, jogador, venceu, cor_tema="green"):
    """
    Mostra tela de resultado final.
    
    Args:
        console: Console do Rich
        jogador: Estado do jogador
        venceu: Se o jogador venceu
        cor_tema: Cor do tema
    """
    tempo_total = time.time() - jogador.tempo_inicio
    
    if venceu:
        titulo = Text("🏆 PARABÉNS! VOCÊ VENCEU! 🏆", style="bold green")
        mensagem = f"Excelente trabalho, {jogador.nome}!"
    else:
        titulo = Text("😔 JOGO ENCERRADO", style="bold red") 
        mensagem = f"Não desista, {jogador.nome}! Tente novamente!"
    
    # Tabela de estatísticas
    tabela = Table(title="📊 Suas Estatísticas")
    tabela.add_column("Métrica", style="bold white")
    tabela.add_column("Valor", style=f"bold {cor_tema}")
    
    tabela.add_row("🏆 Pontuação Final", str(jogador.pontuacao))
    tabela.add_row("👣 Movimentos", str(jogador.movimentos))
    tabela.add_row("⏱️ Tempo Total", f"{tempo_total:.1f}s")
    tabela.add_row("💎 Itens Coletados", str(len(jogador.itens_coletados)))
    
    # Performance
    if venceu:
        if jogador.movimentos < 50:
            performance = "🌟 Excelente!"
        elif jogador.movimentos < 100:
            performance = "⭐ Muito Bom!"
        else:
            performance = "✅ Bom trabalho!"
        tabela.add_row("🎯 Performance", performance)
    
    console.clear()
    console.print(Align.center(titulo))
    console.print()
    console.print(Align.center(Text(mensagem, style="bold blue")))
    console.print()
    console.print(Align.center(tabela))

def animacao_vitoria(console, profundidade=0):
    """
    Função recursiva que cria animação de vitória.
    
    Args:
        console: Console do Rich
        profundidade: Nível de recursão (controla a animação)
    """
    if profundidade >= 5:  # Para recursão após 5 níveis
        return
    
    # Símbolos e cores para animação
    simbolos = ["🎉", "🎊", "⭐", "🏆", "💫"]
    cores = ["red", "yellow", "green", "blue", "magenta"]
    
    # Cria texto animado baseado na profundidade
    texto_animado = Text()
    for i in range(profundidade + 1):
        simbolo = simbolos[i % len(simbolos)]
        cor = cores[i % len(cores)]
        texto_animado.append(f"{simbolo} ", style=f"bold {cor}")
    
    texto_animado.append("VITÓRIA! ", style="bold white")
    
    for i in range(profundidade + 1):
        simbolo = simbolos[-(i+1) % len(simbolos)]
        cor = cores[-(i+1) % len(cores)]
        texto_animado.append(f"{simbolo} ", style=f"bold {cor}")
    
    console.print(Align.center(texto_animado))
    time.sleep(0.3)
    
    # Chamada recursiva
    animacao_vitoria(console, profundidade + 1)

def escolher_dificuldade(console, cor_tema="green"):
    """
    Menu para escolher dificuldade do jogo.
    
    Args:
        console: Console do Rich
        cor_tema: Cor do tema
    
    Returns:
        int: Nível de dificuldade (1-3)
    """
    titulo = Text("⚔️ ESCOLHA A DIFICULDADE ⚔️", style=f"bold {cor_tema}")
    
    opcoes = """
[bold green]1.[/bold green] 🟢 Fácil (15x31) - 3 itens
[bold yellow]2.[/bold yellow] 🟡 Médio (21x41) - 5 itens  
[bold red]3.[/bold red] 🔴 Difícil (25x51) - 8 itens

[dim]Digite o número (1-3):[/dim]
    """
    
    painel = Panel(
        opcoes.strip(),
        title="🎯 Dificuldade",
        border_style=cor_tema,
        width=45
    )
    
    console.clear()
    console.print(Align.center(titulo))
    console.print()
    console.print(Align.center(painel))
    
    while True:
        try:
            opcao = int(input("\n> ").strip())
            if opcao in [1, 2, 3]:
                return opcao
            else:
                console.print("[bold red]Por favor, digite 1, 2 ou 3.[/bold red]")
        except ValueError:
            console.print("[bold red]Por favor, digite um número válido.[/bold red]")

def cores_disponiveis():
    """
    Retorna lista de cores disponíveis para o tema.
    
    Returns:
        list: Lista de cores disponíveis
    """
    return ["green", "blue", "red", "yellow", "magenta", "cyan", "white"]