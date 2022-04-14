import pygame
import os
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
    def __init__(self, iGridN, iGridM, input_type):
        self.GridN = iGridN
        self.GridM = iGridM
        
        self.game = GOL.GameOfLife(iGridN, iGridM)
        if(input_type == "Manual"): self.game.init_population(self.GridN, self.GridM)
        elif( input_type == "Random" ): self.game.rand_population(self.GridN, self.GridM)
        elif (input_type == "Csv"): 
            self.GridN, self.GridM = self.game.csv_population()

        
        self.h_interval = WIDTH/self.GridN
        self.v_interval = HEIGHT/self.GridM
        self.grid_lines = []
        
        for i in range(self.GridN):
            x_lines = [(0,self.v_interval+self.v_interval*i),(WIDTH, self.v_interval+self.v_interval*i)]
            self.grid_lines.append(x_lines)

        for i in range(self.GridM):
            y_lines = [(self.h_interval+self.h_interval*i, 0),(self.h_interval+self.h_interval*i, HEIGHT)]
            self.grid_lines.append(y_lines)

        
        
        # print("Grid lines: ", self.grid_lines)

    def draw_lines(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, BLACK, line[0], line[1], 1)

    def fill_cell(self, x, y, surface):
        rect = pygame.Rect(x*self.h_interval, y*self.v_interval, self.h_interval, self.v_interval)
        # print("coordinates: ", x*self.h_interval, y*self.v_interval, self.h_interval, self.v_interval)
        pygame.draw.rect(surface, BLACK, rect, 0)
        self.game.set_cell(x,y)

    def delete_cell(self,x,y,surface):
        rect = rect = pygame.Rect(x*self.h_interval, y*self.v_interval, self.h_interval, self.v_interval)
        pygame.draw.rect(surface, WHITE, rect, 0)

    def draw_state(self,surface):
        for i in range(self.GridM):
            for j in range(self.GridN):
                if self.game.get_cell(i,j):
                    self.fill_cell(i,j,surface)
                else:
                    self.delete_cell(i,j,surface)

    def draw_NextState(self,surface):
        self.game.eval_nextState()
        self.draw_state(surface)