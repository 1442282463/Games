import pygame

class BasePanel:
    def __init__(self, Parent: pygame.Surface = None):
        self.parent = Parent
        self.layer = pygame.Surface(Parent.get_size())
        self.synchronization_ui = []    # 需要同步的ui
        # self.sublayer = []  #子图层

    def refresh_ui(self):
        for ui in self.synchronization_ui:
            ui.refresh_ui()
    
    def destroy(self):
        for ui in self.synchronization_ui:
            ui.destroy()
