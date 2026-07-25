from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter


ASSETS = Path("assets")
GIF_DIR = ASSETS / "gifs"
VIDEO_DIR = ASSETS / "videos"
FIGURE_DIR = ASSETS / "figures"

GIF_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def plot_trajectory(history, save=False):

    xs = [h[1] for h in history]
    ys = [h[2] for h in history]

    plt.figure(figsize=(6, 6))

    plt.plot(xs, ys, linewidth=2)

    plt.scatter(xs[0], ys[0], c="green", s=80, label="Start")
    plt.scatter(xs[-1], ys[-1], c="red", s=80, label="Goal")

    plt.grid(True)
    plt.axis("equal")

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")

    plt.legend()

    if save:
        plt.savefig(
            FIGURE_DIR / "trajectory.png",
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()


def animate_robot(
    history,
    interval=40,
    save_gif=False,
    save_mp4=False,
):
    """
    SPACE -> Pause/Resume
    ESC   -> Close animation
    """

    xs = [h[1] for h in history]
    ys = [h[2] for h in history]
    thetas = [h[3] for h in history]

    fig, ax = plt.subplots(figsize=(7, 7))

    margin = 1.0

    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys) - margin, max(ys) + margin)

    ax.set_aspect("equal")

    ax.grid(True)

    trajectory, = ax.plot([], [], lw=2)

    robot, = ax.plot([], [], "bo", markersize=8)

    heading, = ax.plot([], [], lw=3)

    paused = False

    def init():

        trajectory.set_data([], [])

        robot.set_data([], [])

        heading.set_data([], [])

        return trajectory, robot, heading

    def update(frame):

        trajectory.set_data(xs[: frame + 1], ys[: frame + 1])

        robot.set_data([xs[frame]], [ys[frame]])

        length = 0.25

        hx = xs[frame] + length * __import__("math").cos(thetas[frame])
        hy = ys[frame] + length * __import__("math").sin(thetas[frame])

        heading.set_data(
            [xs[frame], hx],
            [ys[frame], hy],
        )

        return trajectory, robot, heading

    anim = FuncAnimation(
        fig,
        update,
        frames=len(history),
        init_func=init,
        interval=interval,
        blit=False,
        repeat=False,
    )

    def on_key(event):
        nonlocal paused

        if event.key == " ":

            paused = not paused

            if paused:
                anim.event_source.stop()
            else:
                anim.event_source.start()

        elif event.key == "escape":
            plt.close(fig)

    fig.canvas.mpl_connect("key_press_event", on_key)

    if save_gif:

        print("Saving GIF...")

        anim.save(
            GIF_DIR / "pid_controller.gif",
            writer=PillowWriter(fps=25),
        )

        print("GIF saved.")

    if save_mp4:

        print("Saving MP4...")

        writer = FFMpegWriter(fps=25)

        anim.save(
            VIDEO_DIR / "pid_controller.mp4",
            writer=writer,
        )

        print("MP4 saved.")

    plt.show()

    return anim