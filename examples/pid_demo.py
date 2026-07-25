import matplotlib.pyplot as plt

from robotics_playground.robot import DifferentialDriveRobot
from robotics_playground.simulator import Simulator
from robotics_playground.visualization import (
    plot_trajectory,
    animate_robot,
)

from robotics_playground.controllers.pid import (
    PIDController,
    PIDGains,
)


robot = DifferentialDriveRobot()

sim = Simulator(
    robot=robot,
    dt=0.05,
    t_end=20,
)

controller = PIDController(

    distance_gains=PIDGains(
        kp=0.8,
        ki=0.0,
        kd=0.10,
    ),

    heading_gains=PIDGains(
        kp=2.0,
        ki=0.0,
        kd=0.20,
    ),

    v_max=1.0,
    omega_max=1.5,
)

controller.set_target(
    (
        3.0,
        2.0,
        0.0,
    )
)

history = sim.run(controller)

plot_trajectory(
    history,
    save=True,
)

anim = animate_robot(
    history,
    save_gif=True,
    save_mp4=False,   # True if FFmpeg is installed
)