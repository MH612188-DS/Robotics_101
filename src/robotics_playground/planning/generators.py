import math

from robotics_playground.planning.path import Path


def straight_line(
    length=5.0,
    samples=100,
):

    pts = []

    for i in range(samples):

        x = length * i / (samples - 1)

        pts.append((x, 0))

    return Path(pts)


def circle(
    radius=2.0,
    samples=300,
):

    pts = []

    for i in range(samples):

        theta = 2 * math.pi * i / samples

        pts.append(
            (
                radius * math.cos(theta),
                radius * math.sin(theta),
            )
        )

    return Path(pts)


def square(
    side=4.0,
    samples_per_side=50,
):

    pts = []

    for i in range(samples_per_side):

        pts.append((i * side / samples_per_side, 0))

    for i in range(samples_per_side):

        pts.append((side, i * side / samples_per_side))

    for i in range(samples_per_side):

        pts.append(
            (
                side - i * side / samples_per_side,
                side,
            )
        )

    for i in range(samples_per_side):

        pts.append(
            (
                0,
                side - i * side / samples_per_side,
            )
        )

    return Path(pts)


def sine_wave(
    length=10,
    amplitude=1,
    samples=300,
):

    pts = []

    for i in range(samples):

        x = length * i / samples

        y = amplitude * math.sin(x)

        pts.append((x, y))

    return Path(pts)


def figure_eight(
    radius=2,
    samples=500,
):

    pts = []

    for i in range(samples):

        t = 2 * math.pi * i / samples

        x = radius * math.sin(t)

        y = radius * math.sin(t) * math.cos(t)

        pts.append((x, y))

    return Path(pts)