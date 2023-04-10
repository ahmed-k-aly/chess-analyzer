# class for chess grid
from Model.pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King
class Layout:
    def __init__(self):
        self.squares = [[i]*8 for i in range(8)]
        self.setup_board()

    def setup_board(self):
        # setup the board with the correct colors
        # and pieces in the correct positions
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.squares[i][j] = Square('white', (i, j))
                else:
                    self.squares[i][j] = Square('black', (i, j))
                    
                    
    def get_square(self, position):
        # return the square at the given position. Constant Time
        return self.squares[position[0]][position[1]]

    def get_squares(self):
        # return all the squares on the board
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
                board += str(self.squares[i][j]) + ' '
        return board

    def pretty_print(self):
        # print the board in a more readable format in ASCII chess
        # print bounds
        print('  a   b   c   d   e   f   g   h  ')
        for i in range(8):
            print(i+1, end=' ')
            for j in range(8):
                print(self.squares[i][j], end=' ')
            print('')
        print('  a   b   c   d   e   f   g   h  ')
    
    def convert_to_positions(self):
        # output the board as a list of piece strings based on their position
        # used for the neural network
        board = [['']*8 for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.squares[i][j].piece:
                    string = str(self.squares[i][j])
                    board[i][j] = (string[1]).upper() if string[0] == 'w' else (string[1]).lower()
                else:
                    board[i][j] = ''
        return board
    
    def convert_to_squares(self, positions):
        # convert a list of piece strings to a board
        # used for the neural network
        piecesDict = {  'p': Pawn(None, None),
                        'r': Rook(None, None),
                        'n': Knight(None, None),
                        'b': Bishop(None, None),
                        'q': Queen(None, None),
                        'k': King(None, None)
}
        for i in range(8):
            for j in range(8):
                if positions[i][j]:
                    color = 'w' if positions[i][j].isupper() else 'b'
                    piece = piecesDict[positions[i][j].lower()]
                    piece.color = color
                    self.squares[i][j].setPiece(piece)
                else:
                    self.squares[i][j].removePiece()

class Square:
    
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.highlighted = False
        self.piece = None
        self.isEmpty = True
    
    
    def setPiece(self, piece: Piece):
        self.piece = piece
        self.isEmpty = False
    
    def removePiece(self):
        self.piece = None
        self.isEmpty = True
    
    def swapPiece(self, piece: Piece):
        self.piece = piece
    
    def swapSquarePiece(self, square):
        self.piece, square.piece = square.piece, self.piece
    
    def highlight(self):
        self.highlighted = True
        
    def unhighlight(self):
        self.highlighted = False
    
    def getColor(self):
        return self.color

    def getPosition(self):
        return self.position
    
    def __str__(self):
        return str(self.piece) if self.piece else ''