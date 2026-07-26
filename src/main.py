from src.tracking import calculate_mean_position, calculate_position_error
from src.model import MovingObject
from src.sensor import PositionSensor

def main() -> None:
    sensor_1 = PositionSensor(1)
    sensor_2 = PositionSensor(1)
    sensor_3 = PositionSensor(1)

    obj = MovingObject(0, 0, 2, 1)
    real_positions: list[tuple[float, float]] = []
    estimated_positions: list[tuple[float, float]] = []
    sensor_1_positions: list[tuple[float, float]] = []
    total_sensor_error = 0.0
    total_estimation_error = 0.0

    for _ in range(100):
        obj.update(0.1)
        real_position = (obj.x, obj.y)
        real_positions.append(real_position)
        sensor_1_reading = sensor_1.measure(obj.x, obj.y)
        sensor_2_reading = sensor_2.measure(obj.x, obj.y)
        sensor_3_reading = sensor_3.measure(obj.x, obj.y)
        sensor_readings = [sensor_1_reading, sensor_2_reading, sensor_3_reading]
        estimated_reading = calculate_mean_position(sensor_readings)
        estimated_positions.append(estimated_reading)
        sensor_1_positions.append(sensor_1_reading)        
        total_sensor_error += calculate_position_error(real_position, sensor_1_reading)
        total_estimation_error += calculate_position_error(real_position, estimated_reading)

    print("Mean sensor error:", total_sensor_error / len(real_positions))
    print("Mean estimation error:", total_estimation_error / len(real_positions))
      

if __name__ == "__main__":
    main()