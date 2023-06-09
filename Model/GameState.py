# chess game state class
from Model.pieces import *
from Model.layout import Layout

class GameState:
    def __init__(self, PGN):
        self.turn = 'w'
        self.numTurns = 0
        self.isCheck = False
        self.isCheckmate = False
        self.isStalemate = False
        self.PGN_move_list = PGN # PGN file to initialize the board
        self.board = None
    
    
    def place_pieces(self):
        for i in range(8):
            self.board.get_square((1, i)).setPiece(Pawn('w', i))  #  set the second rank to w pawns
            self.board.get_square((6, i)).setPiece(Pawn('b', i))  #  set the seventh rank to b pawns
        # set rooks
        for i in range(2):
            self.board.get_square((0, i*7)).setPiece(Rook('w', i)) 
            self.board.get_square((7, i*7)).setPiece(Rook('b', i)) 
        # set knights
        for i in range(2):
            self.board.get_square((0, i*5+1)).setPiece(Knight('w', i))
            self.board.get_square((7, i*5+1)).setPiece(Knight('b', i))
        # set bishops
        for i in range(2): 
            self.board.get_square((0, i*3+2)).setPiece(Bishop('w', i)) 
            self.board.get_square((7, i*3+2)).setPiece(Bishop('b', i))
        # set queens
        for i in range(2):
            self.board.get_square((0, 3)).setPiece(Queen('w', i))
            self.board.get_square((7, 3)).setPiece(Queen('b', i))
        # set kings
        for i in range(2):
            self.board.get_square((0, 4)).setPiece(King('w', i))
            self.board.get_square((7, 4)).setPiece(King('b', i))
        
    def init_board(self):
        # put the Piece in the correct positions on the board 
        self.board = Layout()
        self.place_pieces()
        
    def get_next_state(self, move: str):
        # return the next state of the game based on the move
        legal = move in self.get_legal_moves()
        if not legal:
            raise Exception('Illegal move')
        # make the move
        self.make_move(move)
        # update the turn
        self.turn = 'b' if self.turn == 'w' else 'w'
        self.numTurns += 1
        # update the game state
        self.isCheck = self.board.is_check(self.turn)
        self.isCheckmate = self.board.is_checkmate(self.turn)
        self.isStalemate = self.board.is_stalemate(self.turn)
        return self


    def make_move(self, move: str):
        # make the move
        # get the piece type
        piece = move[0] if move[0].isupper() else 'p'
        # get the piece color
        color = self.turn
        isCapture = 'x' in move
        # get the destination square
        dest = move[-2:]


    def get_game_state(self):
        # return the current state of the game
        return self
        
    def get_legal_moves(self):
        # return a list of legal moves for the current player
        pass
    
    
    def get_turn(self):
        return self.turn
        
    
    def get_board(self):
        if self.board == None:
            self.init_board()
        return self.board