from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.controller import GameController, CharacterNotFoundException
from levelup.character import DEFAULT_CHARACTER_NAME, InvalidMoveException, Character
from levelup.map import Direction
from levelup.position import Position

class FakeCharacter(Character):
    name: str

    def __init__(self, name = DEFAULT_CHARACTER_NAME):
        self.name = name

class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            None,
        )

    def test_create_character(self):
        testobj = GameController()
        test_char = FakeCharacter("arbitrary")
        testobj.create_character("arbitrary")
        self.assertEqual(testobj.character.name, test_char.name)
