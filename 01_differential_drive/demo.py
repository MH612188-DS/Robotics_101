import math

from src.robot import DifferentialDriveRobot
from src.simulator import Simulator
from src.visualization import (
    plot_trajectory,
    animate_trajectory,
)


def straight_line_control(t, robot):
    return 0.5, 0.0


def circle_control(t, robot):
    return 0.5, 0.5


def rotate_in_place_control(t, robot):
    return 0.0, 0.8


def run_demo():
    robot = DifferentialDriveRobot(x=0.0, y=0.0, theta=0.0)
    sim = Simulator(robot=robot, dt=0.05, t_end=12.0)

    history = sim.run(circle_control)

    plot_trajectory(history)

    anim = animate_trajectory(history)


if __name__ == "__main__":
    run_demo()