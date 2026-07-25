from dataclasses import dataclass
import math


def wrap_angle(theta: float) -> float:
    """Wrap angle to [-pi, pi]."""
    return (theta + math.pi) % (2.0 * math.pi) - math.pi


@dataclass
class DifferentialDriveRobot:
    x: float = 0.0
    y: float = 0.0
    theta: float = 0.0

    def pose(self):
        return self.x, self.y, self.theta

    def step(self, v: float, omega: float, dt: float) -> None:
        """
        Update robot pose using Euler integration.

        Kinematic model:
            x_dot = v * cos(theta)
            y_dot = v * sin(theta)
            theta_dot = omega
        """
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta = wrap_angle(self.theta + omega * dt)