# chess game state class
import Model.Pieces as Pieces
import Model.layout as Layout
class GameState:
    def __init__(self, PGN):
        self.turn = 'white'
        self.numTurns = 0
        self.isCheck = False
        self.isCheckmate = False
        self.isStalemate = False
        self.PGN_move_list = PGN # PGN file to initialize the board
        self.board = Layout.Layout()
    
    
    def place_pieces(self):
        for i in range(8):
            self.board.get_square((1, i)).setPiece(Pieces.Pawn('white', i))  #  set the second rank to white pawns
            self.board.get_square((6, i)).setPiece(Pieces.Pawn('black', i))  #  set the seventh rank to black pawns
        # set rooks
        for i in range(2):
            self.board.get_square((0, i*7)).setPiece(Pieces.Rook('white', i)) 
            self.board.get_square((7, i*7)).setPiece(Pieces.Rook('black', i)) 
        # set knights
        for i in range(2):
            self.board.get_square((0, i*5+1)).setPiece(Pieces.Knight('white', i))
            self.board.get_square((7, i*5+1)).setPiece(Pieces.Knight('black', i))
        # set bishops
        for i in range(2): 
            self.board.get_square((0, i*3+2)).setPiece(Pieces.Bishop('white', i)) 
            self.board.get_square((7, i*3+2)).setPiece(Pieces.Bishop('black', i))
        # set queens
        for i in range(2):
            self.board.get_square((0, 3)).setPiece(Pieces.Queen('white', i))
            self.board.get_square((7, 3)).setPiece(Pieces.Queen('black', i))
        # set kings
        for i in range(2):
            self.board.get_square((0, 4)).setPiece(Pieces.King('white', i))
            self.board.get_square((7, 4)).setPiece(Pieces.King('black', i))
        
    def init_board(self):
        # put the pieces in the correct positions on the board 
        self.place_pieces()
        
    def get_next_state(self, move):
        # return the next state of the game based on the move
        pass
    
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
    

