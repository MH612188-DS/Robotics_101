import math
from dataclasses import dataclass
from typing import Tuple

from robotics_playground.controllers.base import Controller
from robotics_playground.robot import DifferentialDriveRobot, wrap_angle


@dataclass
class PIDGains:
    kp: float
    ki: float = 0.0
    kd: float = 0.0


class PIDController(Controller):
    def __init__(
        self,
        distance_gains: PIDGains,
        heading_gains: PIDGains,
        v_max: float = 1.0,
        omega_max: float = 1.5,
        goal_tolerance: float = 0.05,
        heading_tolerance: float = 0.05,
        
    ):  
        self.target = (0.0, 0.0, 0.0)
        self.distance_gains = distance_gains
        self.heading_gains = heading_gains
        self.v_max = v_max
        self.omega_max = omega_max
        self.goal_tolerance = goal_tolerance
        self.heading_tolerance = heading_tolerance

        self.reset()

    def set_target(self, target):
        self.target = target

    def reset(self) -> None:
        self.distance_integral = 0.0
        self.heading_integral = 0.0
        self.prev_distance_error = 0.0
        self.prev_heading_error = 0.0

    def _clamp(self, value: float, limit: float) -> float:
        return max(-limit, min(limit, value))

    def compute_control(self, robot, dt: float) -> Tuple[float, float]:
        x, y, theta = robot.x, robot.y, robot.theta

        xg, yg, thetag = self.target
        dx = xg - x
        dy = yg - y
        distance_error = math.sqrt(dx * dx + dy * dy)

        desired_heading = math.atan2(dy, dx)
        heading_error = wrap_angle(desired_heading - theta)

        goal_heading_error = wrap_angle(thetag - theta)

        # Distance PID
        self.distance_integral += distance_error * dt
        distance_derivative = (distance_error - self.prev_distance_error) / dt if dt > 0 else 0.0
        v = (
            self.distance_gains.kp * distance_error
            + self.distance_gains.ki * self.distance_integral
            + self.distance_gains.kd * distance_derivative
        )

        # Heading PID
        self.heading_integral += heading_error * dt
        heading_derivative = (heading_error - self.prev_heading_error) / dt if dt > 0 else 0.0
        omega = (
            self.heading_gains.kp * heading_error
            + self.heading_gains.ki * self.heading_integral
            + self.heading_gains.kd * heading_derivative
        )

        self.prev_distance_error = distance_error
        self.prev_heading_error = heading_error

        # Stop when close enough to target
        if distance_error < self.goal_tolerance and abs(goal_heading_error) < self.heading_tolerance:
            return 0.0, 0.0

        return self._clamp(v, self.v_max), self._clamp(omega, self.omega_max)