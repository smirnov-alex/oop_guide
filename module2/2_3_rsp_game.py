from random import choice


class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        self.choice = input(f"{self.name}, choose rock, paper, lizard, spock or scissors: ").lower()


class Computer:
    def __init__(self):
        self.choice = None
        self.name = "Компьютер"

    def choose(self):
        elements = ['rock', 'scissors', 'paper', 'lizard', 'spock']
        self.choice = choice(elements)
        print(f'Компьютер выбрал {self.choice}')


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissors"],
        }

    def get_winner(self):
        if self.player1.choice == self.player2.choice:
            return None
        elif self.player2.choice in self.rules[self.player1.choice]:
            return self.player1
        else:
            return self.player2

    def play(self):
        self.player1.choose()
        self.player2.choose()
        winner = self.get_winner()
        if winner:
            print(f"{winner.name} победил!")
        else:
            print("У нас ничья.")


# Пример использования
player2 = Computer()
player1 = Player("Вика")
game = Game(player1, player2)
game.play()
