import random
from src.tracking import calculate_mean_position, calculate_position_error, calculate_weighted_mean_position
from src.visualization import plot_positions
from src.model import MovingObject
from src.sensor import PositionSensor
from src.alpha_beta_filter import AlphaBetaFilter
from src.kalman_filter import KalmanFilter


def main() -> None:
    sensors = [PositionSensor(1), PositionSensor(3), PositionSensor(5)]
    weights = [1 / sensor.noise_std**2 for sensor in sensors]
    obj = MovingObject(0, 0, 2, 1)
    alpha_beta_filter = None
    kalman_x = KalmanFilter(0.0, 0.0, 1.0, 4.0, 0.1)
    kalman_y = KalmanFilter(0.0, 0.0, 1.0, 4.0, 0.1)
    alpha = 0.4
    beta = 0.05
    dt = 0.1
    real_positions: list[tuple[float, float]] = []
    mean_estimates: list[tuple[float, float]] = []
    weighted_mean_estimates: list[tuple[float, float]] = []
    individual_sensor_readings: list[tuple[float, float]] = []
    alpha_beta_filter_estimates: list[tuple[float, float]] = []
    kalman_estimates: list[tuple[float, float]] = []
    total_sensor_error = 0.0
    total_mean_error = 0.0
    total_weighted_mean_error = 0.0
    total_alpha_beta_filter_error = 0.0
    total_kalman_error = 0.0

    for _ in range(100):
        obj.update(dt)
        real_position = (obj.x, obj.y)
        real_positions.append(real_position)
        sensor_readings = []
        for sensor in sensors:
            sensor_readings.append(sensor.measure(obj.x, obj.y))
        mean_estimate = calculate_mean_position(sensor_readings)
        weighted_mean_estimate = calculate_weighted_mean_position(sensor_readings, weights)
        if alpha_beta_filter is None:
            alpha_beta_filter = AlphaBetaFilter(weighted_mean_estimate, (0, 0), alpha, beta)
            filtered_position = weighted_mean_estimate
        else:
            filtered_position = alpha_beta_filter.update(weighted_mean_estimate, dt)
        kalman_x.predict(dt)
        kalman_y.predict(dt)
        kalman_x.update(weighted_mean_estimate[0], 1 / sum(weights))
        kalman_y.update(weighted_mean_estimate[1], 1 / sum(weights))
        mean_estimates.append(mean_estimate)
        individual_sensor_readings.append(sensor_readings[0])
        weighted_mean_estimates.append(weighted_mean_estimate)
        alpha_beta_filter_estimates.append(filtered_position)
        kalman_estimates.append((kalman_x.state[0], kalman_y.state[0]))
        total_sensor_error += calculate_position_error(real_position, sensor_readings[0])
        total_mean_error += calculate_position_error(real_position, mean_estimate)
        total_weighted_mean_error += calculate_position_error(real_position, weighted_mean_estimate)
        total_alpha_beta_filter_error += calculate_position_error(real_position, filtered_position)
        total_kalman_error += calculate_position_error(real_position, (kalman_x.state[0], kalman_y.state[0]))

    number_of_positions = len(real_positions)
    mean_sensor_error = total_sensor_error / number_of_positions
    mean_unweighted_error = total_mean_error / number_of_positions
    mean_weighted_error = total_weighted_mean_error / number_of_positions
    mean_alpha_beta_error = total_alpha_beta_filter_error / number_of_positions
    mean_kalman_error = total_kalman_error / number_of_positions

    improvement = (
        (mean_weighted_error - mean_alpha_beta_error)
        / mean_weighted_error
    ) * 100

    print(f"Mean sensor error: {mean_sensor_error:.3f}")
    print(f"Mean unweighted estimate error: {mean_unweighted_error:.3f}")
    print(f"Mean weighted estimate error: {mean_weighted_error:.3f}")
    print(f"Alpha-beta filter mean error: {mean_alpha_beta_error:.3f}")
    print(f"Improvement over weighted estimate: {improvement:.1f}%")
    print(f"Kalman filter mean error: {mean_kalman_error:.3f}")
    plot_positions(real_positions, individual_sensor_readings,
                   mean_estimates, weighted_mean_estimates, 
                   alpha_beta_filter_estimates, kalman_estimates)


if __name__ == "__main__":
    main()
