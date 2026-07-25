from dataclasses import dataclass, field
from typing import List, Tuple

from robotics_playground.robot import DifferentialDriveRobot
from robotics_playground.controllers.base import Controller


@dataclass
class Simulator:
    robot: DifferentialDriveRobot
    dt: float = 0.05
    t_end: float = 20.0

    history: List[Tuple[float, float, float, float]] = field(default_factory=list)

    def reset(self):
        self.history.clear()

    def run(self, controller: Controller):
        """
        Runs the simulation.

        Controller must implement

            compute_control(robot, dt)

        returning

            (v, omega)
        """

        controller.reset()
        self.reset()

        t = 0.0

        while t <= self.t_end:

            v, omega = controller.compute_control(self.robot, self.dt)

            self.robot.step(v, omega, self.dt)

            self.history.append(
                (
                    t,
                    self.robot.x,
                    self.robot.y,
                    self.robot.theta,
                )
            )

            t += self.dt

        return self.history