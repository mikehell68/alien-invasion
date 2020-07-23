import unittest
import ship
import settings
from unittest import mock

class Ship_UnitTests(unittest.TestCase):
    def setUp(self):
        settings = mock.MagicMock()
        screen = mock.MagicMock()
        self.ship = ship.Ship(ai_settings=settings, screen=screen)

    def test_Ship(self):
        self.assertIs(type(self.ship), ship.Ship)