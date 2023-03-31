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

    def test_is_valid_position_y(self):
        testmap = GameMap()
        self.assertTrue(testmap.is_valid_position(Position(4,5)))
        
    def test_is_invalid_position_x(self):
        testmap = GameMap()
        self.assertFalse(testmap.is_valid_position(Position(10,5)))

    def test_is_invalid_position_y(self):
        testmap = GameMap()
        self.assertFalse(testmap.is_valid_position(Position(4,10)))

    def test_calculate_position_NORTH(self):
        testmap = GameMap()
        test_pos = Position(7,2)
        expected_position = Position(7,1)
        self.assertTrue(testmap.calculate_position(test_pos, "n"), expected_position)

    def test_calculate_position_SOUTH(self):
        testmap = GameMap()
        test_pos = Position(7,2)
        expected_position = Position(7,3)
        self.assertTrue(testmap.calculate_position(test_pos, "s"), expected_position)

    def test_calculate_position_EAST(self):
        testmap = GameMap()
        test_pos = Position(7,2)
        expected_position = Position(8,2)
        self.assertTrue(testmap.calculate_position(test_pos, "e"), expected_position)
        
    def test_calculate_position_WEST(self):
        testmap = GameMap()
        test_pos = Position(7,2)
        expected_position = Position(6,2)
        self.assertTrue(testmap.calculate_position(test_pos, "w"), expected_position)

