# Project 02: PID Motion Controller

## Goal

Add a feedback controller to the differential-drive simulator so the robot can move toward a target pose automatically.

This project builds on Project 01 and introduces closed-loop control, error computation, and controller tuning.

---

## Why this project matters

A simulator is only half the story. Without feedback, the robot just obeys commands blindly like a very expensive shopping cart.

This project teaches:

* open-loop vs closed-loop control
* error computation
* proportional, integral, and derivative action
* controller tuning
* stability and convergence

---

## Learning objectives

By the end of this project you should understand:

* how feedback reduces error
* why a controller needs a target and a measured state
* how P, PI, PD, and PID behave differently
* how tuning affects overshoot, oscillation, and settling time
* how to design reusable control code for later robotics projects

---

## What we will build

We will extend the differential-drive simulator from Project 01 and add a controller that generates velocity commands automatically.

The robot should:

* start from an initial pose
* move toward a target pose
* reduce position and heading error over time
* stop when it reaches a tolerance threshold

---

## Mathematical idea

Let the robot state be:

`state = [x, y, theta]`

Let the target be:

`target = [x_goal, y_goal, theta_goal]`

Define the error between target and current state.

For this project, we will control:

* distance to goal
* heading to goal

A simple control law can be built from:

* `Kp` for immediate correction
* `Ki` for accumulated steady-state error
* `Kd` for damping and smoother convergence

The generic PID equation is:

`u(t) = Kp * e(t) + Ki * integral(e(t)) + Kd * derivative(e(t))`

We will apply this idea in a robotics-friendly way by producing:

* linear velocity `v`
* angular velocity `omega`

---

## Recommended controller strategy

For a differential-drive robot, it is usually better to control:

* distance error with one controller
* heading error with another controller

That means:

* linear velocity is driven by distance to the target
* angular velocity is driven by heading error

This keeps the implementation simple and stable for a first robotics controller.

---

## Repository update

Add a controller layer:

```text
src/robotics_playground/
├── controllers/
│   ├── __init__.py
│   ├── base.py
│   └── pid.py
```

The simulator should call the controller through a shared interface rather than knowing the control details directly.

---

## Development stages

### Stage 1: Base controller interface

Create a generic controller API.

### Stage 2: Proportional control

Make the robot move toward the goal using only `Kp`.

### Stage 3: Full PID control

Add integral and derivative terms.

### Stage 4: Goal-reaching demo

Run the robot toward a target pose and plot the trajectory.

### Stage 5: Analysis

Compare:

* P only
* PI
* PD
* PID

---

## Verification

The controller is working if:

* the robot moves toward the goal
* heading error decreases over time
* the robot does not spin endlessly
* the path is smooth and stable
* the final pose is within tolerance

---

## Deliverables

* `base.py` for the controller interface
* `pid.py` for the PID controller
* `pid_demo.py` for a sample run
* trajectory plot
* error plots
* updated README section for Project 02

---

## Future extension

After this project, the same controller interface will support:

* Pure Pursuit
* Stanley Controller
* LQR
* MPC

That is the whole point of doing the architecture properly now instead of improvising later like a caffeinated raccoon.
