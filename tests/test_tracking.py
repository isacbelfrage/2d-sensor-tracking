import unittest
from src.tracking import *


class TestTracking(unittest.TestCase):
    def test_calculate_mean_position(self):
        # Arrange
        same_positions = [(2, 2), (2, 2), (2, 2)]
        different_positions = [(1, 2), (2, 1), (0, 3)]
        # Act & Assert
        self.assertEqual(calculate_mean_position(same_positions), (2, 2))
        self.assertEqual(calculate_mean_position(different_positions), (1, 2))

    def test_calculate_position_error(self):
        # Arrange
        position_1 = (0, 0)
        position_2 = (3, 4)

        # Act & Assert
        self.assertEqual(calculate_position_error(position_1, position_2), 5)