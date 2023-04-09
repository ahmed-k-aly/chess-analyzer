# class for chess grid
from Model.Pieces import Piece
class Layout:
    def __init__(self):
        self.squares = []
        self.setup_board()

    def setup_board(self):
        # setup the board with the correct colors
        # and pieces in the correct positions
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.squares.append(Square('white', (i, j)))
                else:
                    self.squares.append(Square('black', (i, j)))
                    
                    
    def get_square(self, position):
        # return the square at the given position
        for square in self.squares:
            if square.get_position() == position:
                return square
        return None

    def get_squares(self):
        return self.squares
    
    
    def get_squares_with_piece(self):
        squares = []
        for square in self.squares:
            if square.piece:
                squares.append(square)
        return squares
    
    
    def get_squares_with_piece_of_color(self, color):
        squares = []
        for square in self.squares:
            if square.piece and square.piece.color == color:
                squares.append(square)
        return squares

    def __str__(self):
        # print the board
        board = ''
        for i in range(8):
            for j in range(8):
                if self.get_square((i, j)).piece:
                    board += self.get_square((i, j)).piece.get_piece_type()[0]
                else:
                    board += ' '
            board += ','
        return board

class Square:
    
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.highlighted = False
        self.piece = None
        self.isEmpty = True
    
    
    def set_piece(self, piece: Piece):
        self.piece = piece
        self.isEmpty = False
    
    def highlight(self):
        self.highlighted = True
        
    def unhighlight(self):
        self.highlighted = False
    
    def get_color(self):
        return self.color

    def get_position(self):
        return self.position