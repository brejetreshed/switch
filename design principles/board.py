import random

def initialize_board(size):
    numbers = list(range(1, (size * size) + 1))  
    random.shuffle(numbers)  
    board = []
    
    for i in range(size):
        board.append(numbers[i * size:(i + 1) * size])
    
    return board

# Example usage
board = initialize_board(10)
for row in board:
    print(row)
