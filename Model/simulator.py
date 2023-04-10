import time
import chess.pgn
import sys
sys.path.insert(0, 'C:\\Users\\nitro\\Documents\\Coding\\chess-analyzer')
import pygame
from Model.controller import Controller
from View.board import Board
from Model.layout import Layout, Square
# Load PGN file

# adding Model to the system path
controller = Controller()
screen = pygame.display.set_mode((1000, 700))
layout = controller.get_game_board_extended(None)
UIboard = Board(screen, layout)



with open('Model/game') as f:
    game = chess.pgn.read_game(f)

# Access moves from the game
board = game.board()
for move in game.mainline_moves():
    board.push(move)

    fen = board.fen()
    print(fen)
    positions = controller.convert_fen_to_game_state(fen)
    print(positions)
    layout = Layout()
    layout.convert_to_squares(positions)
    controller.game_state.board = layout
    UIboard.layout = controller.get_game_board_extended(controller.game_state)
    # we draw the board here
    UIboard.draw_board()
    UIboard.draw_pieces()
    pygame.display.update()
    # clear the pieces from the screen
    UIboard.screen.fill('#1B0000')
    time.sleep(1/15)

while True:
    # keep displaying the last position
    UIboard.draw_board()
    UIboard.draw_pieces()
    pygame.display.update()
    
    



# # Access FEN notation of current position
# fen = board.fen()
# print(fen)