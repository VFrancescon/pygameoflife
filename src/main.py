import GOL
import sys

GridN_ = 25
GridM_ = 25

def main(argv):
    if len(argv) == 3:   
        game = GOL.GameOfLife(int(argv[1]), int(argv[2]))
    else:
        game = GOL.GameOfLife(GridN_, GridM_)
    
    

if __name__ == "__main__":
    main(sys.argv)