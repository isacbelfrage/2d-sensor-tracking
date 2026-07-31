class KalmanFilter:
    def __init__(self,
                position: float,
                velocity: float,
                position_variance: float, 
                velocity_variance: float,
                acceleration_variance: float):
        self.state: list[float] = [position, velocity]
        self.covariance: list[list[float]] = [[position_variance, 0.0],
                                              [0.0, velocity_variance]]
        self.acceleration_variance = acceleration_variance
        

    