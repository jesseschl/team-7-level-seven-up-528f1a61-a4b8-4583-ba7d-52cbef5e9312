from unittest import TestCase
from levelup.character import Character, InvalidMoveException, DEFAULT_CHARACTER_NAME
from levelup.map import GameMap, Direction
from levelup.position import Position


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
