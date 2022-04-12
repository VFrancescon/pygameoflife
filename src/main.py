import GOL
import grid as gr
import sys
import os
import pygame
import easygui as g
pygame.init()
pygame.font.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'

GridN_ = 25
GridM_ = 25
WIDTH = 720
HEIGHT = 720

clear = lambda: os.system('clear')

filedialog_title = "Choose a csv file"

def main(argv):
    running = True
    l_click = False
    r_click = False
    
    
    if len(argv) == 3:   
        # game = GOL.GameOfLife(int(argv[1]), int(argv[2]))
        grid = gr.Grid(int(argv[1]), int(argv[2]))
        h_interval = WIDTH/int(argv[1])
        v_interval = HEIGHT/int(argv[2])
    else:
        # game = GOL.GameOfLife(GridN_, GridM_)
        grid = gr.Grid(GridN_, GridM_)
        h_interval = WIDTH/GridN_
        v_interval = HEIGHT/GridM_
        
    
    surface = pygame.display.set_mode((gr.WIDTH, gr.HEIGHT))
    pygame.display.set_caption("pyGame of Life")
    surface.fill((255,255,255))
    grid.draw_lines(surface)
    grid.draw_state(surface)
    
    while(running):
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o: inputk = 'o'
                elif event.key == pygame.K_n: inputk = 'n'
                if isinstance(inputk, str):
                    if(inputk == 'o'): filename = g.fileopenbox(filedialog_title, filetypes=["*.csv"], )
                    elif(inputk == 'n'): grid.draw_NextState(surface)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_click = int(pos[0] // h_interval)
                y_click = int(pos[1] // v_interval)
                if(pygame.mouse.get_pressed()[0]):    
                    # print("mouse press at: ", x_click, y_click)
                    grid.fill_cell(x_click,y_click, surface)
                if(pygame.mouse.get_pressed()[2]):    
                    # print("mouse press at: ", x_click, y_click)
                    grid.delete_cell(x_click,y_click, surface)
                

    # game.eval_neighbours()
    # game.print_grid()
    # game.eval_nextState()
    # game.print_grid()
    
    # usr_in = True
    
    # while(usr_in):
    #     input("Press enter to continue")
    #     game.eval_neighbours()
    #     game.print_grid()
    #     print(" at 1, 3: ", game.get_cell(1,3))
    #     game.eval_nextState()
    #     game.print_grid()
    #     print(" at 2, 1: ", game.get_cell(2,1))


if __name__ == "__main__":
    main(sys.argv)