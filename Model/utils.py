# some utility functions
import random

def two_adjacent_letters(s: str):
    # returns two adjacent lowercase letters in a string if they exist else returns None
    for i in range(len(s)-1):
        if s[i].islower() and s[i+1].islower():
            return s[i:i+2]
    return None

def get_piece_type(s: str):
    # returns the piece type of a move
    if s[0].isupper():
        return s[0]
    else:
        return 'p'
    
def extra_information_in_move(s: str):
    # returns the extra information in a move
    # returns None if there is no extra information
    toReturn = ''
    if '+' in s:
        toReturn += '+'
    if '#' in s:
        toReturn += '#'
    if '=' in s:
        toReturn += '='
    if toReturn == '':
        return None
    
def board_to_fen(position):
    position = reversed(position)
    fen = ''
    for row in position:
        empty_squares = 0
        for square in row:
            if square:
                if empty_squares:
                    fen += str(empty_squares)
                    empty_squares = 0
                fen += square
            else:
                empty_squares += 1
        if empty_squares:
            fen += str(empty_squares)
        fen += '/'
    fen = fen[:-1]  # remove last '/'
    fen += ' w - - 0 1'  # add remaining FEN fields
    return fen



def expand_piece_name(piece_name: str)->str:
        # expand the piece name to the full name
        if piece_name == 'k':
            return 'king'
        elif piece_name == 'q':
            return 'queen'
        elif piece_name == 'r':
            return 'rook'
        elif piece_name == 'b':
            return 'bishop'
        elif piece_name == 'n':
            return 'knight'
        elif piece_name == 'p':
            return 'pawn'
        else:
            return ''
        
def shuffler(squares):
    # shuffle the board
    # for every piece on the board, move it to a random square
    # if the square is occupied, swap the pieces
    # this is a good way to test the game
    for i in range(8):
        for j in range(8):
            if squares[i][j].piece:
                # move the piece to a random square
                piece = squares[i][j].piece
                # get a random square
                random_i = random.randint(0, 7)
                random_j = random.randint(0, 7)
                # swap the pieces
                temp_piece = squares[random_i][random_j].piece
                squares[random_i][random_j].piece = piece
                squares[i][j].piece = temp_piece
    return squares