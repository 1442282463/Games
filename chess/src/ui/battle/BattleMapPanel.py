from utils import PanelUtils
from ui.BasePanel import BasePanel
import pygame

class BattleMapPanel(BasePanel):
    def __init__(self, Parent: pygame.Surface = None):
        super().__init__(Parent)
        self.map_data_path = "TestMap.json"
        self.size = 0
    
    def init_data(self):
        self.data = PanelUtils.load_map_data(self.map_data_path)
        self.row = self.data["row"]
        self.col = self.data["col"]
        self.center = self.data["center"]
        self.spacing = self.data["spacing"]
    
    def init_map(self):
        width = self.col
        pygame.Rect(0, 0, self.col, self.row)