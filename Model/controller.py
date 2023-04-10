from Model.gameState import GameState
import random
def get_game_board(game_state: GameState)->list[list[str]]:
    # returns a dict for what is on each squar
    if not game_state:
        # create a new game state
        game_state = GameState(None)

    squares = game_state.get_board().get_squares()
    squares = shuffler(game_state)
    # convert the squares to a list of strings
    board = [['']*8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            if squares[i][j].piece:
                string = str(squares[i][j])
                board[i][j] = string[0] + '_' + expand_piece_name(string[1])
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
    
def shuffler(game_state: GameState):
    # shuffle the board
    # for every piece on the board, move it to a random square
    # if the square is occupied, swap the pieces
    # this is a good way to test the game
    squares = game_state.get_board().get_squares()
    for i in range(8):
        for j in range(8):
            if squares[i][j].piece:
                # move the piece to a random square
                piece = squares[i][j].piece
                # get a random square
                random_i = random.randint(0, 7)
                random_j = random.randint(0, 7)
                # swap the pieces
                temp_piece = squares[random_i][random_j].piece
                squares[random_i][random_j].piece = piece
                squares[i][j].piece = temp_piece
    return squares