import random

class Die:
    def __init__(self):
        random.seed(0)

    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_score(self, score):
        self.total_score += score

    def reset_score(self):
        self.total_score = 0


class PigGame:
    def __init__(self, player1, player2):
        self.die = Die()
        self.players = [Player(player1), Player(player2)]
        self.current_player = 0

    def switch_turn(self):
        self.current_player = 1 - self.current_player

    def play_turn(self):
        player = self.players[self.current_player]
        turn_total = 0

        print(f"{player.name}'s turn")
        while True:
            roll = self.die.roll()
            print(f"Rolled: {roll}")

            if roll == 1:
                print(f"{player.name} rolled a 1! No points added.")
                turn_total = 0
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}, Overall score: {player.total_score}")
                choice = input("Roll again (r) or Hold (h)? ").lower()
                if choice == 'h':
                    break

        player.add_score(turn_total)
        print(f"{player.name} ends turn with {player.total_score} points.\n")
        self.switch_turn()

    def play_game(self):
        while all(player.total_score < 100 for player in self.players):
            self.play_turn()

        winner = max(self.players, key=lambda p: p.total_score)
        print(f"{winner.name} wins with {winner.total_score} points!")


if __name__ == "__main__":
    game = PigGame("Player 1", "Player 2")
    game.play_game()
