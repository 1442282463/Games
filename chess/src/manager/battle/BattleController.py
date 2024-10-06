from data.battle_data.BattleData import BattleData
from user.BattleUser import BattleUser
from ui.battle.BattlePanel import BattlePanel
from ui.battle.BattleMapPanel import BattleMapPanel
import Global

class BattleController:
    def __init__(self, Scene):
        self.scene = Scene(self)
        self.data = BattleData()
        self.screen = Global.main_screen
    
    def init_role(self):
        self.player1 = BattleUser()
        self.player2 = BattleUser()
        self.data.player1 = self.player1
        self.data.player2 = self.player2
    
    def init_ui(self):
        self.battle_ui = BattlePanel(self.screen)
        self.battle_map_ui = BattleMapPanel(self.battle_ui)

    def update_data(self):
        pass