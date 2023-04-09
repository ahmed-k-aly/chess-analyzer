# chess game state class

class GameState:
    def __init__(self, board, PGN):
        self.board = board # board can be None or a list of pieces based on a PGN file
        self.turn = 'white'
        self.numTurns = 0
        self.isCheck = False
        self.isCheckmate = False
        self.isStalemate = False
        self.PGN_move_list = PGN # PGN file to initialize the board
    
    def init_board(self):
        # initialize the board to starting position
        self.board = []

        
        
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
    

class Piece:
    # piece class
    def __init__(self, color: int, piece_type: str):
        self.color:int = color
        self.piece_type:str = piece_type

    def get_color(self)->int:
        return self.color
    
    def get_piece_type(self)->str:
        return self.piece_type
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the piece (implemented in subclasses)
        pass
    
    def get_value(self):
        # return the value of the piece (implemented in subclasses)
        pass 
    
    def possible_moves(self, game_state: GameState):
        # return a list of possible moves for the piece (implemented in subclasses)
        pass
    
    def get_position(self):
        # return the position of the piece
        pass