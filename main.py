# generate board
def board():
    board = {}
    letters = ['a','b','c','d','e','f','g','h']
    for letter in letters:
        num = 1
        while num < 9:
            position = f'{letter}' + f'{num}'
            board[position] = None
            num += 1
    return board

