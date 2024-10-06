from pygame import Surface
from ui.BasePanel import BasePanel

class ZonePanel(BasePanel):
    def __init__(self, Parent: Surface = None):
        super().__init__(Parent)

    def init_ui(self):
        self.chess_list = []
    
    def refresh_ui(self):
        pass

    def destroy(self):
        pass