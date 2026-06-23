import pygame
import environment

def init_gui(width=500, height=500):
    pygame.init()
    pygame.display.set_caption("Agent based tumor simulation")
    screen = pygame.display.set_mode((width, height))
    return screen


def gui_window(screen, grid_t, rows, cols):

    grid_surface = pygame.Surface((cols, rows))
    for row_idx, row in enumerate(grid_t):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                grid_surface.set_at((col_idx, row_idx), (222, 49, 99))
            elif cell == 2:
                grid_surface.set_at((col_idx, row_idx), (129, 19, 49))
            elif cell == 0:
                grid_surface.set_at((col_idx, row_idx), (103, 49, 71))

    frame = pygame.transform.scale(grid_surface, (500, 500))
    screen.blit(frame, frame.get_rect(center=(250, 250)))

def game_loop(rows, cols):
    screen = init_gui()
    grid = environment.create_grid(rows, cols)
    grid_t = environment.place_tumor(grid, rows, cols)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid_t = environment.do_single_time_step(grid_t)

        gui_window(screen, grid_t, rows, cols)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()