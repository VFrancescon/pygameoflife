import random
import easygui as g
import csv
import sys

filedialog_title = "Choose a csv file"

class GameOfLife:
    """Backend class. Handles populating the Grid according to the given size and calculates the Next State of the board give the current one."""

    GridN = 0 #: Grid N size
    GridM = 0 #: Grid M size
    population = []
    """The Population member is a 2D (size NxM) array of True/False values.  
    Where True represents a Live cell and False represents a dead one.
    """
    neighbours = [] 
    """Similarly to Population, neighbours is a 2D (NxM) array containing the neighbour count for each of the respective Cells. 
    """

    def __init__(self, iGridN, iGridM):
        """Initialises size of a NxM Grid

        Args:
            iGridN (integer): Grid N size
            iGridM (integer): Grid M size
        """
        self.GridN = iGridN
        self.GridM = iGridM

    def rand_population(self, GridN, GridM):
        """Randomly populates the NxM Grid. 
        Random generation is handled by generating a random 1 bit number and casting it to bool.

        .. highlight::python
        .. code-block:: python

            rand_TrueFalseValue = bool(random.getrandbits(1))

        Args:
            GridN (integer): Grid N size
            GridM (integer): Grid M size
        """

        self.population = [ False for i in range(GridM)] 
        self.neighbours = [ False for i in range(GridM)]
        

        for i in range(GridM):
            temp_list = [ bool(random.getrandbits(1)) for i in range(GridN)]
            self.population[i] = temp_list
            self.neighbours[i] = [0 for i in range(GridN)]

    def init_population(self, GridN, GridM):
        """Initialises empty :data:`~GOL.GameOfLife.population` and :data:`~GOL.GameOfLife.neighbours` arrays
        in size NxM. 

        This method is used for purely manual entry.

        Args:
            GridN (integer): Grid N size
            GridM (integer): Grid M size
        """

        self.population = [ False for i in range(GridM)]
        
        self.neighbours = [ False for i in range(GridM)]

        for i in range(GridM):
            temp_list = [ False for i in range(GridN)]
            self.population[i] = temp_list
            self.neighbours[i] = [0 for i in range(GridN)]


    def csv_population(self):
        """Populates the Grid with input from a CSV file.
        
        Raises ValueError exceptions if the CSV contains invalid data.
        
        A few notes: 
        
        1. The CSV file must be formatted as follows
            0 corresponds to a dead cell
            
            1 corresponds to a live cell
            
            No title for rows or columns

        2. Grid sizes (:data:`~GOL.GameOfLife.GridN`, :data:`~GOL.GameOfLife.GridM`): 
            They are inferred from the CSV data. 
            Therefore whatever values may have been inputted from the command line (or given at boot-up otherwise)
            will be ignored.

        3. File path fetching is done through `easyGUI <https://pypi.org/project/easygui/>`_

        Returns:
            Integers: Size N and M inferred from the CSV data read. 

            
        """
        filename = g.fileopenbox(filedialog_title, filetypes=["*.csv"], )
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    int_list = list(map(int, row))
                except ValueError:
                    print("ERROR: Value", row, "cannot be cast to Int. Exiting now.")
                    sys.exit(0)
                bool_list = list(map(bool, int_list))
                self.population.append(bool_list)
                self.neighbours.append(int_list)
                
        self.GridN = len(self.population[0])
        self.GridM = len(self.population)
        csvfile.close()
        # self.eval_neighbours()

        # self.print_grid()

        return self.GridN, self.GridM

    def eval_neighbours(self):
        """Iterates through all of the cells in the Population array and counts the amount
        of alive cells immediately adjecent. The counted value is then written to the Neighbours array.
        """
        for i in range(self.GridM):
            for j in range(self.GridN):
                neighbour = 0
                for a in range(-1, 2, 1):
                    for b in range(-1, 2, 1):
                        x_in = i+b
                        y_in = j+a
                        if( a == 0 and b == 0): continue
                        if(x_in < 0 or x_in >= self.GridM): continue
                        if(y_in < 0 or y_in >= self.GridN): continue
                        if( self.population[x_in][y_in] ):
                            neighbour += 1
                # print(i,j)
                self.neighbours[i][j] = neighbour


    def eval_nextState(self):
        """Evaluates the next state of the board given the values in the neighbour array.

        Neighbour array is calculated from :func:`GOL.GameOfLife.eval_neighbours`.
        
        The logic used follows the standard Game of Life rules:
            1. Cells with less than 2 alive neighbors die by underpopulation
            2. Cells with more than 3 alive neighbors die by overpopulation
            3. Alive cells with exactly 2 alive neighbors stay alive
            4. Dead cells with exactly 3 alive neighbors are now alive
        """
        self.eval_neighbours()
        for i in range(self.GridM):
            for j in range(self.GridN):
                if(self.neighbours[i][j] < 2): self.population[i][j] = False
                if(self.neighbours[i][j] == 2) : continue
                if(self.neighbours[i][j] == 3) : self.population[i][j] = True
                if(self.neighbours[i][j] > 3) : self.population[i][j] = False

    def get_cell(self, x, y):
        """Helper function, gets the value held in cell at Coordinates x,y

        Args:
            x integer: X coordinate
            y integer: Y coordinate

        Returns:
            bool: True if cell is alive, False if it is dead
        """
        try:
            self.population[y][x]
        except:
            print("ERROR: Index out of Range. Check the CSV for incomplete rows")
            sys.exit(0)
        return self.population[y][x]

    def set_cell(self, x, y):
        """Helper function, sets the cell at Coordinates x,y to Alive

        Args:
            x integer: X coordinate
            y integer: Y coordinate
        """
        self.population[y][x] = True

    def unset_cell(self,x,y):
        """Helper function, sets the cell at Coordinates x,y to False

        Args:
            x integer: X coordinate
            y integer: Y coordinate
        """
        self.population[y][x] = False

    def get_row(self, y):
        """Helper function, gets the row at specified Y coordinate

        Args:
            y integer: Y coordinate

        Returns:
            List(bools): Row in the table at Y coordinate
        """
        return self.population[y]

    def print_grid(self):
        """Debug function. Prints grid to the terminal.
        """
        print("Population:")
        for i in range(self.GridM):
            print(self.population[i])

        
        print("Neighbors:")
        for i in range(self.GridM):
            print(self.neighbours[i])

        