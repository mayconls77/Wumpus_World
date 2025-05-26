# 🗺️ Mundo Wumpus (Wumpus World)

Um jogo clássico de lógica e aventura implementado em Python, baseado no famoso "Hunt the Wumpus" de Gregory Yob (1973).

## 📖 Sobre o Jogo

Você é um aventureiro corajoso explorando uma caverna perigosa em busca de ouro. A caverna é habitada pelo terrível **Wumpus** - uma criatura que devora qualquer um que se aproxime. Além disso, existem **poços mortais** espalhados pela caverna.

Sua missão: **encontrar o ouro e escapar com vida!**

## 🎯 Objetivo

1. **Explore** a caverna usando pistas sensoriais
2. **Encontre** o ouro dourado
3. **Evite** o Wumpus e os poços mortais
4. **Escape** da caverna retornando à entrada (posição 0,0)

## 🕹️ Como Jogar

### Controles
```
w - Mover para frente
a - Virar à esquerda
d - Virar à direita
g - Pegar ouro
s - Atirar flecha
c - Sair da caverna (só na posição 0,0)
h - Mostrar ajuda
m - Mostrar mapa completo (debug)
q - Sair do jogo
```

### Elementos do Mundo
- **🤖 Jogador:** Representado por setas direcionais (↑→↓←)
- **👹 Wumpus:** Criatura mortal que te devora
- **🕳️ Poços:** Buracos profundos onde você pode cair
- **💰 Ouro:** Tesouro que você deve coletar
- **❓ Inexplorado:** Áreas ainda não visitadas

### Percepções (Pistas)
- **💨 Brisa:** Indica que há um poço em uma sala adjacente
- **💀 Fedor:** Indica que o Wumpus está em uma sala adjacente
- **✨ Brilho:** Você encontrou o ouro!

## 🧠 Estratégia

### Dicas de Sobrevivência
1. **Use a lógica:** Se sente brisa, há um poço ao lado
2. **Mapeie mentalmente:** Lembre-se das pistas de cada posição
3. **Seja cauteloso:** Só avance quando tiver certeza da segurança
4. **Use a flecha sabiamente:** Você tem apenas uma flecha para matar o Wumpus
5. **Planeje a fuga:** Lembre-se do caminho de volta para (0,0)

### Exemplo de Raciocínio
```
Posição (0,0): Sinto brisa + fedor
↓ Isso significa:
- Há um poço em (0,1) ou (1,0)
- O Wumpus está em (0,1) ou (1,0)
- Uma das posições adjacentes tem ambos os perigos!
```

## 🏆 Sistema de Pontuação

| Ação | Pontos |
|------|--------|
| Movimento | -1 |
| Virar | -1 |
| Atirar flecha | -10 |
| Matar Wumpus | +500 |
| Pegar ouro | +1000 |
| Escapar com ouro | +1000 |
| Morrer | -1000 |

**Objetivo:** Maximize sua pontuação completando o jogo rapidamente!

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Instalação e Execução
```bash
# Clone ou baixe o arquivo wumpus_world.py
python wumpus_world.py
```

### Menu Principal
```
=== MUNDO WUMPUS ===
1. Novo Jogo (4x4)
2. Novo Jogo (5x5)
3. Sair
```

## 🎮 Interface do Jogo

```
🗺️  MUNDO WUMPUS
────────────────────────────────────────
Pos:(0,0) | Dir:Norte | Score:0 | Flecha:✓ | Ouro:✗
➤ 🎮 Jogo iniciado!

   0  1  2  3 
0  ↑  ❓ ❓ ❓ 
1  ❓ ❓ ❓ ❓ 
2  ❓ ❓ ❓ ❓ 
3  ❓ ❓ ❓ ❓ 

👁️  Você sente uma brisa... | Você sente um fedor terrível...

Comando [w/a/d/g/s/c/h/m/q]: 
```

## 🧩 Características Técnicas

### Arquitetura
- **Orientado a objetos:** Classe `WumpusWorld` encapsula toda a lógica
- **Modular:** Métodos separados para cada funcionalidade
- **Configurável:** Tamanhos de mundo variáveis (4x4, 5x5)

### Recursos Implementados
- ✅ Geração aleatória de mundo
- ✅ Sistema de percepções realista
- ✅ Interface visual com emojis
- ✅ Sistema de pontuação completo
- ✅ Modo debug para desenvolvimento
- ✅ Controles intuitivos e responsivos
- ✅ Feedback visual imediato

### Algoritmos Utilizados
- **Geração de mundo:** Posicionamento aleatório com validação
- **Sistema de percepções:** Propagação de efeitos para células adjacentes
- **Detecção de colisões:** Validação de movimentos e limites
- **Trajetória de projétil:** Simulação do voo da flecha

## 🎓 Valor Educacional

Este jogo é amplamente usado em:
- **Cursos de Inteligência Artificial**
- **Ensino de lógica proposicional**
- **Sistemas baseados em conhecimento**
- **Algoritmos de busca e reasoning**

### Conceitos Demonstrados
- Raciocínio sob incerteza
- Representação de conhecimento
- Tomada de decisão baseada em evidências
- Planejamento de ações sequenciais

## 🔧 Possíveis Melhorias

### Funcionalidades Futuras
- [ ] Interface gráfica (Pygame/Tkinter)
- [ ] Sistema de níveis de dificuldade
- [ ] Múltiplos Wumpus
- [ ] Powerups e itens especiais
- [ ] Sistema de rankings/leaderboard
- [ ] Modo multiplayer
- [ ] IA para jogar automaticamente

### Otimizações
- [ ] Salvamento de progresso
- [ ] Configurações personalizáveis
- [ ] Sons e efeitos visuais
- [ ] Tutorial interativo

## 📚 Referências

- **Jogo Original:** Hunt the Wumpus - Gregory Yob (1973)
- **Livro:** "Artificial Intelligence: A Modern Approach" - Russell & Norvig
- **Aplicação em IA:** Exemplo clássico de ambiente parcialmente observável

## 👥 Contribuições

Contribuições são bem-vindas! Algumas áreas para melhoria:
- Interface gráfica
- Novos tipos de sensores/perigos
- Algoritmos de IA para agentes automáticos
- Otimização de performance

## 📄 Licença

Este projeto é livre para uso educacional e pessoal.

---

**Divirta-se explorando o perigoso Mundo Wumpus! 🎮✨**
