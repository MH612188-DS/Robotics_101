from dataclasses import dataclass, field
from typing import Callable, List, Tuple

from src.robot import DifferentialDriveRobot


ControlFn = Callable[[float, DifferentialDriveRobot], Tuple[float, float]]


@dataclass
class Simulator:
    robot: DifferentialDriveRobot
    dt: float = 0.05
    t_end: float = 10.0
    history: List[Tuple[float, float, float, float]] = field(default_factory=list)

    def run(self, control_fn: ControlFn) -> List[Tuple[float, float, float, float]]:
        """
        Run simulation.

        control_fn(t, robot) -> (v, omega)
        """
        self.history.clear()

        t = 0.0
        while t <= self.t_end:
            v, omega = control_fn(t, self.robot)
            self.robot.step(v, omega, self.dt)

            self.history.append((t, self.robot.x, self.robot.y, self.robot.theta))
            t += self.dt

        return self.history