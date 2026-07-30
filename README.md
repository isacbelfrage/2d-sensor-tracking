# 2D Sensor Tracking

This is a learning project focused on implementing a system that tracks a moving object, such as a boat or drone, based on noisy sensor data. In later versions, the project will grow into a distributed system. 

Version 1 included:
- A model of an object moving at constant speed and direction.
- Three noisy position sensors
- Mean position estimation
- Error comparison
- Unit tests
- Visualization of real, measured and estimated positions

Version 2 currently includes, in addition to this:
- Weighted estimate and comparison between weighted and unweighted mean.

## Create environment

Create a virtual environment:
```bash
python -m venv .venv
```
Activate it:
```bash
source .venv/bin/activate
```
Install the project dependencies:
```bash
python -m pip install -r requirements.txt
```

## How to run the simulation
The simulation is run with this command: 
```bash
python -m src.main
```

## How to run the tests
The tests are run by using:
```bash
python -m unittest -v
```