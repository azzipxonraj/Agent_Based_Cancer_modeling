import pygame
import environment


def gui_window(rows, cols):
    pygame.init()
    cell_size = 5
    screen = pygame.display.set_mode((rows * cell_size, cols * cell_size))

    pygame.display.set_caption("Agent based tumor simulation")
    

