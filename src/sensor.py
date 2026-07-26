import random


class PositionSensor:
    def __init__(self, noise_std: float):
        if noise_std < 0:
            raise ValueError("noise_std must be non-negative")
        
        self.noise_std = noise_std

    def measure(self, x: float, y: float) -> tuple[float, float]:
        measured_x = x + random.gauss(0, self.noise_std)
        measured_y = y + random.gauss(0, self.noise_std)
        return (measured_x, measured_y)