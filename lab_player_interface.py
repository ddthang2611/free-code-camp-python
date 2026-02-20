from abc import ABC


class Player(ABC):
    def __init__(self):
        self.move = []
        self.position = (0, 0)
        self.path = []
