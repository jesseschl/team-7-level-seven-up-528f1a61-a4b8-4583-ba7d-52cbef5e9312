from unittest import TestCase
from levelup.map import GameMap
from levelup.position import Position


class TestMap(TestCase):
    def test_init(self):
        testmap = GameMap()
        self.assertEqual(testmap.starting_position, Position(0,0))

    def test_is_valid_position_x(self):
        testmap = GameMap()
        self.assertTrue(testmap.is_valid_position(Position(4,5)))

    # def test_is_valid_position_y(self):
    #     testmap = GameMap()
    #     self.assertTrue(testmap.is_valid_position(Position(4,5)))
        
