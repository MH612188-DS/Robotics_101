# Project 01: Differential Drive Robot Simulator

## Goal

Build a simple differential-drive robot simulator in Python from scratch.
The purpose is to understand robot state, kinematics, numerical integration, and simulation structure before adding control and estimation.

## What this project teaches

* Robot pose representation
* World frame vs robot frame
* Differential-drive kinematics
* Forward motion simulation
* Euler integration
* Basic animation and trajectory logging

## Robot state

The robot state is:

`state = [x, y, theta]`

where:

* `x` = position on the world x-axis
* `y` = position on the world y-axis
* `theta` = heading angle in radians

## Inputs

The robot is controlled by:

`u = [v, omega]`

where:

* `v` = linear velocity
* `omega` = angular velocity

## Kinematic model

The robot motion is governed by:

* `dx/dt = v * cos(theta)`
* `dy/dt = v * sin(theta)`
* `dtheta/dt = omega`

This is a kinematic model only.
No dynamics, no wheel torque, no slip modelling. Because apparently humans enjoy making simple things complicated later.

## Discrete-time simulation

Since a computer updates in steps, we approximate continuous motion using Euler integration:

* `x[k+1] = x[k] + v * cos(theta[k]) * dt`
* `y[k+1] = y[k] + v * sin(theta[k]) * dt`
* `theta[k+1] = theta[k] + omega * dt`

## Verification checks

The simulator is correct if:

* `v > 0, omega = 0` gives a straight line
* `v = 0, omega != 0` rotates in place
* `v > 0, omega != 0` produces a circle
* `v = 0, omega = 0` keeps the robot still

## Files

* `robot.py` for the robot state and update rule
* `simulator.py` for running the simulation loop
* `visualization.py` for plotting and animation
* `demo.py` for example runs
