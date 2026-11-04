# Asteroid Game

Projeto do clássico jogo de arcade **Asteroids**, desenvolvido em Python com a biblioteca **Pygame**. O projeto utiliza o gerenciador de pacotes **uv**.

## Funcionalidades 
* **Controle da Nave:** Movimentação fluida com rotação e aceleração.
* **Sistema de Tiros:** Dispare contra os alvos na tela.
* **Geração de Asteroides:** Asteroides surgem em posições e tamanhos aleatórios.
* **Divisão de Asteroides:** Ao serem atingidos, os asteroides grandes se dividem em pedaços menores.
* **Sistema de Pontuação:** Marcador simples para acompanhar o seu progresso durante a partida.

##  Tecnologias Utilizadas
* **[Python](https://python.org)** (v3.12 ou superior)
* **[Pygame-ce](https://github.org)** / **Pygame** (Para renderização 2D e física do jogo)
* **[uv](https://github.com)** (Para gerenciamento de dependências e ambiente virtual)

##  Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python e o gerenciador `uv` instalados na sua máquina. Se ainda não tiver o `uv`, instale com:
```bash
# No macOS/Linux
curl -LsSf https://astral.sh | sh

# No Windows (PowerShell)
powershell -c "irm https://astral.sh | iex"
```

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd asteroids
   ```

2. **Instale as dependências e sincronize o ambiente:**
   O `uv` lerá os arquivos `pyproject.toml` e `uv.lock` para criar o ambiente virtual automaticamente:
   ```bash
   uv sync
   ```

3. **Execute o jogo:**
   ```bash
   uv run main.py
   ```

##  Como Jogar
* `W` / `S` ou `Seta para Cima` / `Seta para Baixo` — Mover a nave para frente/trás.
* `A` / `D` ou `Seta para Esquerda` / `Seta para Direita` — Rotacionar a nave.
* `Espaço` — Atirar.

##  Estrutura do Projeto
* `main.py`: Ponto de entrada do jogo (loop principal e inicialização).
* `player.py`: Lógica do jogador, movimentação e tiros.
* `asteroid.py` & `asteroidfield.py`: Comportamento, movimentação e divisão dos asteroides.
* `circleshape.py`: Classe base para detecção de colisões baseada em círculos.
* `constants.py`: Configurações globais do jogo (largura da tela, velocidade, cores, etc.).
