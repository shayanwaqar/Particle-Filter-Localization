import math
import numpy as np
from utils import *
from wall import Wall

class LidarSim:
    # Constructor
    def __init__(self, walls:list[Wall], max_range:float, n_rays:float):
        self.walls = walls
        self.max_range = max_range
        self.n_rays = n_rays
        self.resolution = int(360/n_rays)
        self.measurements = math.inf*np.ones(self.resolution)

    # Simulate the lidar sensor reading
    def read(self, pose:SE2) -> np.ndarray:
        '''
        Simulate the lidar sensor readings given the current pose of the robot.

        Parameters:
        pose (SE2): The current pose of the robot, represented as an SE2 object, 
        which includes the x and y coordinates and the heading (orientation) of 
        the robot.

        Returns:
        np.ndarray: An array of simulated lidar measurements, where each element 
        represents the distance to the nearest wall for a specific lidar ray.

        Steps:
        1. Iterate through each lidar ray:
           - For each ray, calculate the angle based on the robot's heading and 
           the resolution of the lidar.
           - Determine the endpoint of the lidar ray based on the maximum range 
           and the calculated angle.

        2. Check for intersections with walls:
           - For each wall, check if the lidar ray intersects with the wall 
           using the line_rectangle_intersect function.
           - If an intersection is detected, calculate the intersection points 
           between the lidar ray and the edges of the wall.
           - Calculate the distances from the robot to these intersection points.

        4. Find the minimum distance:
           - Among all intersection points, find the minimum distance and update 
           the measurements array for the corresponding ray.

        5. Return the measurements:
           - Return the array of simulated lidar measurements.
        '''

        # Reset the measurements
        self.measurements = math.inf*np.ones(self.n_rays) # Webots lidar sensor returns inf for no detection
        
        ######### START STUDENT CODE #########
        # Hint - You may find the following functions in utils.py useful: 
        # line_rectangle_intersect, line_segment_intersect, line_intersection, distance_between_points
        for i in range(self.n_rays):
            angle = i * (360 / self.n_rays) + (360 / (2 * self.n_rays))
            angle_rad = math.radians(angle)
            cos = math.cos(pose.h + angle_rad)
            sin = math.sin(pose.h + angle_rad)
            ray_end_x = pose.x + self.max_range * cos
            ray_end_y = pose.y + self.max_range * sin
            ray_end = Point(ray_end_x, ray_end_y)
            min_distance = self.max_range
            for wall in self.walls:
                  wall.compute_line_equations()
                  if line_rectangle_intersect(pose.position(), ray_end, wall.pose, wall.dimensions):
                     edges = [
                        Point(wall.top_left[0], wall.top_left[1]),
                        Point(wall.top_right[0], wall.top_right[1]),
                        Point(wall.bottom_right[0], wall.bottom_right[1]),
                        Point(wall.bottom_left[0], wall.bottom_left[1])
                     ]
                     wall_edges = [
                        (edges[0], edges[1]),
                        (edges[1], edges[2]),
                        (edges[2], edges[3]),
                        (edges[3], edges[0])
                     ]
                     for edge_start, edge_end in wall_edges:
                        intersection = line_intersection(pose.position(), ray_end, edge_start, edge_end)
                        if intersection:
                              distance = distance_between_points(pose.position(), intersection)
                              if distance < min_distance:
                                 min_distance = distance
            if min_distance < self.max_range:
                  self.measurements[i] = min_distance
               
        ########## END STUDENT CODE ##########

        return self.measurements
