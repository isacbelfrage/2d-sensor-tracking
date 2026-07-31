import numpy as np


class KalmanFilter:
    def __init__(self,
                position: float,
                velocity: float,
                position_variance: float, 
                velocity_variance: float,
                acceleration_variance: float):
        self.state = np.array([position, velocity], dtype=float)
        self.covariance = np.array(
            [
                [position_variance, 0.0], 
                [0.0, velocity_variance]
            ], 
            dtype=float
        )
        self.acceleration_variance = acceleration_variance

    def predict(self, dt: float) -> None:
        if dt <= 0:
            raise ValueError("dt must be positive")
        state_transition = np.array([[1, dt], [0, 1]])
        predicted_state = state_transition @ self.state
        process_noise = np.array([[self.acceleration_variance * dt**4 / 4, self.acceleration_variance * dt**3 / 2],
                                  [self.acceleration_variance * dt**3 / 2, self.acceleration_variance * dt**2]])
        predicted_covariance = state_transition @ self.covariance @ state_transition.T + process_noise
        self.state = predicted_state
        self.covariance = predicted_covariance

    def update(self, measurement: float, measurement_variance: float) -> None:
        if measurement_variance < 0:
            raise ValueError("measurement_variance must be non-negative")
        measurement_model = np.array([[1, 0]])
        measurement_residual = measurement - measurement_model @ self.state
        residual_variance = measurement_model @ self.covariance @ measurement_model.T + measurement_variance
        kalman_gain = self.covariance @ measurement_model.T @ np.linalg.inv(residual_variance)
        self.state = self.state + kalman_gain @ measurement_residual
        self.covariance = (np.identity(2) - kalman_gain @ measurement_model) @ self.covariance

        
        