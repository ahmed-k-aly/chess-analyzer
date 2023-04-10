import chess.pgn
# Load PGN file
with open('Model/game') as f:
    game = chess.pgn.read_game(f)

# Access moves from the game
board = game.board()
for move in game.mainline_moves():
    board.push(move)

# Access FEN notation of current position
fen = board.fen()
print(fen)