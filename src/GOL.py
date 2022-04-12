import random

class GameOfLife:
    #class members
    GridN = 0
    GridM = 0
    neighbours = [[]]
    population = [[]]


    def __init__(self, iGridN, iGridM):
        self.GridN = iGridN
        self.GridM = iGridM
        self.rand_population(self.GridN, self.GridM)

    def rand_population(self, GridN, GridM):

        self.population = [ False for i in range(GridM)]
        
        self.neighbours = [ False for i in range(GridM)]

        for i in range(GridM):
            temp_list = [ bool(random.getrandbits(1)) for i in range(GridN)]
            self.population[i] = temp_list
            self.neighbours[i] = [0 for i in range(GridN)]
        print("Grid is: ", len(self.neighbours[0]), "x",len(self.neighbours))

    def init_population(self, GridN, GridM):

        self.population = [ False for i in range(GridM)]
        
        self.neighbours = [ False for i in range(GridM)]

        for i in range(GridM):
            temp_list = [ False for i in range(GridN)]
            self.population[i] = temp_list
            self.neighbours[i] = [0 for i in range(GridN)]
        print("Grid is: ", len(self.neighbours[0]), "x",len(self.neighbours))


    def eval_neighbours(self):
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
                self.neighbours[i][j] = neighbour


    def eval_nextState(self):
        for i in range(self.GridM):
            for j in range(self.GridN):
                # if(self.neighbours[i][j] < 2): print("underpopulation at ", j, i)
                # if(self.neighbours[i][j] == 2) : print("Stay alive at ", j, i )
                # if(self.neighbours[i][j] == 3) : print("Born at ", j, i )
                # if(self.neighbours[i][j] > 3) : print("Overpopulation at ", j, i )
                if(self.neighbours[i][j] < 2): self.population[i][j] = False
                if(self.neighbours[i][j] == 2) : continue
                if(self.neighbours[i][j] == 3) : self.population[i][j] = True
                if(self.neighbours[i][j] > 3) : self.population[i][j] = False

    def get_cell(self, x, y):
        return self.population[y][x]

    def get_row(self, y):
        return self.population[y]

    def print_grid(self):
        print("Population:")
        for i in range(self.GridM):
            print(self.population[i])
        # print("Neighbours:")
        # for i in range(self.GridM):
        #     print(self.neighbours[i])
        