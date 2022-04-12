import GOL
import sys
import os

GridN_ = 25
GridM_ = 25

clear = lambda: os.system('clear')

def main(argv):
    if len(argv) == 3:   
        game = GOL.GameOfLife(int(argv[1]), int(argv[2]))
    else:
        game = GOL.GameOfLife(GridN_, GridM_)
    
    # game.eval_neighbours()
    # game.print_grid()
    # game.eval_nextState()
    # game.print_grid()
    
    usr_in = True
    
    while(usr_in):
        input("Press enter to continue")
        game.eval_neighbours()
        game.print_grid()
        print(" at 1, 3: ", game.get_cell(1,3))
        game.eval_nextState()
        game.print_grid()
        print(" at 2, 1: ", game.get_cell(2,1))


if __name__ == "__main__":
    main(sys.argv)