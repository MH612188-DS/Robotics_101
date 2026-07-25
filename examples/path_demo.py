import matplotlib.pyplot as plt

from robotics_playground.planning.generators import (
    straight_line,
    circle,
    square,
    figure_eight,
    sine_wave,
)

paths = [
    ("Straight", straight_line()),
    ("Circle", circle()),
    ("Square", square()),
    ("Figure 8", figure_eight()),
    ("Sine", sine_wave()),
]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes = axes.flatten()

for ax, (title, path) in zip(axes, paths):

    xs = [p.x for p in path.waypoints]
    ys = [p.y for p in path.waypoints]

    ax.plot(xs, ys)
    ax.set_title(title)
    ax.set_aspect("equal")
    ax.grid(True)

axes[-1].axis("off")

plt.tight_layout()
plt.show()