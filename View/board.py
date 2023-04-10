'''creates a chess board with pieces on it based on the current state of the game board.
This is a class that is used by the view class to display the board and pieces on the screen.
'''
import pygame
import os
import sys
import time
import math
import json
import sys

class Board:
    def __init__(self, screen, layout):
        self.screen = screen
        self.layout = layout
        self.board_width = 600
        self.board_height = 600
        self.board_x = 200
        self.board_y = 50
        self.board_color = (255, 255, 255)
        self.board_outline_color = (200, 200, 200)
        self.board_outline_width = 5
        self.board_square_width = self.board_width / 8
        self.board_square_height = self.board_height / 8
        self.pieces = json.load(open('view/constants.json'))['pieces']
        self.pieces_path = json.load(open('view/constants.json'))['pieces_path']
        self.path_suffix = '1x.png'
        
    
    def draw_board(self):
        screen.fill('#1B0000')
        # function that draws the board
        # draw the board outline
        board_outline = (self.board_x-3, self.board_y-3, self.board_width+6, self.board_height+6)
        board_outline_rect = pygame.draw.rect(self.screen, self.board_outline_color, board_outline, self.board_outline_width)
        # fill rectangle with color
        board_rect = pygame.draw.rect(self.screen, self.board_color, (self.board_x, self.board_y, self.board_width, self.board_height))
        # draw the board squares
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    square_color = (255, 255, 255)
                else:
                    square_color = (0, 0, 0)
                square = (self.board_x + i * self.board_square_width, self.board_y + j * self.board_square_height, self.board_square_width, self.board_square_height)
                square_rect = pygame.draw.rect(self.screen, square_color, square)


    def draw_pieces(self):
        # function that draws the pieces
        # draw the pieces
        for j in range(8):
            for i in range(8):
                piece = self.layout[i][j]
                if piece == '':
                    continue
                full_piece_path = self.pieces_path + piece +'_' + self.path_suffix
                piece_image = pygame.image.load(full_piece_path)
                piece_image = pygame.transform.scale(piece_image, (int(self.board_square_width), int(self.board_square_height)))
                # draw the pieces on the 1st and 8th row
                self.screen.blit(piece_image, (self.board_x + (j) * self.board_square_width, self.board_y + i * self.board_square_height))

    def draw(self):
        while True:
            self.draw_board()
            self.draw_pieces()
            pygame.display.update()
            # shuffle layout list randomly to test
            self.layout = controller.get_game_board(None)
            # clear the pieces from the screen
            self.screen.fill('#1B0000')
            time.sleep(1/60)

 
# adding Model to the system path
sys.path.insert(0, 'C:\\Users\\nitro\\Documents\\Coding\\chess-analyzer')
from Model import controller
screen = pygame.display.set_mode((1000, 700))
layout = controller.get_game_board(None)
board = Board(screen, layout)
board.draw()