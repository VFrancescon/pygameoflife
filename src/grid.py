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
WIDTH = 720
HEIGHT = 720


class Grid:
    def __init__(self, iGridN, iGridM ):
        self.GridN = iGridN
        self.GridM = iGridM
        self.game = GOL.GameOfLife(iGridN, iGridM)
        self.h_interval = WIDTH/iGridN
        self.v_interval = HEIGHT/iGridM
        self.grid_lines = []

        for i in range(iGridN):
            x_lines = [(0,self.v_interval+self.v_interval*i),(WIDTH, self.v_interval+self.v_interval*i)]
            self.grid_lines.append(x_lines)

        for i in range(iGridM):
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
        rect = rect = pygame.Rect(x*self.h_interval+1, y*self.v_interval+1, self.h_interval-1, self.v_interval-1)
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