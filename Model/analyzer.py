"""
 this takes in a chess position and move, and it analyzes how good that move is.
It does this by simulating the move and then analyzing the board state.
 It does this by using the chess engine stockfish. 
 It then returns the score of the move. This is the core of the analyzer. 
 It is a very important part of the project. It is also the most complex 
 part of the project. 
"""
from stockfish import Stockfish
class Analyzer:
    
    def __init__(self, depth=15, n_moves=5):
        self.stockfish = Stockfish("C://Users//nitro\Downloads\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe", depth=depth)
        self.depth = depth
        self.stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.n_moves = 5
        

    def analyze_move(self, fen_position, next_fen_position, is_white):
        # this function takes in a fen position and a pgn move and returns the score of the move
        if is_white == None:
            raise Exception("is_white is None")
        
        self.stockfish.is_fen_valid("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.stockfish.set_fen_position(fen_position)
        stockfish_score = self.stockfish.get_evaluation()['value']
        get_best_n_moves = self.stockfish.get_top_moves(5)
        
        # simulate the move in the stockfish engine
        self.stockfish.set_fen_position(next_fen_position)
        # get the score of the move
        stockfish_score_new = self.stockfish.get_evaluation()['value']

        # compare the scores
        if is_white:
            return stockfish_score_new - stockfish_score
        else:
            return stockfish_score - stockfish_score_new


