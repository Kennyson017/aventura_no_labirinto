
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