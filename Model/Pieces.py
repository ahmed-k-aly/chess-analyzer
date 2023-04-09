from Model.GameState import GameState

class Piece:
    # piece class
    def __init__(self, color: int, piece_type: str):
        self.color:int = color
        self.piece_type:str = piece_type
        self.is_taken = False
        self.position = None
        self.id = None # for pieces that have the same type and color (e.g. two white pawns)

    def get_color(self)->int:
        return self.color
    
    def get_piece_type(self)->str:
        return self.piece_type
    
    def get_piece_name(self)->str:
        return self.piece_type + '_' + self.color + '_' + self.id
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the piece (implemented in subclasses)
        pass
    
    def get_value(self):
        # return the value of the piece (implemented in subclasses)
        pass 
    
    def possible_moves(self):
        # return a list of all possible moves for the piece based on how it can move (implemented in subclasses)
        pass
    
    def get_position(self):
        # return the position of the piece
        pass
    
    def set_position(self, position):
        # set the position of the piece
        pass

    def __hash__(self) -> int: 
        # hash based on piece type, color, and position
        return hash((self.piece_type, self.color, self.position))
    
class Pawn(Piece):
    # pawn class
    def __init__(self, color: int, id: int):
        super().__init__(color, 'pawn')
        self.id = id
        self.has_moved = False
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the pawn
        pass
    
    def get_value(self):
        # return the value of the pawn
        return 1
    
    def possible_moves(self):
        # return a list of all possible moves for the pawn based on how it can move
        pass
    
    def get_position(self):
        # return the position of the pawn
        pass
    
    def set_position(self, position):
        # set the position of the pawn
        pass

class Knight(Piece):
    # knight class
    def __init__(self, color: int, id: int):
        super().__init__(color, 'knight')
        self.id = id
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the knight
        pass
    
    def get_value(self):
        # return the value of the knight
        return 3
    
    def possible_moves(self):
        # return a list of all possible moves for the knight based on how it can move
        pass
    
    def get_position(self):
        # return the position of the knight
        pass
    
    def set_position(self, position):
        # set the position of the knight
        pass

class Bishop(Piece):
    # bishop class
    def __init__(self, color: int, id: int):
        super().__init__(color, 'bishop')
        self.id = id
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the bishop
        pass
    
    def get_value(self):
        # return the value of the bishop
        return 3
    
    def possible_moves(self):
        # return a list of all possible moves for the bishop based on how it can move
        pass
    
    def get_position(self):
        # return the position of the bishop
        pass
    
    def set_position(self, position):
        # set the position of the bishop
        pass

class Rook(Piece):
    # rook class
    def __init__(self, color: int, id: int):
        super().__init__(color, 'rook')
        self.id = id
        self.has_moved = False
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the rook
        pass
    
    def get_value(self):
        # return the value of the rook
        return 5
    
    def possible_moves(self):
        # return a list of all possible moves for the rook based on how it can move
        pass
    
    def get_position(self):
        # return the position of the rook
        pass
    
    def set_position(self, position):
        # set the position of the rook
        pass

class Queen(Piece):
    # queen class
    def __init__(self, color: int, id: int):
        super().__init__(color, 'queen')
        self.id = id
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the queen
        pass
    
    def get_value(self):
        # return the value of the queen
        return 9
    
    def possible_moves(self):
        # return a list of all possible moves for the queen based on how it can move
        pass
    
    def get_position(self):
        # return the position of the queen
        pass
    
    def set_position(self, position):
        # set the position of the queen
        pass
    
class King(Piece):
    # king class
    def __init__(self, color: int, id: int):
        super().__init__(color, 'king')
        self.id = id
        self.has_moved = False
    
    def get_legal_moves(self, game_state: GameState):
        # return a list of legal moves for the king
        pass
    
    def get_value(self):
        # return the value of the king
        return float('inf')
    
    def possible_moves(self):
        # return a list of all possible moves for the king based on how it can move
        pass
    
    def get_position(self):
        # return the position of the king
        pass
    
    def set_position(self, position):
        # set the position of the king
        pass