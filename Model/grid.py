# class for chess grid

class Grid:
    
    
    pass

class Square:
    
    def __init__(self):
        self.color = None
        self.piece = None
        self.highlighted = False
    
    def set_color(self, color):
        self.color = color
    
    def set_piece(self, piece: Piece):
        self.piece = piece
    
    def highlight(self):
        self.highlighted = True