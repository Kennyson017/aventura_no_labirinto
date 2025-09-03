Trabalho Prático I - Jogo do Labirinto

Aventura no Labirinto
Você vai criar um jogo chamado "Aventura no Labirinto", onde o jogador explora um labirinto interagindo via terminal. O projeto precisa exercitar tudo que aprendemos no módulo 1, ou seja:

 

Conter pelo menos uma função recursiva

Conter pelo menos um match-case (a forma mais simples é nas opções do menu).

Executar em um ambiente virtual com bibliotecas externas instaladas (e criar um requirements.txt desse ambiente)

Ser implementado de forma modular

Adicionar docstrings a todos os módulos e funções do pacote que criaremos e exporte o html da documentação

Implementar uma CLI com opções e argumentos para execução

 

Agora vamos detalhar um pouco as regras

Ambientes Virtuais
Ser criado em um ambiente virtual onde você vai instalar todas as bibliotecas externas necessárias. Ao final você deve exportar um arquivo requirements.txt para adicionar ao GitHub do projeto.

Escolha uma biblioteca externa para "embelezar" o terminal

Como tudo será via linha de comando, não precisa ser chato e monocromático. Vamos usar uma biblioteca que enriquece as possibilidades da linha de comando.

Sugestão: https://github.com/Textualize/rich

Biblioteca externa para ler o teclado no terminal

Sugestão: https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

 

Exemplo de uso das bibliotecas externas:

https://github.com/camilalaranjeira/python-intermediario/blob/main/exemplo_keyboard/main.py

Implementação Modular
Seu projeto deve ter a estrutura apresentada a seguir, contendo um pacote com três módulos, além de um main.py com o controle principal do sistema. Os outros arquivos se referem à documentação e configurações de ambiente. A seguir você encontra uma descrição de cada um dos arquivos que sua solução deve possuir.




aventura_no_labirinto/ 

├── aventura_pkg/ 

│ ├── __init__.py 

│ ├── labirinto.py 

│ ├── jogador.py 

│ └── utils.py 

├── main.py 

├── requirements.txt 

├── aventura_pkg.html

└── README.md

labirinto.py
Pelo menos duas funções: criar_labirinto() e imprimir_labirinto(). O labirinto pode, por exemplo, ser lido de arquivo ou gerado aleatoriamente. Mas não pode ser uma string ou outra estrutura pré-escrita no script. 

Solte sua criatividade. Que tal colocar items no labirinto para o jogador coletar? Isso exigiria uma checagem se o jogador e o item estão na mesma posição.

jogador.py
Crie as funções necessárias para controlar a movimentação (biblioteca pynput) e a pontuação do jogador.

Uma (de muitas) sugestões são as funções:

iniciar_jogador() que desenha o jogador na posição inicial do labirinto e inicia sua pontuação.

mover() que lê o teclado e altera a posição do jogador.

pontuar() que atualiza a pontuação de acordo com as regras. Use a criatividade.

Desafio: criar uma função recursiva que retorna a lista de comandos para resolver o labirinto. Você pode criar um labirinto mais simples para testar sua função. Crie uma opção no menu inicial para assistir o personagem do jogo executar os movimentos da solução recursiva.

utils.py
Você deve adicionar pelo menos duas funções utilitárias. Por exemplo a função imprime_instrucoes() que lê as instruções de um arquivo e imprime formatada (rich text) na tela.

Outra sugestão é terceirizar a impressão do menu para esse módulo, para que você tenha liberdade de formatá-lo para impressão sem crescer tanto o main.

main.py
Você deve implementar uma CLI para executar o main. Defina pelo menos 5 elementos (argumentos, opções, parâmetros) sendo pelo menos uma delas obrigatória. Sugestões:

--name <nome>: Nome do(a) jogador(a)

--color <cor>: Escolher a cor principal do jogo

--dificuldade <x>: Crie mais de um labirinto e deixe o(a) jogador(a) escolher

--disable-sound: Que tal colocar música no jogo com uma opção para desligar? (playsound)

--help: Personalize o help padrão

Aqui é onde tudo acontece. Ao iniciar, o jogo deve apresentar um menu de opções (pelo menos "instruções" e "jogar"). Nessa etapa você pode pedir o nome do(a) jogador(a) para formatar as mensagens na tela.

Ao iniciar o jogo e imprimir o labirinto e o(a) jogador(a) na tela, se inicia um laço (infinito ou com máximo de movimentos) chamando as funções de jogo (mover, pontuar, etc.).

Ao final, crie uma tela formatada de vitória ou derrota (talvez no módulo utils?) se despedindo do(a) jogador(a).

Sugestão: que tal incluir aqui a sua função recursiva? Crie no módulo utils uma função recursiva que faz uma animação simples para celebrar a vitória do(a) jogador(a).

README.md
Seu projeto no GitHub deve ter um readme introduzindo o jogo (com prints de telas), além de instruções de como executar e como jogar.

requirements.txt
Exporte as dependências instaladas em seu ambiente virtual

aventura_pkg.html
Exporte as docstrings do seu pacote aventura_pkg para o arquivo aventura_pkg.html

# 🏰 Aventura no Labirinto

Um jogo interativo de labirinto desenvolvido em Python com interface rica e controles fluidos.

## 📋 Características

- **🎨 Interface rica** com biblioteca Rich
- **🎮 Controles fluidos** - WASD ou setas
- **💎 Sistema de itens** coletáveis com pontuação
- **⚔️ Três níveis de dificuldade** (Fácil, Médio, Difícil)
- **🤖 IA que resolve labirintos** automaticamente
- **🏆 Sistema de pontuação** com bônus de tempo
- **🎨 Temas de cores** personalizáveis
- **📊 Estatísticas detalhadas** do jogador

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone <repo-url>
cd aventura_no_labirinto
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎮 Como Jogar

### Uso Básico (Obrigatório especificar nome):
```bash
python main.py --name "Seu Nome"
```

### Opções Avançadas:
```bash
# Com cor personalizada e dificuldade
python main.py --name "João" --color blue --dificuldade 2

# Sem som
python main.py --name "Maria" --disable-sound

# Jogo direto (sem menu)
python main.py --name "Pedro" --auto-play --dificuldade 1
```

### Argumentos CLI:

| Argumento | Tipo | Descrição |
|-----------|------|-----------|
| `--name` | **Obrigatório** | Nome do jogador |
| `--color` | Opcional | Cor do tema (green, blue, red, yellow, magenta, cyan, white) |
| `--dificuldade` | Opcional | Nível: 1=Fácil, 2=Médio, 3=Difícil |
| `--disable-sound` | Flag | Desabilita efeitos sonoros |
| `--auto-play` | Flag | Inicia jogo diretamente |

## 🎯 Controles

- **W, A, S, D** ou **Setas**: Mover jogador
- **ESC**: Sair do jogo

## 🎮 Símbolos do Jogo

| Símbolo | Significado |
|---------|-------------|
| @ | Jogador (você) |
| █ | Paredes |
| · | Caminhos |
| ◉ | Saída |
| 💎⭐🗝️💰🏆 | Itens coletáveis |

## 📊 Sistema de Pontuação

- **Itens coletados**: 10-50 pontos cada
- **Bônus de tempo**: Até 100 pontos extras
- **Performance**: Menos movimentos = melhor classificação

## 🏗️ Estrutura do Projeto

```
aventura_no_labirinto/
├── aventura_pkg/
│   ├── __init__.py          # Inicialização do pacote
│   ├── labirinto.py         # Geração e impressão de labirintos
│   ├── jogador.py           # Controle do jogador e IA
│   └── utils.py             # Funções utilitárias e interface
├── main.py                  # CLI e loop principal
├── requirements.txt         # Dependências
└── README.md               # Este arquivo
```

## 🔧 Módulos

### 📦 `labirinto.py`
- `criar_labirinto()`: Gera labirintos proceduralmente
- `imprimir_labirinto()`: Renderiza labirinto com cores
- `verificar_item_coletado()`: Sistema de itens

### 🎮 `jogador.py`  
- `iniciar_jogador()`: Inicializa estado do jogador
- `mover()`: Controla movimentação manual e automática
- `pontuar()`: Sistema de pontuação
- `resolver_labirinto()`: **IA recursiva** que resolve labirintos

### 🛠️ `utils.py`
- `imprime_instrucoes()`: Instruções formatadas
- `mostrar_menu()`: Interface de menu
- `animacao_vitoria()`: **Animação recursiva** de celebração
- `escolher_dificuldade()`: Seleção de nível

## 🤖 Funcionalidades Especiais

### IA que Resolve Labirintos
A função `resolver_labirinto()` usa **recursão** para encontrar o caminho até a saída:
- Algoritmo de backtracking
- Visualização em tempo real
- Demonstração automática dos movimentos

### Animação Recursiva
A função `animacao_vitoria()` cria uma celebração animada usando recursão:
- Efeitos visuais crescentes
- Cores e símbolos dinâmicos
- Profundidade controlada automaticamente

## 🎨 Temas de Cores

Escolha entre 7 temas de cores:
- `green` (padrão)
- `blue` 
- `red`
- `yellow`
- `magenta` 
- `cyan`
- `white`

## 🐛 Solução de Problemas

### Erro de Permissões (Linux/Mac):
```bash
sudo pip install -r requirements.txt
```

### Problemas com Teclado:
- Execute como administrador (Windows)
- No Linux: `sudo python main.py --name "Nome"`

### Dependências em Conflito:
```bash
pip install --upgrade rich keyboard playsound
```

## 🚀 Exemplos de Uso

### Jogo Rápido:
```bash
python main.py --name "Aventureiro" --color green --dificuldade 1
```

### Modo Silencioso:
```bash
python main.py --name "João" --disable-sound --auto-play
```

### Ver IA em Ação:
```bash
python main.py --name "Observer"
# Escolha opção 3 no menu
```

## 📈 Próximas Funcionalidades

- 🏆 Sistema de ranking persistente
- 🎵 Trilha sonora dinâmica
- 🌟 Mais tipos de itens especiais
- 🗺️ Editor de labirintos customizados
- 👥 Modo multiplayer local

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar documentação
- Otimizar código

## 📜 Licença

Este projeto é open source. Use e modifique livremente!

---

**Divirta-se explorando labirintos! 🏰✨**