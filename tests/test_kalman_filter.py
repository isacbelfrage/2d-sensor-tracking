import unittest
from src.kalman_filter import KalmanFilter


class TestKalmanFilter(unittest.TestCase):
    def test_initiation(self):
        # Arrange
        kalman_filter = KalmanFilter(1, 1 , 1, 1, 1)

        # Assert
        self.assertEqual(kalman_filter.state, [1, 1])
        self.assertEqual(kalman_filter.covariance, [[1, 0], [0, 1]])
        self.assertEqual(kalman_filter.acceleration_variance, 1)