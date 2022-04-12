

class GameOfLife:
    #class members
    GridN = 0
    GridM = 0
    neighbours = [[]]
    population = [[]]


    def __init__(self, iGridN, iGridM):
        self.GridN = iGridN
        self.GridM = iGridM
        self.init_population(self.GridN, self.GridM)

    def init_population(self, GridN, GridM):
        self.population = [ False for i in range(GridM)]
        self.neighbours = [ False for i in range(GridM)]

        for i in range(GridM):
            temp_list = [False for i in range(GridN)]
            self.population[i] = temp_list
            self.neighbours[i] = [0 for i in range(GridN)]

        print("Grid is: ", len(self.neighbours[0]), len(self.neighbours))
