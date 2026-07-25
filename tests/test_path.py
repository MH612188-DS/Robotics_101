from robotics_playground.planning.generators import (
    straight_line,
    circle,
)

from robotics_playground.planning.path import Path


def test_length():

    p = straight_line()

    assert len(p) == 100

    assert p.length > 4.9


def test_circle():

    p = circle()

    assert len(p) == 300


def test_closest():

    p = straight_line()

    idx = p.closest_index(0.2, 0)

    assert idx < 10


def test_lookahead():

    p = straight_line()

    wp = p.lookahead_point(
        0.0, 0.0, 2.0
        )

    assert wp.arc_length >= 2.0


def test_custom():

    p = Path(
        [
            (0, 0),
            (1, 0),
            (2, 0),
        ]
    )

    assert len(p) == 3