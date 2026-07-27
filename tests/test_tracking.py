import unittest
from src.tracking import calculate_mean_position, calculate_weighted_mean_position, calculate_position_error


class TestTracking(unittest.TestCase):
    def test_mean_position_rejects_empty_input(self):
        # Arrange
        empty_list = []

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_mean_position(empty_list)

    def test_mean_position_averages_coordinates(self):
        # Arrange
        same_positions = [(2, 2), (2, 2), (2, 2)]
        different_positions = [(1, 2), (2, 1), (0, 3)]

        # Act & Assert
        self.assertEqual(calculate_mean_position(same_positions), (2, 2))
        self.assertEqual(calculate_mean_position(different_positions), (1, 2))

    def test_weighted_mean_rejects_empty_input(self):
        # Arrange
        empty_list = []
        weights = []

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_weighted_mean_position(empty_list, weights)

    def test_weighted_mean_rejects_mismatched_lengths(self):
        # Arrange
        positions = [(1, 0), (2, 3)]
        weights = [1]

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_weighted_mean_position(positions, weights)

    def test_weighted_mean_rejects_zero_total_weight(self):
        # Arrange
        positions = [(1, 0), (2, 3)]
        weights = [0, 0]

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_weighted_mean_position(positions, weights)

    def test_weighted_mean_rejects_negative_weight(self):
        # Arrange
        positions = [(1, 0), (2, 3)]
        weights = [1, -3]

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_weighted_mean_position(positions, weights)

    def test_weighted_mean_applies_weights_to_coordinates(self):
        # Arrange
        positions = [(0, 5), (10, 10)]
        weights = [3, 1]

        # Act & Assert
        self.assertEqual(calculate_weighted_mean_position(positions, weights), (2.5, 6.25))

    def test_position_error_calculates_euclidean_distance(self):
        # Arrange
        position_1 = (0, 0)
        position_2 = (3, 4)

        # Act & Assert
        self.assertEqual(calculate_position_error(position_1, position_2), 5)
