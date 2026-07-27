import unittest
from src.visualization import split_positions

class TestVisualization(unittest.TestCase):
    def test_split_positions_separates_coordinates(self):
        # Arrange
        positions = [(1, 2), (2, 2), (2, 1)]

        # Act
        x_positions, y_positions = split_positions(positions)

        # Assert
        self.assertEqual(x_positions, [1, 2, 2])
        self.assertEqual(y_positions, [2, 2, 1])
