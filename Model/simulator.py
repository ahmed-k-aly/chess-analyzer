import time
import chess.pgn
import sys
sys.path.insert(0, 'C:\\Users\\nitro\\Documents\\Coding\\chess-analyzer')
import pygame
from Model.controller import Controller
from View.board import Board
from Model.layout import Layout, Square
# Load PGN file


# ENTRY POINT FILE

# CONSTANTS
FPS = 60

#TODO: ADD THIS TO THE CONTROLLER. ENSURE THAT THE CONTROLLER IS ABLE TO HANDLE THE GAME STATE. NAME THINGS ACCORDINGLY
#TODO: DECOMPOSE THE GAME INTO A DIFFERERNT FILE AND ONLY EXPORT MOVES. THIS FILE JUST GETS A BOARD FROM MODEL AND CALLS THE VIEW TO DRAW IT.

# adding Model to the system path


def go():
    # start the game
    init_game()
    turn = 0
    for move in game.mainline_moves():
        # simulate the game

        # get the next move [CORE OF THE SIMULATOR]
        simulate_move(move)
        turn+=1
        render_board()
        # get the next move
        if not move:
            break
    # display the final position
    while True:
        render_board()





def init_game():
    # initalizing everything
    global controller 
    global screen
    global layout
    global UIboard
    global game # the read game from the pgn file
    global board # the board from the chess.pgn module
    controller = Controller()
    screen = pygame.display.set_mode((1000, 700))
    layout = controller.get_game_board_extended(None)
    UIboard = Board(screen, layout)
  
    with open('Model/game') as f:
        game = chess.pgn.read_game(f)
    # Access moves from the game
    board = game.board()


def simulate_move(move: chess) -> Layout:
    # simulates a move, where the move is in PGN notation and returns the new board state
    board.push(move)
    fen = board.fen()
    positions = controller.convert_fen_to_game_state(fen)
    # get the layout from the game state
    layout: Layout = controller.game_state.board
    layout.convert_to_squares(positions) # simulates the move in the layout
    UIboard.layout = controller.get_game_board_extended(controller.game_state)


def render_board():
    # we draw the board here
    UIboard.draw_board()
    UIboard.draw_pieces()
    pygame.display.update()
    # clear the pieces from the screen
    UIboard.screen.fill('#1B0000')
    time.sleep(1/FPS)

# # Access FEN notation of current position
# fen = board.fen()
# print(fen)

if __name__ == '__main__':
    go()
