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