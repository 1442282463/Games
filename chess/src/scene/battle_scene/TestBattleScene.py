from BattleScene import BattleScene
from ui.battle.BattlePanel import BattlePanel
from ui.battle.BattleMapPanel import BattleMapPanel

class TestBattleScene(BattleScene):
    def __init__(self, Controller):
        super().__init__(Controller)
        self.ui = BattlePanel()

    def init_map(self):
        super().init_map()
        self.map = BattleMapPanel()
        