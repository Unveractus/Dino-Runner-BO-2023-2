from dino_runner.components.coins.coin import Coin
from dino_runner.utils.constants import COIN


class GoldCoin (Coin):
    def __init__(self):
        self.image = COIN
        super() .__init__(self.image)