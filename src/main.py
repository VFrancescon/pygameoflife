from curses import KEY_BACKSPACE
import time
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
intro_msg = "Welcome to pyGame of Life. Commands are as follows:\n"
manual_msg = "o: Load a csv file\nn: Step to next state\nb: Toggle Autorun\nEsc: Quit the Program\nh: See this Prompt Again"


def introBox(msg, title=""):
    ret_val = g.msgbox(msg, title)
    if ret_val is None: # User closed msgbox
        sys.exit(0)

def inputSrcBox(msg):
    Title = "Startup Message"
    message = "Choose an input source:"
    option = ["Manual", "Random", "Csv"]
    while 1:
        selection = g.choicebox(intro_msg+manual_msg+message, Title, option)
        if( selection is None):
            return "Manual"
        else: return selection

def main(argv):
    running = True
    autoRun = False
    surface = pygame.display.set_mode((gr.WIDTH, gr.HEIGHT))
    pygame.display.set_caption("pyGame of Life")
    surface.fill((255,255,255))
    pygame.display.flip()
    time.sleep(1)
    input_method = inputSrcBox(intro_msg+manual_msg)
    
    if len(argv) == 3:   
        grid = gr.Grid(int(argv[1]), int(argv[2]), input_method)
    else:
        grid = gr.Grid(GridN_, GridM_, input_method)
        
    h_interval = grid.h_interval
    v_interval = grid.v_interval
    
    
    grid.draw_lines(surface)
    grid.draw_state(surface)
    
    while(running):
        grid.draw_lines(surface)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o: inputk = 'o'
                elif event.key == pygame.K_n: inputk = 'n'
                elif event.key == pygame.K_b: inputk = 'b'
                elif event.key == pygame.K_h: inputk = 'h'
                elif event.key == pygame.K_ESCAPE : inputk = 'esc'
                if isinstance(inputk, str):
                    if(inputk == 'o'): filename = g.fileopenbox(filedialog_title, filetypes=["*.csv"], )
                    elif(inputk == 'n'): grid.draw_NextState(surface)
                    elif(inputk == 'b') : autoRun = not autoRun
                    elif(inputk == 'h') : introBox(manual_msg, "Runtime Manual")
                    elif(inputk == 'esc') : running = False
                    else: continue
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

        if(autoRun):
            grid.draw_NextState(surface)
            time.sleep(0.5)
                

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