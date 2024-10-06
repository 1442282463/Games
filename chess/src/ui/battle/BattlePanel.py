from pygame import Surface
from ui.battle.component.ScoreBoardPanel import ScoreBoardPanel
from ui.battle.component.ZonePanel import ZonePanel
from ui.BasePanel import BasePanel

class BattlePanel(BasePanel):
    def __init__(self, Parent: Surface = None):
        super().__init__(Parent)
        

    def init_ui(self):
        self.score_view = ScoreBoardPanel()
        self.zone_view = ZonePanel()
        self.opponent_zone_view = ZonePanel()

        self.synchronization_ui += [
            self.score_view,
            self.zone_view,
            self.opponent_zone_view
        ]
    
    def refresh_ui(self):
        super().refresh_ui()
    
    def destroy(self):
        super().destroy()
