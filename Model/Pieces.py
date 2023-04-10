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
    
    
    def __str__(self):
        return str(self.color) + self.piece_type
    
    def get_value(self):
        # return the value of the piece (implemented in subclasses)
        pass 
    
    def possible_moves(self, pos: tuple):
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
        super().__init__(color, 'p')
        self.id = id
        self.has_moved = False
    
    
    def get_value(self):
        # return the value of the pawn
        return 1
    
    def possible_moves(self, pos: tuple):
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
        super().__init__(color, 'n')
        self.id = id
    
    def get_value(self):
        # return the value of the knight
        return 3
    
    def possible_moves(self, pos: tuple):
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
        super().__init__(color, 'b')
        self.id = id
    
    def get_value(self):
        # return the value of the bishop
        return 3
    
    def possible_moves(self, pos: tuple):
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
        super().__init__(color, 'r')
        self.id = id
        self.has_moved = False
    
    def get_value(self):
        # return the value of the rook
        return 5

    def possible_moves(self, pos: tuple):
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
        super().__init__(color, 'q')
        self.id = id

    
    def get_value(self):
        # return the value of the queen
        return 9
    
    def possible_moves(self, pos: tuple):
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
        super().__init__(color, 'k')
        self.id = id
        self.has_moved = False
    
    def get_value(self):
        # return the value of the king
        return float('inf')
    
    def possible_moves(self, pos: tuple):
        # return a list of all possible moves for the king based on how it can move
        pass
    
    def get_position(self):
        # return the position of the king
        pass
    
    def set_position(self, position):
        # set the position of the king
        pass

# Path: Model\GameState.py