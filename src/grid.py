from easygui import enterbox
import pygame
import GOL

pygame.init()
pygame.font.init()

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (14,77,146)
GREY = (128,128,128)
WIDTH = 1000
HEIGHT = 1000


class Grid:
    """Frontend Class. Handles the plotting the backend data on screen.
    """
    def __init__(self, iGridN, iGridM, input_type):
        """Creates an instance of :class:`GOL.GameOfLife` and initialises it accordingly.

        Also generates a list of line coordinates to split the screen in N*M squares.

        Args:
            iGridN (integer): Grid N size
            iGridM (integer): Grid M size
            input_type (string): Input Source: Manual, Random and Csv
        """

        self.GridN = iGridN #: Class-wide copy of Grid N size 
        self.GridM = iGridM #: Class-wide copy of Grid M size
        self.input_type = input_type #: Class-wide copy of input_type Manual, Random and Csv
        
        self.game = GOL.GameOfLife(iGridN, iGridM)
        if(input_type == "Manual"): self.game.init_population(self.GridN, self.GridM)
        elif( input_type == "Random" ): self.game.rand_population(self.GridN, self.GridM)
        elif (input_type == "Csv"): 
            self.GridN, self.GridM = self.game.csv_population()

        
        self.h_interval = WIDTH/self.GridN #: Horizontal size of each square
        self.v_interval = HEIGHT/self.GridM #: Vertical size of each square
        self.grid_lines = []
        """Container for the Grid Lines Coordinates

        .. note::
            Pygame lines are drawn by giving two 2D points, hence grid_lines should come out as a MxNx2 Matrix.
        """
        
        for i in range(self.GridN):
            x_lines = [(0,self.v_interval+self.v_interval*i),(WIDTH, self.v_interval+self.v_interval*i)]
            self.grid_lines.append(x_lines)

        for i in range(self.GridM):
            y_lines = [(self.h_interval+self.h_interval*i, 0),(self.h_interval+self.h_interval*i, HEIGHT)]
            self.grid_lines.append(y_lines)

    def draw_lines(self, surface):
        """Iterates over :data:`~grid.Grid.grid_lines` and draws all lines.

        Args:
            surface (pygame Surface): Window surface to draw on.
        """
        for line in self.grid_lines:
            pygame.draw.line(surface, BLACK, line[0], line[1], 1)

    def fill_cell(self, x, y, surface):
        """Populates the specified Cell on the frontend and calls :func:`~GOL.GameOfLife.set_cell` to register the change.

        Args:
            x (integer): X Coordinate
            y (integer): X Coordinate
            surface (pygame Surface): Window surface to draw on.
        """
        rect = pygame.Rect(x*self.h_interval, y*self.v_interval, self.h_interval, self.v_interval)
        pygame.draw.rect(surface, BLACK, rect, 0)
        self.game.set_cell(x,y)

    def delete_cell(self,x,y,surface):
        """Opposite to :func:`~grid.Grid.fill_cell`

        Args:
            x (integer): X Coordinate
            y (integer): X Coordinate
            surface (pygame Surface): Window surface to draw on.
        """
        rect = rect = pygame.Rect(x*self.h_interval, y*self.v_interval, self.h_interval, self.v_interval)
        pygame.draw.rect(surface, WHITE, rect, 0)
        self.game.unset_cell(x,y)

    def draw_state(self,surface):
        """Iterates over every element of :data:`~GOL.GameOfLife.population` and draws them on screen accordingly.

        Args:
            surface (pygame Surface): Window surface to draw on.
        """
        for i in range(self.GridM):
            for j in range(self.GridN):
                if self.game.get_cell(i,j):
                    self.fill_cell(i,j,surface)
                else:
                    self.delete_cell(i,j,surface)

    def draw_NextState(self,surface):
        """Convenience function. Wraps :func:`~grid.Grid.draw_state` and :func:`~GOL.GameOfLife.eval_nextState` in one call.
        Hence, it evaluates the next state and then plots it.

        Args:
            surface (pygame Surface): Window surface to draw on.
        """
        self.game.eval_nextState()
        self.draw_state(surface)

    def reset_Board(self,surface):
        """Reset the board using the same :data:`~grid.Grid.input_type` as was given to the constructor. 

        Args:
            surface (pygame Surface): Window surface to draw on.
        """
        self.game.init_population(self.GridN, self.GridM)
        self.draw_state(surface)

        if(self.input_type == "Manual"): self.game.init_population(self.GridN, self.GridM)
        elif( self.input_type == "Random" ): self.game.rand_population(self.GridN, self.GridM)
        elif (self.input_type == "Csv"): 
            self.GridN, self.GridM = self.game.csv_population()

        self.draw_state(surface)

    def save_Board(self):
        box = enterbox("Enter the output file name", "Output File")
        filename = box + ".csv"
        file = open(filename, 'w')
        for i in range(self.GridM):
            row = self.game.get_row(i)
            for unit in range(self.GridN):
                if unit == (self.GridN - 1): string = str(int(row[unit])) + "\n"
                else: string = str(int(row[unit])) + ","
                file.write(string)
        file.close()                    