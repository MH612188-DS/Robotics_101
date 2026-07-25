from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple
import math


@dataclass(frozen=True)
class Waypoint:
    x: float
    y: float
    heading: float
    curvature: float
    arc_length: float

    def distance_to(self, x: float, y: float) -> float:
        return math.hypot(self.x - x, self.y - y)


class Path:

    def __init__(self, points: Iterable[Tuple[float, float]]):

        pts = list(points)

        if len(pts) < 2:
            raise ValueError("Path requires at least two points.")

        self.waypoints: List[Waypoint] = []

        arc = 0.0

        for i, (x, y) in enumerate(pts):

            # ---------- heading ----------

            if i < len(pts) - 1:
                nx, ny = pts[i + 1]
                heading = math.atan2(ny - y, nx - x)

            else:
                px, py = pts[i - 1]
                heading = math.atan2(y - py, x - px)

            # ---------- arc length ----------

            if i > 0:
                px, py = pts[i - 1]
                arc += math.hypot(x - px, y - py)

            # ---------- curvature ----------
            # Placeholder for now.
            # We'll compute true curvature later.

            curvature = 0.0

            self.waypoints.append(
                Waypoint(
                    x=x,
                    y=y,
                    heading=heading,
                    curvature=curvature,
                    arc_length=arc,
                )
            )

    def __len__(self):
        return len(self.waypoints)

    def __getitem__(self, idx):
        return self.waypoints[idx]

    @property
    def length(self):
        return self.waypoints[-1].arc_length

    def closest_index(self, x: float, y: float):

        distances = [
            wp.distance_to(x, y)
            for wp in self.waypoints
        ]

        return distances.index(min(distances))

    def closest_waypoint(self, x: float, y: float):
        return self.waypoints[self.closest_index(x, y)]

    def lookahead_point(
        self,
        x: float,
        y: float,
        lookahead: float,
    ):

        idx = self.closest_index(x, y)

        start_arc = self.waypoints[idx].arc_length

        for wp in self.waypoints[idx:]:

            if wp.arc_length - start_arc >= lookahead:
                return wp

        return self.waypoints[-1]