from pygame import Surface
from ui.BasePanel import BasePanel

class ScoreBoardPanel(BasePanel):
    def __init__(self, Parent: Surface = None):
        super().__init__(Parent)

    def init_ui(self):
        self.palyer_name_1 = None
        self.palyer_name_2 = None
        self.icon1 = None
        self.icon2 = None
    
    def refresh_ui(self):
        pass

    def destroy(self):
        pass