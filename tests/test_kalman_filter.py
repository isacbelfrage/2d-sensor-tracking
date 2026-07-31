import unittest
import numpy as np
from src.kalman_filter import KalmanFilter


class TestKalmanFilter(unittest.TestCase):
    def test_initializes_state_and_covariance(self):
        # Arrange
        kalman_filter = KalmanFilter(1.0, 1.0 , 1.0, 1.0, 1.0)

        # Assert
        np.testing.assert_array_equal(kalman_filter.state, [1.0, 1.0])
        np.testing.assert_array_equal(kalman_filter.covariance, [[1.0, 0.0], [0.0, 1.0]])
        self.assertEqual(kalman_filter.acceleration_variance, 1.0)

    def test_predict_rejects_non_positive_dt(self):
        # Arrange
        kalman_filter = KalmanFilter(1.0, 1.0 , 1.0, 1.0, 1.0)
        dt = 0

        # Act & Assert
        with self.assertRaises(ValueError):
            kalman_filter.predict(dt)

    def test_predict(self):
        # Arrange
        kalman_filter = KalmanFilter(1.0, 1.0 , 1.0, 1.0, 1.0)
        dt = 1

        # Act
        kalman_filter.predict(dt)

        # Assert
        np.testing.assert_array_equal(kalman_filter.state, [2.0, 1.0])
        np.testing.assert_array_equal(kalman_filter.covariance, [[2.25, 1.5], [1.5, 2.0]])

    def test_update_rejects_negative_variance(self):
        # Arrange
        kalman_filter = KalmanFilter(1.0, 1.0 , 1.0, 1.0, 1.0)

        # Act & Assert
        with self.assertRaises(ValueError):
            kalman_filter.update(1.0, -1.0)

    def test_update(self):
        # Arrange
        kalman_filter = KalmanFilter(10.0, 2.0 , 4.0, 1.0, 0.0)

        # Act
        kalman_filter.predict(dt=1)
        kalman_filter.update(13.0, 1.0)

        # Assert
        np.testing.assert_allclose(kalman_filter.state, [77/6, 13/6])
        np.testing.assert_allclose(kalman_filter.covariance, [[5/6, 1/6], [1/6, 5/6]])

    def test_tracks_state_across_multiple_cycles(self):
        # Arrange
        kalman_filter = KalmanFilter(0.0, 1.0 , 1.0, 1.0, 0.0)

        # Act
        kalman_filter.predict(dt=1)
        kalman_filter.update(1.0, 1.0)
        kalman_filter.predict(dt=1.0)
        kalman_filter.update(3.5, 1.0)

        # Assert
        np.testing.assert_allclose(kalman_filter.state, [3, 3/2])
        np.testing.assert_allclose(kalman_filter.covariance, [[2/3, 1/3], [1/3, 1/3]])