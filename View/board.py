'''creates a chess board with pieces on it based on the current state of the game board.
This is a class that is used by the view class to display the board and pieces on the screen.
'''
import pygame
import os
import sys
import time
import math
import json
class Board:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
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
        for i in range(8):
            for j in range(8):
                piece_image = pygame.image.load(self.pieces_path + 'w_king_1x.png')
                piece_image = pygame.transform.scale(piece_image, (int(self.board_square_width), int(self.board_square_height)))
                self.screen.blit(piece_image, (self.board_x + i * self.board_square_width, self.board_y + j * self.board_square_height))

        
        
        
    def draw(self):
        while True:
            self.draw_board()
            self.draw_pieces()
            pygame.display.update()

screen = pygame.display.set_mode((1000, 700))
board = Board(screen, None)
board.draw()