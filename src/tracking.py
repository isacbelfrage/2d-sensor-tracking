import math


def calculate_mean_position(readings: list[tuple[float, float]]) -> tuple[float, float]:
    sum_x = 0
    sum_y = 0
    for reading in readings:
                sum_x += reading[0]
                sum_y += reading[1]
    return (sum_x / len(readings), sum_y / len(readings))

def calculate_position_error(real_position: tuple[float, float], measured_position: tuple[float, float]) -> float:
    difference = (real_position[0] - measured_position[0], 
                  real_position[1] - measured_position[1])
    return math.sqrt(math.pow(difference[0], 2) + math.pow(difference[1], 2))