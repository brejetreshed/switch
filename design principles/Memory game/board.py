import random
from card import Card

class Board:
    def __init__(self, size):
        """
        Initialize the board with shuffled cards.
        
        :param size: Total number of cards (must be even).
        """
        if size % 2 != 0:
            raise ValueError("Board size must be even.")

        self.size = size
        self.cards = [Card(i) for i in range(size // 2) for _ in range(2)]
        random.shuffle(self.cards)

    def display(self):
        """
        Display the current state of the board.
        """
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

    def flip_card(self, index):
        """
        Flip the card at the specified index.
        
        :param index: The index of the card to flip.
        :return: The flipped card.
        """
        if not (0 <= index < self.size):
            raise ValueError("Index out of range.")
        card = self.cards[index]
        card.flip()
        return card

    def is_match(self, index1, index2):
        """
        Check if the two specified cards match.
        
        :param index1: Index of the first card.
        :param index2: Index of the second card.
        :return: True if the cards match, False otherwise.
        """
        return self.cards[index1].value == self.cards[index2].value

class Game:
    def __init__(self, size):
        """
        Initialize the game with a board.
        
        :param size: Total number of cards on the board.
        """
        self.board = Board(size)
        self.turns = 0
        self.pairs_found = 0

    def play_turn(self, index1, index2):
        """
        Play a single turn by flipping two cards.
        
        :param index1: Index of the first card.
        :param index2: Index of the second card.
        :return: A message indicating the result of the turn.
        """
        if index1 == index2:
            return "Cannot select the same card twice."

        self.turns += 1
        self.board.flip_card(index1)
        self.board.flip_card(index2)

        self.board.display()

        if self.board.is_match(index1, index2):
            self.pairs_found += 1
            return "Match found!"
        else:
            # Flip cards back if they don't match
            self.board.flip_card(index1)
            self.board.flip_card(index2)
            return "No match. Try again."

    def is_game_over(self):
        """
        Check if all pairs have been found.
        
        :return: True if the game is over, False otherwise.
        """
        return self.pairs_found == self.board.size // 2
    

def main():
    try:
        board_size = int(input("Enter the size of the board: "))
        if board_size % 2 != 0:
            raise ValueError("Board size must be even.")

        game = Game(board_size)

        print("Game started! Match all pairs to win.")
        while not game.is_game_over():
            game.board.display()

            try:
                index1 = int(input("Enter the index of the first card: "))
                index2 = int(input("Enter the index of the second card: "))

                message = game.play_turn(index1, index2)
                print(message)
            except ValueError as e:
                print(f"Error: {e}")

        print(f"Congratulations!")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
