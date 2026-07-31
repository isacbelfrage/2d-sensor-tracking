## Alpha-Beta Filter Parameter Experiment

- dt = 0.1
- nbr of steps: 100
- noise_std = 1, 3, 5
- velocity of object (2, 1)
- initial velocity for filter = (0, 0)
- the first weighted mean estimation is used as initial position


Random seed: `42`

| Alpha | Beta | Weighted Mean Error | Alpha-Beta Error | Improvement | Notes |
|:------:|:----:|--------------------:|-----------------:|------------:|-------|
| 0.80 | 0.20 | 1.171 | 0.960 | 18.0% | current reference, jumpy and uneven tracking |
| 0.40 | 0.20 | 1.171 | 0.709 | 39.5% | better improvement and smoother tracking visually |
| 0.80 | 0.05 | 1.171 | 0.953 | 18.7% | similar to first test |
| 0.40 | 0.05 | 1.171 | 0.610 | 47.9% | smoothest tracking visually |

Random seed: `7`

| Alpha | Beta | Weighted Mean Error | Alpha-Beta Error | Improvement | Notes |
|:------:|:----:|--------------------:|-----------------:|------------:|-------|
| 0.80 | 0.20 | 1.132 | 0.967 | 14.6% | current reference, jumpy and uneven tracking |
| 0.40 | 0.20 | 1.132 | 0.806 | 28.8% | better improvement and smoother tracking visually |
| 0.80 | 0.05 | 1.132 | 0.954 | 15.7% | similar to first test |
| 0.40 | 0.05 | 1.132 | 0.676 | 40.3% | smoothest tracking visually |

### Conclusion
Among the tested parameter combinations, alpha=0.4 and beta=0.05 produced the lowest mean position error and the smoothest trajectory for both random seeds. This result is limited to the current constant-velocity simulation and does not prove that these gains are optimal for other motion patterns or noise conditions.

## Kalman Filter Comparison

The Kalman filter was compared with the weighted mean and the alpha-beta filter
using several random seeds. Each seed produces a different but reproducible
sequence of sensor noise.

- dt = 0.1
- number of steps = 100
- sensor noise standard deviations = 1, 3, 5
- object velocity = (2, 1)
- Kalman initial position = (0, 0)
- Kalman initial velocity = (0, 0)
- initial position variance = 1.0
- initial velocity variance = 4.0
- acceleration variance = 0.1
- measurement variance = inverse-variance weighted sensor variance
- alpha = 0.4
- beta = 0.05

| Random seed | Weighted mean error | Alpha-beta error | Kalman error | Kalman improvement over weighted mean | Kalman improvement over alpha-beta |
|------------:|--------------------:|-----------------:|-------------:|--------------------------------------:|-----------------------------------:|
| 42 | 1.171 | 0.610 | 0.375 | 68.0% | 38.5% |
| 7 | 1.132 | 0.676 | 0.326 | 71.2% | 51.8% |
| 123 | 1.248 | 0.645 | 0.417 | 66.6% | 35.3% |
| 2026 | 1.241 | 0.638 | 0.348 | 72.0% | 45.5% |
| **Mean** | **1.198** | **0.642** | **0.367** | **69.4%** | **42.9%** |

### Conclusion

The Kalman filter produced the lowest mean position error for all four tested
random seeds. On average, its error was 69.4% lower than the weighted mean and
42.9% lower than the alpha-beta filter. This result applies to the current
constant-velocity simulation and the selected filter parameters. It does not
show that the Kalman filter will always perform better for other motion models,
noise assumptions, or parameter choices.
