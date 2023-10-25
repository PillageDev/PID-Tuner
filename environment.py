import pybullet as p
import pybullet_data
import matplotlib.pylab as plt
import time

physics_client = p.connect(p.GUI)
p.setGravity(0, 0, -9.81)
plane_id = p.loadURDF("C:\\Users\\llluy\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\pybullet_data\\plane_transparent.urdf")
p.resetBasePositionAndOrientation(plane_id, [0, 0, 0], [0, 0, 0, 1])
robot_starting_pos = [0, 0, 1]
robot_starting_orientation = p.getQuaternionFromEuler([0, 0, 0])
robot_id = p.loadURDF("C:\\Users\\llluy\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\pybullet_data\\cube_small.urdf", robot_starting_pos, robot_starting_orientation)

for _ in range(1000):
    p.stepSimulation()
    time.sleep(1. / 240.)
    
    linear_vel, _ = p.getBaseVelocity(robot_id)
    speed_x, speed_y, speed_z = linear_vel
    speed_magnitude = (speed_x**2 + speed_y**2 + speed_z**2)**0.5
    
    plt.plot(_, linear_vel)
    plt.title("Linear Velocity")
    plt.show()
p.disconnect()
