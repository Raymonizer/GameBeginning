from ppb import BaseScene
from ppb import GameEngine

with GameEngine(BaseScene) as engine:
    engine.run()
