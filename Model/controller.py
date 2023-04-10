from gameState import GameState

def get_game_board(game_state: GameState)->list[list[str]]:
    # returns a dict for what is on each squar
    squares = game_state.get_board().get_squares()
    # convert the squares to a list of strings
    board = [[str(square) for square in row] for row in squares]
    return board