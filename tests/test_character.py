from unittest import TestCase
from levelup.character import Character, InvalidMoveException, DEFAULT_CHARACTER_NAME
from levelup.map import GameMap, Direction
from levelup.position import Position

class FakeGameMap(GameMap):
    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        return Position(4,4)


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_init(self):
        expected_name = DEFAULT_CHARACTER_NAME
        testobj = Character()
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_move(self):
        test_char = Character()
        test_char.position = Position(3,3)
        test_char.map = FakeGameMap()
        expected_position = Position(4,4)
        test_char.move('s')
        self.assertEqual(test_char.position, expected_position)
