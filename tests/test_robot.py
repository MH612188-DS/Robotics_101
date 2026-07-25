import math
from src.robotics_playground.robot import DifferentialDriveRobot


def test_straight_motion():
    r = DifferentialDriveRobot()
    r.step(v=1.0, omega=0.0, dt=1.0)
    assert abs(r.x - 1.0) < 1e-6
    assert abs(r.y - 0.0) < 1e-6


def test_rotation_only():
    r = DifferentialDriveRobot()
    r.step(v=0.0, omega=math.pi, dt=1.0)
    assert abs(r.x - 0.0) < 1e-6
    assert abs(r.y - 0.0) < 1e-6
    assert abs(abs(r.theta) - math.pi) < 1e-6 or abs(r.theta + math.pi) < 1e-6