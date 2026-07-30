class AlphaBetaFilter:
    def __init__(self, position: tuple[float, float],
                velocity: tuple[float, float],
                alpha: float, beta: float):
        self.position = position
        self.velocity = velocity
        self.alpha = alpha
        self.beta = beta

    def update(self, measurement: tuple[float, float], dt: float) -> tuple[float, float]:
        if dt <= 0:
            raise ValueError("dt must be greater than zero")
        x, y = self.position
        vx, vy = self.velocity

        predicted_x = x + vx * dt
        predicted_y = y + vy * dt
        residual_x = measurement[0] - predicted_x
        residual_y = measurement[1] - predicted_y
        x = predicted_x + self.alpha * residual_x
        y = predicted_y + self.alpha * residual_y
        vx = vx + (self.beta / dt) * residual_x
        vy = vy + (self.beta / dt) * residual_y
        self.velocity = (vx, vy)
        self.position = (x, y)
        return self.position