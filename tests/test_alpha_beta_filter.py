import unittest
from src.alpha_beta_filter import AlphaBetaFilter


class TestAlphaBetaFilter(unittest.TestCase):
    def test_update_rejects_non_positive_dt(self):
        # Arrange
        position = (0, 0)
        velocity = (2, 1)
        dt = 0
        measurement = (3, 0.5)
        alpha = 0.8
        beta = 0.2

        ab_filter = AlphaBetaFilter(position, velocity, alpha, beta)

        # Act & Assert
        with self.assertRaises(ValueError):
            ab_filter.update(measurement, dt)

    def test_update_corrects_position_and_velocity(self):
        # Arrange
        position = (0, 0)
        velocity = (2, 1)
        dt = 1
        measurement = (3, 0.5)
        alpha = 0.8
        beta = 0.2

        ab_filter = AlphaBetaFilter(position, velocity, alpha, beta)

        # Act
        result = ab_filter.update(measurement, dt)

        # Assert
        self.assertEqual(result, ab_filter.position)
        self.assertAlmostEqual(result[0], 2.8)
        self.assertAlmostEqual(result[1], 0.6)
        self.assertAlmostEqual(ab_filter.velocity[0], 2.2)
        self.assertAlmostEqual(ab_filter.velocity[1], 0.9)

    def test_update_corrects_after_multiple_updates(self):
        # Arrange
        position = (0, 0)
        velocity = (2, 1)
        dt = 1
        measurement_1 = (3, 0.5)
        measurement_2 = (5.5, 1.0)
        alpha = 0.8
        beta = 0.2

        ab_filter = AlphaBetaFilter(position, velocity, alpha, beta)

        # Act
        ab_filter.update(measurement_1, dt)
        result = ab_filter.update(measurement_2, dt)

        # Assert
        self.assertEqual(result, ab_filter.position)
        self.assertAlmostEqual(result[0], 5.4)
        self.assertAlmostEqual(result[1], 1.1)
        self.assertAlmostEqual(ab_filter.velocity[0], 2.3)
        self.assertAlmostEqual(ab_filter.velocity[1], 0.8)