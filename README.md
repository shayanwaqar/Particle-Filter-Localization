# Particle-Filter-Localization

Implementation of a Particle Filter for robot localization in the Webots simulator using LiDAR measurements and differential drive kinematics.

```
# Particle Filter Localization in Webots

## Overview

This project implements Particle Filter Localization for an E-Puck robot navigating a maze in the Webots simulator. The robot starts without knowledge of its initial position and relies on LiDAR sensor measurements to estimate its pose. The project focuses on:

- Coordinate transformations between world, sensor, and robot frames  
- LiDAR measurement simulation for accurate distance estimation  
- Differential drive kinematics for motion modeling  
- Handling localization ambiguity in symmetrical environments  
- Graphical visualization of particle distribution and localization process  

---

## Project Structure

### 📂 Worlds  
- `maze_world1.wbt` - A small maze environment with symmetrical features.

### 🎮 Controller  
- `proj4_maze_world1_controller.py` - Controls the robot's movement in the maze.

### 🛠️ Particle Filter Implementation  
- `environment.py` - Handles robot interactions and simulation environment.  
- `geometry.py` - Implements geometric transformations and calculations.  
- `gui.py` - Provides a graphical interface for visualization.  
- `particle_filter.py` - Implements the particle filter algorithm.  
- `run_pf.py` - Runs the particle filter using pre-recorded LiDAR data.  
- `wall.py` - Defines wall structures and their corner points.  
- `lidar_sim.py` - Simulates LiDAR measurements for particles.  
- `settings.py` - Stores configuration settings.  
- `utils.py` - Contains helper functions used across the project.  
- `unit_tests.py` - Includes unit tests for geometry, environment, and LiDAR simulation.  

---

## Installation

1. Install Webots if not already installed:  
   [Download Webots](https://cyberbotics.com/)  

2. Clone this repository:  
```

git clone [https://github.com/shayanwaqar/Particle-Filter-Localization.git](https://github.com/shayanwaqar/Particle-Filter-Localization.git)
cd Particle-Filter-Webots

```

3. Install dependencies:  
```

pip install -r requirements.txt

```

---

## Running the Project

### Option 1: Run in Webots Simulator
1. Open `maze_world1.wbt` in Webots.
2. Run the robot controller:
```

python proj4_maze_world1_controller.py

```
3. A GUI will open to visualize the particles and robot pose.

### Option 2: Run the Particle Filter Separately
1. Enable data capture in `settings.py`:  
```

DATA_CAPTURE_MODE = True

```
2. Run the Webots simulation to generate LiDAR data.  
3. Run the particle filter on the recorded data:
```

python run_pf.py

```
4. The GUI will display particle distribution and localization results.

---

## Testing
Run unit tests to verify key components:
```

python unit_tests.py

```
Ensure all tests pass before running the full simulation.

---

## Notes
- Webots' LiDAR returns `inf` values when no obstacles are detected.  
- Localization starts with uncertainty but improves as the robot explores.  
- Debug using local tests before relying on an autograder.  

---

## License
This project is released under the MIT License. See `LICENSE` for details.
```
