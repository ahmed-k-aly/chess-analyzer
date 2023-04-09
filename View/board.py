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
        self.board_color = (200, 200, 200)
        self.board_outline_color = (0, 0, 0)
        self.board_outline_width = 5
        self.board_square_width = self.board_width / 8
        self.board_square_height = self.board_height / 8
        self.board_square_color = (0, 0, 0)
        self.board_square_outline_color = (0, 0, 0)
        self.board_square_outline_width = 1
        self.pieces = json.load(open('view/constants.json'))['pieces']
        self.pieces_path = json.load(open('view/constants.json'))['pieces_path']
        
    def draw_board(self):
        self.board_rect = pygame.draw.rect(self.screen, self.board_color, (self.board_x, self.board_y, self.board_width, self.board_height))
        self.board_outline_rect = pygame.draw.rect(self.screen, self.board_outline_color, (self.board_x - self.board_outline_width, self.board_y - self.board_outline_width, self.board_width + self.board_outline_width * 2, self.board_height + self.board_outline_width * 2))
        self.board_squares = []
        for i in range(8):
            for j in range(8):
                self.board_squares.append(pygame.draw.rect(self.screen, self.board_square_color, (self.board_x + i * self.board_square_width, self.board_y + j * self.board_square_height, self.board_square_width, self.board_square_height)))
                self.board_squares.append(pygame.draw.rect(self.screen, self.board_square_outline_color, (self.board_x + i * self.board_square_width, self.board_y + j * self.board_square_height, self.board_square_width, self.board_square_height), self.board_square_outline_width))
    
    def draw_pieces(self):
        self.pieces_images = []
        for piece in self.board:
            self.pieces_images.append(pygame.image.load(os.path.join(self.pieces_path, self.pieces[piece])))
        for i in range(len(self.board)):
            self.screen.blit(self.pieces_images[i], (self.board_x + (i % 8) * self.board_square_width, self.board_y + math.floor(i / 8) * self.board_square_height)) 

    def draw(self):
        self.draw_board()
        self.draw_pieces()