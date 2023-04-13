from Model.gameState import GameState
import random
from Model.layout import Layout
from Model.utils import *
class Controller:
    def __init__(self, FEN =  "6k1/6p1/7p/3R3P/4QP2/1p2PK2/3r4/8 b - - 0 52" ):
        self.game_state = None
        self.FEN = FEN
    
    def create_game_state(self, PGN=None):
        # create a new game state
        self.game_state = GameState(PGN)
    
    def get_game_state(self):
        return self.game_state
    
    def get_next_move(self) -> str:
        # get the next move from the user/PGN/ai
        pass
    def get_next_game_state(self) -> GameState:
        # get the next game state
        move = self.get_next_move()
        self.game_state = self.game_state.get_next_state(move)
        return self.game_state
    
    def get_game_board_extended(self, game_state: GameState)->list[list[str]]:
        
        # returns a dict for what is on each squar
        if not game_state:
            # create a new game state
            self.game_state = GameState(None)
            
        squares = self.game_state.get_board().squares
        
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
    
    def convert_to_fen(self, game_state: GameState)->str:
        # convert the game state to a FEN string
        positions = game_state.get_board().convert_to_positions()
        return board_to_fen(positions)
    
    def convert_fen_to_game_state(self, FEN: str)-> list[list[str]]:
        # convert a FEN string to a game state
        board = fen_to_board(FEN)
        return board