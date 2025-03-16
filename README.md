# Particle-Filter-Localization

Implementation of a Particle Filter for robot localization in the Webots simulator using LiDAR measurements and differential drive kinematics.

```
# Particle Filter Implementation in Webots Simulator

## Overview

This project implements **Particle Filter Localization** for an **E-Puck** robot in the **Webots simulator**. The robot begins without knowing its initial position and relies on **LiDAR sensor measurements** to localize itself in a maze environment. The project involves **coordinate transformations, differential drive kinematics, LiDAR measurement simulation, and handling ambiguous environments**.

## Features

- **Coordinate Transformations**: Implements transformations between world, sensor, and robot frames for accurate localization.
- **LiDAR Measurement Simulation**: Simulates LiDAR distance readings for particles in the maze.
- **Differential Drive Kinematics**: Computes robot motion based on wheel encoder data.
- **Handling Ambiguous Environments**: Solves localization challenges caused by symmetrical maze features.
- **Graphical Visualization**: A Python GUI displays particles, robot trajectory, and LiDAR readings.

## Project Structure

The repository contains the following key files:

### Worlds
- `maze_world1.wbt` - A small maze environment with symmetrical features.

### Controller
- `proj4_maze_world1_controller.py` - Controls the robot's movement in the maze.

### Particle Filter
- `environment.py` - Simulates the environment and robot interactions.
- `geometry.py` - Implements geometric calculations and transformations.
- `gui.py` - Provides a graphical interface for particle filter visualization.
- `particle_filter.py` - Implements the particle filter algorithm.
- `run_pf.py` - Runs the particle filter using captured data.
- `wall.py` - Manages wall structures and corner points.
- `lidar_sim.py` - Simulates LiDAR measurements for particles.
- `settings.py` - Holds configuration settings.
- `utils.py` - Contains utility functions.
- `unit_tests.py` - Includes unit tests for key components.

## Installation

1. Install Webots if not already installed:  
   [Download Webots](https://cyberbotics.com/)
   
2. Clone this repository:
```

git clone [https://github.com/yourusername/Particle-Filter-Webots.git](https://github.com/yourusername/Particle-Filter-Webots.git)
cd Particle-Filter-Webots

```

3. Install required dependencies:
```

pip install -r requirements.txt

```

## Running the Project

### Run in Webots Simulator
1. Open `maze_world1.wbt` in Webots.
2. Run the robot controller:
```

python proj4_maze_world1_controller.py

```
3. The Python GUI will visualize the robot's pose and particles.

### Run Particle Filter Separately
1. Enable data capture in `settings.py`:
```

DATA_CAPTURE_MODE = True

```
2. Run the Webots simulation to generate data.
3. Run the particle filter:
```

python run_pf.py

```
4. The GUI will visualize particle movement.

## Testing
Run unit tests before executing the full simulation:
```

python unit_tests.py

```
Ensure all tests pass before proceeding.

## Notes
- Webots' LiDAR may return `inf` values for out-of-range measurements.
- The robot starts with ambiguous localization but improves as it explores.
- Use local tests before submitting to an autograder.

## License
This project is released under the MIT License. See `LICENSE` for details.
```
