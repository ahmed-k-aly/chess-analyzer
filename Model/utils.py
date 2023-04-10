# some utility functions

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
    
    