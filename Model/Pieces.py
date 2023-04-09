from Model.GameState import GameState

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
    
    def possible_moves(self):
        # return a list of possible moves for the piece (implemented in subclasses)
        pass
    
    def get_position(self):
        # return the position of the piece
        pass