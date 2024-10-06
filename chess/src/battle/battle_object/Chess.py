import pygame
import Global

class Chess:
    def __init__(self) -> None:
        self.dt = config.DT

    def init_attr(self):
        self.pos = pygame.Vector2(0, 0)
        self.choose_flag = False    # 棋子选中状态
    
    # 选择棋子
    def choose(self):
        self.choose_flag = True
    
    # 取消棋子选中
    def cancel_choose(self):
        self.choose_flag = False
    
    # 移动棋子
    def move(self, pos):
        move_y = pos.y - self.pos.y
        move_x = pos.x - self.pos.x
        self.pos.x += move_x * self.dt
        self.pos.y += move_y * self.dt
        