"""
class that handles the view of the game and displays the board and pieces on the screen 
based on the current state of the game board. As well as other things like the menu and
analytics. It's basically the master view that handles all the display.
""" 
import sys
import pygame
from board import Board
# from menu import Menu
# from analytics import Analytics
# from game import Game



class View:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.board_view = Board(self.screen, self.board)
        # self.menu_view = Menu(self.screen)
        # self.analytics_view = Analytics(self.screen)
        # self.game_view = Game(self.screen)
        self.screen_width = 1000
        self.screen_height = 700
        self.screen_color = (255, 255, 255)
        self.screen_outline_color = (0, 0, 0)
        self.screen_outline_width = 5
        self.screen_outline = (self.screen_outline_width, self.screen_outline_width, self.screen_width - self.screen_outline_width, self.screen_height - self.screen_outline_width)
        self.screen_outline_rect = pygame.draw.rect(self.screen, self.screen_outline_color, self.screen_outline)
        self.screen_rect = pygame.draw.rect(self.screen, self.screen_color, (0, 0, self.screen_width, self.screen_height))

    def draw(self):
        self.screen.fill(self.screen_color)
        self.screen_rect = pygame.draw.rect(self.screen, self.screen_color, (0, 0, self.screen_width, self.screen_height))
        self.screen_outline_rect = pygame.draw.rect(self.screen, self.screen_outline_color, self.screen_outline)
        self.board_view.draw()
        # self.menu_view.draw()
        # self.analytics_view.draw()
        # self.game_view.draw()


# display the board and pieces on the screen
def display_board():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Chess')
    board = ['white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'black_knight', 'black_rook', 'black_pawn', 'black_king', 'black_queen', 'black_bishop']
    view = View(screen, board)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        view.draw()
        pygame.display.update()
        
display_board()