import unittest
from unittest.mock import call, patch
from src.sensor import PositionSensor


class TestPositionSensor(unittest.TestCase):
    def test_zero_noise_returns_exact_position(self):
        # Arrange
        sensor = PositionSensor(0)

        # Act
        measured_pos = sensor.measure(3.0, 4.0)

        # Assert
        self.assertEqual(measured_pos, (3.0, 4.0))

    def test_negative_noise_is_rejected(self):
        # Act & Assert 
        with self.assertRaises(ValueError):
            PositionSensor(-1)

    @patch("src.sensor.random.gauss")
    def test_noise_is_added_to_both_coordinates(self, mock_gauss):
        sensor = PositionSensor(2)
        mock_gauss.side_effect = [0.5, -0.25]
        measured_pos = sensor.measure(3.0, 4.0)
        self.assertEqual(measured_pos, (3.5, 3.75))
        self.assertEqual(mock_gauss.call_count, 2)
        calls = [call(0, 2), call(0, 2)]
        mock_gauss.assert_has_calls(calls)


if __name__ == "__main__":
    unittest.main()
