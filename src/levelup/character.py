from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_CHARACTER_NAME = "Character"


class InvalidMoveException(Exception):
    pass


class Character:
    name: str
    map: GameMap = None
    position: Position = None

    def __init__(self, name = DEFAULT_CHARACTER_NAME):
        self.name = name

    def enter_map(self, game_map: GameMap):
        pass

    def move(self, direction: Direction):
        self.position = self.map.calculate_position(self.position, direction)
        
