from game import GoldRush


def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    game = GoldRush(rows, cols)
    game.load_board()
    game.print()

    while not game.win:
        player = "player1"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print()
        if game._check_win(player):
            print(f"{player} wins!")
            break

        player = "player2"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print()
        if game._check_win(player):
            print(f"{player} wins!")
            break

if __name__ == "__main__":
    play_game()



    def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    game = GoldRush(rows, cols)
    game.load_board()
    game.print()
    player1 = 'player1'
    player2 = 'player2'
    while not game.win:
        if player_turn(game, player1):
            break
        if player_turn(game, player2):
            break
def player_turn(game , player):
    direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
    game.move_player(player, direction)
    game.print()
    if game._check_win(player):
        print(f"{player} wins!")
        return True
    return False
if __name__ == "__main__":
    play_game()

React

Reply

4:20
from Matrix import Matrix
import random
class GoldRush(Matrix):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.win = "" ##
        ##
        self.coins = 0
        self.player1 = 'player1'
        self.player2 = 'player2'
        self.coin = 'coin'
        self.empty_place = '.'
        self.wall = 'wall'
        ##
    ##
    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_element = self.coin if random.randint(0,1) == 0 else self.empty_place
                    self.matrix[i].append(rand_element)
                    if rand_element == self.coin:
                        self.coins += 1
                else:
                    self.matrix[i].append(self.wall)
            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_element = self.coin if random.randint(0,1) == 0 else self.empty_place
                self.matrix[i][k] = rand_element
                if rand_element == self.coin:
                    self.coins += 1
        self.matrix[0][0] = self.player1
        self.matrix[self.rows - 1][self.cols - 1] = self.player2
        min_coins = 10
        if self.coins < min_coins:
            return self.load_board()
        else:
            return self.matrix
#   name
    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"score{player_num}")
        winner_points = 100
        if score == winner_points:
            self.win = player
            return self.win
# ted
    def _other_player(self, player):
        if player == self.player1:
            return self.player2
        return self.player1
    #
    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col
        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return
        if self.matrix[new_row][new_col] not in [self.wall, other_player]:
            if self.matrix[new_row][new_col] == self.coin:
                self._score(player)
            self.matrix[curr_row][curr_col] = self.empty_place
            self.matrix[new_row][new_col] = player
        return self._check_win(player)
#
    def _move_down(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 1, 0)
    def _move_up(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, -1, 0)
    def _move_right(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, 1)
    def _move_left(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, -1)
    def move_player(self, player, direction):
        curr_row, curr_col = None, None
        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break
        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)
#
    def _score(self, player):
        player_num = player[-1],
        score_attr = f"score{player_num}"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))
from Matrix import Matrix
import random
class GoldRush(Matrix):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.win = "" ##
        ##
        self.coins = 0
        self.player1 = 'player1'
        self.player2 = 'player2'
        self.coin = 'coin'
        self.empty_place = '.'
        self.wall = 'wall'
        ##
    ##
    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_element = self.coin if random.randint(0,1) == 0 else self.empty_place
                    self.matrix[i].append(rand_element)
                    if rand_element == self.coin:
                        self.coins += 1
                else:
                    self.matrix[i].append(self.wall)
            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_element = self.coin if random.randint(0,1) == 0 else self.empty_place
                self.matrix[i][k] = rand_element
                if rand_element == self.coin:
                    self.coins += 1
        self.matrix[0][0] = self.player1
        self.matrix[self.rows - 1][self.cols - 1] = self.player2
        min_coins = 10
        if self.coins < min_coins:
            return self.load_board()
        else:
            return self.matrix
#   name
    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"score{player_num}")
        winner_points = 100
        if score == winner_points:
            self.win = player
            return self.win
# ted
    def _other_player(self, player):
        if player == self.player1:
            return self.player2
        return self.player1
    #
    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col
        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return
        if self.matrix[new_row][new_col] not in [self.wall, other_player]:
            if self.matrix[new_row][new_col] == self.coin:
                self._score(player)
            self.matrix[curr_row][curr_col] = self.empty_place
            self.matrix[new_row][new_col] = player
        return self._check_win(player)
#
    def _move_down(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 1, 0)
    def _move_up(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, -1, 0)
    def _move_right(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, 1)
    def _move_left(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, -1)
    def move_player(self, player, direction):
        curr_row, curr_col = None, None
        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break
        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)
#
    def _score(self, player):
        player_num = player[-1],
        score_attr = f"score{player_num}"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))