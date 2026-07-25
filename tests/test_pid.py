import math

from robotics_playground.robot import DifferentialDriveRobot

from robotics_playground.controllers.pid import (
    PIDController,
    PIDGains,
)


def test_zero_error():

    robot = DifferentialDriveRobot()

    controller = PIDController(

        distance_gains=PIDGains(1.0),
        heading_gains=PIDGains(2.0),
    )

    controller.set_target((0, 0, 0))

    v, omega = controller.compute_control(
        robot,
        dt=0.1,
    )

    assert math.isclose(v, 0.0, abs_tol=1e-6)

    assert math.isclose(
        omega,
        0.0,
        abs_tol=1e-6,
    )


def test_positive_distance():

    robot = DifferentialDriveRobot()

    controller = PIDController(

        distance_gains=PIDGains(1.0),

        heading_gains=PIDGains(2.0),
    )

    controller.set_target((5, 0, 0))

    v, omega = controller.compute_control(
        robot,
        dt=0.1,
    )

    assert v > 0

    assert abs(omega) < 1e-6


def test_heading_turn():

    robot = DifferentialDriveRobot()

    controller = PIDController(

        distance_gains=PIDGains(1.0),

        heading_gains=PIDGains(2.0),
    )

    controller.set_target((0, 5, 0))

    v, omega = controller.compute_control(
        robot,
        dt=0.1,
    )

    assert omega > 0