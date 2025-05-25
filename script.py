import random
import os


class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.world = [[0 for _ in range(size)] for _ in range(size)]
        self.player_pos = [0, 0]
        self.player_direction = 0  # 0=Norte, 1=Leste, 2=Sul, 3=Oeste
        self.has_arrow = True
        self.has_gold = False
        self.game_over = False
        self.victory = False
        self.score = 0

        # Códigos para elementos do mundo
        self.WUMPUS = 1
        self.PIT = 2
        self.GOLD = 4
        self.BREEZE = 8
        self.STENCH = 16

        self.directions = ['Norte', 'Leste', 'Sul', 'Oeste']
        self.moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Norte, Leste, Sul, Oeste

        self.setup_world()

    def setup_world(self):
        """Configura o mundo com Wumpus, poços e ouro"""
        # Limpa o mundo
        self.world = [[0 for _ in range(self.size)] for _ in range(self.size)]

        # Coloca o Wumpus (1 apenas)
        wumpus_pos = self.get_random_position(exclude=[(0, 0)])
        self.world[wumpus_pos[0]][wumpus_pos[1]] |= self.WUMPUS

        # Coloca poços (2-3 poços)
        num_pits = random.randint(2, 3)
        for _ in range(num_pits):
            pit_pos = self.get_random_position(exclude=[(0, 0), wumpus_pos])
            self.world[pit_pos[0]][pit_pos[1]] |= self.PIT

        # Coloca o ouro
        gold_pos = self.get_random_position(exclude=[(0, 0), wumpus_pos])
        self.world[gold_pos[0]][gold_pos[1]] |= self.GOLD

        # Adiciona brisas adjacentes aos poços
        for i in range(self.size):
            for j in range(self.size):
                if self.world[i][j] & self.PIT:
                    self.add_adjacent_effect(i, j, self.BREEZE)

        # Adiciona fedor adjacente ao Wumpus
        for i in range(self.size):
            for j in range(self.size):
                if self.world[i][j] & self.WUMPUS:
                    self.add_adjacent_effect(i, j, self.STENCH)

    def get_random_position(self, exclude=[]):
        """Retorna uma posição aleatória válida"""
        while True:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos not in exclude:
                # Verifica se a posição não tem outros elementos
                if self.world[pos[0]][pos[1]] == 0:
                    return pos

    def add_adjacent_effect(self, row, col, effect):
        """Adiciona efeito nas células adjacentes"""
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                self.world[new_row][new_col] |= effect

    def is_valid_position(self, row, col):
        """Verifica se a posição é válida"""
        return 0 <= row < self.size and 0 <= col < self.size

    def get_perceptions(self):
        """Retorna as percepções do jogador na posição atual"""
        row, col = self.player_pos
        perceptions = []

        if self.world[row][col] & self.BREEZE:
            perceptions.append("Você sente uma brisa...")

        if self.world[row][col] & self.STENCH:
            perceptions.append("Você sente um fedor terrível...")

        if self.world[row][col] & self.GOLD:
            perceptions.append("Você vê um brilho dourado!")

        return perceptions

    def move_forward(self):
        """Move o jogador para frente"""
        if self.game_over:
            return False

        dr, dc = self.moves[self.player_direction]
        new_row = self.player_pos[0] + dr
        new_col = self.player_pos[1] + dc

        print(f"Tentando mover de ({self.player_pos[0]}, {self.player_pos[1]}) para ({new_row}, {new_col})")
        print(f"Direção: {self.directions[self.player_direction]} ({dr}, {dc})")

        if not self.is_valid_position(new_row, new_col):
            print("Você bateu na parede!")
            input("Pressione Enter para continuar...")
            return False

        self.player_pos = [new_row, new_col]
        self.score -= 1  # Custo por movimento

        print(f"Movimento realizado! Nova posição: ({self.player_pos[0]}, {self.player_pos[1]})")

        # Verifica perigos
        cell = self.world[new_row][new_col]

        if cell & self.WUMPUS:
            print("\n💀 Você foi devorado pelo Wumpus!")
            self.game_over = True
            self.score -= 1000
            input("Pressione Enter para continuar...")
            return False

        if cell & self.PIT:
            print("\n🕳️ Você caiu em um poço!")
            self.game_over = True
            self.score -= 1000
            input("Pressione Enter para continuar...")
            return False

        input("Pressione Enter para continuar...")
        return True

    def turn_left(self):
        """Vira o jogador para a esquerda"""
        if not self.game_over:
            old_direction = self.directions[self.player_direction]
            self.player_direction = (self.player_direction - 1) % 4
            new_direction = self.directions[self.player_direction]
            print(f"Virou à esquerda: {old_direction} → {new_direction}")
            self.score -= 1
            input("Pressione Enter para continuar...")

    def turn_right(self):
        """Vira o jogador para a direita"""
        if not self.game_over:
            old_direction = self.directions[self.player_direction]
            self.player_direction = (self.player_direction + 1) % 4
            new_direction = self.directions[self.player_direction]
            print(f"Virou à direita: {old_direction} → {new_direction}")
            self.score -= 1
            input("Pressione Enter para continuar...")

    def grab_gold(self):
        """Pega o ouro se estiver na mesma posição"""
        if self.game_over:
            return False

        row, col = self.player_pos
        if self.world[row][col] & self.GOLD:
            self.has_gold = True
            self.world[row][col] &= ~self.GOLD  # Remove o ouro do mundo
            self.score += 1000
            print("✨ Você pegou o ouro!")
            return True
        else:
            print("Não há ouro aqui.")
            return False

    def shoot_arrow(self):
        """Atira uma flecha na direção atual"""
        if not self.has_arrow:
            print("Você não tem mais flechas!")
            return False

        if self.game_over:
            return False

        self.has_arrow = False
        self.score -= 10

        # Trajetória da flecha
        row, col = self.player_pos
        dr, dc = self.moves[self.player_direction]

        # A flecha voa até encontrar algo ou sair do mundo
        while True:
            row += dr
            col += dc

            if not self.is_valid_position(row, col):
                print("🏹 A flecha voou para fora da caverna...")
                return False

            if self.world[row][col] & self.WUMPUS:
                print("🎯 Você acertou o Wumpus! Ele está morto!")
                self.world[row][col] &= ~self.WUMPUS  # Remove o Wumpus
                self.score += 500
                return True

        return False

    def climb_out(self):
        """Sai da caverna (só funciona na posição inicial)"""
        if self.player_pos == [0, 0]:
            if self.has_gold:
                print("🏆 Parabéns! Você escapou com o ouro!")
                self.victory = True
                self.score += 1000
            else:
                print("🚪 Você saiu da caverna, mas sem o ouro...")
            self.game_over = True
            return True
        else:
            print("Você só pode sair da caverna na posição inicial (0,0)!")
            return False

    def display_world(self, show_all=False):
        """Exibe o mundo (modo debug mostra tudo)"""
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=== MUNDO WUMPUS ===")
        print(f"Posição: (linha {self.player_pos[0]}, coluna {self.player_pos[1]})")
        print(f"Direção: {self.directions[self.player_direction]}")
        print(f"Pontuação: {self.score}")
        print(f"Flecha: {'Sim' if self.has_arrow else 'Não'}")
        print(f"Ouro: {'Sim' if self.has_gold else 'Não'}")
        print()

        # Mostra indicador de direção
        direction_arrows = ['↑', '→', '↓', '←']
        print(f"Jogador olhando para: {direction_arrows[self.player_direction]}")
        print()

        # Exibe o tabuleiro com coordenadas
        print("   ", end="")
        for j in range(self.size):
            print(f" {j} ", end="")
        print()

        for i in range(self.size):
            print(f"{i}  ", end="")
            for j in range(self.size):
                if [i, j] == self.player_pos:
                    # Mostra jogador com direção
                    print(f"{direction_arrows[self.player_direction]} ", end=" ")
                elif show_all:
                    cell = self.world[i][j]
                    if cell & self.WUMPUS:
                        print("👹", end=" ")
                    elif cell & self.PIT:
                        print("🕳️", end=" ")
                    elif cell & self.GOLD:
                        print("💰", end=" ")
                    else:
                        print("⬜", end=" ")
                else:
                    print("❓", end=" ")
            print()

        print()

        # Mostra percepções
        perceptions = self.get_perceptions()
        if perceptions:
            print("Percepções:")
            for perception in perceptions:
                print(f"- {perception}")
        else:
            print("Tudo parece normal...")
        print()

    def get_help(self):
        """Mostra ajuda do jogo"""
        help_text = """
=== COMANDOS ===
w - Mover para frente
a - Virar à esquerda
d - Virar à direita
g - Pegar ouro
s - Atirar flecha
c - Sair da caverna (só na posição 0,0)
h - Mostrar esta ajuda
m - Mostrar mapa completo (debug)
q - Sair do jogo

=== OBJETIVO ===
- Encontre o ouro e escape da caverna
- Evite o Wumpus (👹) e os poços (🕳️)
- Use pistas: brisa indica poço próximo, fedor indica Wumpus próximo

=== PONTUAÇÃO ===
- Movimento: -1 ponto
- Virar: -1 ponto
- Atirar flecha: -10 pontos
- Matar Wumpus: +500 pontos
- Pegar ouro: +1000 pontos
- Escapar com ouro: +1000 pontos extra
- Morrer: -1000 pontos
"""
        print(help_text)
        input("Pressione Enter para continuar...")

    def play(self):
        """Loop principal do jogo"""
        print("🎮 Bem-vindo ao Mundo Wumpus!")
        print("Digite 'h' para ver os comandos.")
        input("Pressione Enter para começar...")

        while not self.game_over:
            self.display_world()

            command = input("Digite seu comando: ").lower().strip()

            if command == 'w':
                self.move_forward()
            elif command == 'a':
                self.turn_left()
            elif command == 'd':
                self.turn_right()
            elif command == 'g':
                self.grab_gold()
            elif command == 's':
                self.shoot_arrow()
            elif command == 'c':
                self.climb_out()
            elif command == 'h':
                self.get_help()
            elif command == 'm':
                print("\n=== MAPA COMPLETO (DEBUG) ===")
                temp = WumpusWorld()
                temp.world = self.world
                temp.player_pos = self.player_pos
                temp.player_direction = self.player_direction
                temp.score = self.score
                temp.has_arrow = self.has_arrow
                temp.has_gold = self.has_gold
                temp.display_world(show_all=True)
                input("Pressione Enter para continuar...")
            elif command == 'q':
                print("Saindo do jogo...")
                break
            else:
                print("Comando inválido! Digite 'h' para ver a ajuda.")
                input("Pressione Enter para continuar...")

        # Resultado final
        self.display_world(show_all=True)
        if self.victory:
            print("🎉 VITÓRIA! Você completou o jogo!")
        elif self.game_over:
            print("💀 GAME OVER!")

        print(f"Pontuação final: {self.score}")


# Função para iniciar o jogo
def main():
    """Função principal para iniciar o jogo"""
    while True:
        print("\n=== MUNDO WUMPUS ===")
        print("1. Novo Jogo (4x4)")
        print("2. Novo Jogo (5x5)")
        print("3. Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            game = WumpusWorld(4)
            game.play()
        elif choice == '2':
            game = WumpusWorld(5)
            game.play()
        elif choice == '3':
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()