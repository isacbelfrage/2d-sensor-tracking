import unittest
from src.model import MovingObject

class TestMovingObject(unittest.TestCase):
    def test_update_changes_position(self):
        # Arrange
        obj = MovingObject(0.0, 0.0, 2.0, 1.0)

        # Act
        obj.update(0.5)

        # Assert
        self.assertAlmostEqual(obj.x, 1.0)
        self.assertAlmostEqual(obj.y, 0.5)

if __name__ == "__main__":
    unittest.main()