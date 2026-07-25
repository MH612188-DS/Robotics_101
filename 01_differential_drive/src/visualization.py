import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_trajectory(history):
    xs = [h[1] for h in history]
    ys = [h[2] for h in history]

    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, label="trajectory")
    plt.scatter(xs[0], ys[0], label="start")
    plt.scatter(xs[-1], ys[-1], label="end")
    plt.axis("equal")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.show(block=True)


def animate_trajectory(history):
    xs = [h[1] for h in history]
    ys = [h[2] for h in history]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    line, = ax.plot([], [], lw=2)
    point, = ax.plot([], [], "ro")

    margin = 1.0
    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys) - margin, max(ys) + margin)

    def init():
        line.set_data([], [])
        point.set_data([], [])
        return line, point

    def update(frame):
        line.set_data(xs[:frame + 1], ys[:frame + 1])
        point.set_data([xs[frame]], [ys[frame]])
        return line, point

    anim = FuncAnimation(
        fig,
        update,
        frames=len(history),
        init_func=init,
        blit=False,
        interval=50,
    )
    return anim