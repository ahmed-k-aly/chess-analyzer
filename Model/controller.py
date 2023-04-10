from gameState import GameState

def get_game_board(game_state: GameState)->list[list[str]]:
    # returns a dict for what is on each squar
    squares = game_state.get_board().get_squares()
    # convert the squares to a list of strings
    board = [['' for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            if squares[i][j].piece:
                string = str(squares[i][j])
                board = string[0] + '_' + expand_piece_name(string[1])
            else:
                board[i][j] = ''
    return board

def expand_piece_name(piece_name: str)->str:
    # expand the piece name to the full name
    if piece_name == 'k':
        return 'king'
    elif piece_name == 'q':
        return 'queen'
    elif piece_name == 'r':
        return 'rook'
    elif piece_name == 'b':
        return 'bishop'
    elif piece_name == 'n':
        return 'knight'
    elif piece_name == 'p':
        return 'pawn'
    else:
        return ''