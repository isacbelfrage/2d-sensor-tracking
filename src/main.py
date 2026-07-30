from src.tracking import calculate_mean_position, calculate_position_error, calculate_weighted_mean_position
from src.visualization import plot_positions
from src.model import MovingObject
from src.sensor import PositionSensor


def main() -> None:
    sensors = [PositionSensor(1), PositionSensor(3), PositionSensor(5)]
    weights = [1 / sensor.noise_std**2 for sensor in sensors]
    obj = MovingObject(0, 0, 2, 1)
    real_positions: list[tuple[float, float]] = []
    mean_estimates: list[tuple[float, float]] = []
    weighted_mean_estimates: list[tuple[float, float]] = []
    individual_sensor_readings: list[tuple[float, float]] = []
    total_sensor_error = 0.0
    total_mean_error = 0.0
    total_weighted_mean_error = 0.0

    for _ in range(100):
        obj.update(0.1)
        real_position = (obj.x, obj.y)
        real_positions.append(real_position)
        sensor_readings = []
        for sensor in sensors:
            sensor_readings.append(sensor.measure(obj.x, obj.y))
        mean_estimate = calculate_mean_position(sensor_readings)
        weighted_mean_estimate = calculate_weighted_mean_position(sensor_readings, weights)
        mean_estimates.append(mean_estimate)
        individual_sensor_readings.append(sensor_readings[0])
        weighted_mean_estimates.append(weighted_mean_estimate)
        total_sensor_error += calculate_position_error(real_position, sensor_readings[0])
        total_mean_error += calculate_position_error(real_position, mean_estimate)
        total_weighted_mean_error += calculate_position_error(real_position, weighted_mean_estimate)

    print("Mean sensor error:", total_sensor_error / len(real_positions))
    print("Mean unweighted estimate error:", total_mean_error / len(real_positions))
    print("Mean weighted estimate error:", total_weighted_mean_error / len(real_positions))
    plot_positions(real_positions, individual_sensor_readings, mean_estimates, weighted_mean_estimates)


if __name__ == "__main__":
    main()