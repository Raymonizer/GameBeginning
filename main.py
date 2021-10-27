from ppb import GameEngine, BaseScene

class Game(BaseScene):

    def __init__(self, engine, background_color=(0, 0, 0), **kwargs):
        super().__init__(engine=engine, 
                         background_color=background_color,
                         **kwargs)
