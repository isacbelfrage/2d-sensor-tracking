import math


def calculate_mean_position(positions: list[tuple[float, float]]) -> tuple[float, float]:
    if len(positions) == 0:
        raise(ValueError("List can't be empty"))
    sum_x = 0.0
    sum_y = 0.0
    for position in positions:
        sum_x += position[0]
        sum_y += position[1]
    return (sum_x / len(positions), sum_y / len(positions))


def calculate_weighted_mean_position(positions: list[tuple[float, float]], weights: list[float]) -> tuple[float, float]:
    sum_weights = sum(weights)
    if len(positions) == 0:
        raise(ValueError("List can't be empty"))
    if len(weights) != len(positions):
        raise(ValueError("Lists have to be same size"))
    if sum_weights == 0:
        raise(ValueError("Sum of weights must be non-zero"))
    for weight in weights:
        if weight < 0:
            raise(ValueError("Weights must be non-negative"))
    sum_x = 0.0
    sum_y = 0.0
    for i in range(len(positions)):
        sum_x += positions[i][0] * weights[i]
        sum_y += positions[i][1] * weights[i]
    return (sum_x / sum_weights, sum_y / sum_weights)
    

def calculate_position_error(real_position: tuple[float, float], measured_position: tuple[float, float]) -> float:
    difference = (real_position[0] - measured_position[0], 
                  real_position[1] - measured_position[1])
    return math.sqrt(math.pow(difference[0], 2) + math.pow(difference[1], 2))