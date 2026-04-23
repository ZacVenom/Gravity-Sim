# Gravity Simulation

A real-time 2D gravity simulator built with Pygame, modeling interactions between multiple bodies using Newtonian physics.

## Features

- Real-time N-body gravity simulation
- Interactive object creation with mouse input
- Velocity visualization using direction arrows
- Zoom in/out functionality
- Optional speed display for each object
- Camera follows the first object dynamically

## Physics Model

The simulation is based on Newton’s Law of Universal Gravitation:

F = G * (m1 * m2) / r²

Each frame:
- Gravitational forces between all object pairs are calculated
- Velocities are updated based on acceleration
- Positions are updated accordingly

This results in:
- Orbital motion
- Chaotic multi-body systems
- Emergent behavior from simple rules

## Controls

- **UP / DOWN arrows** → Zoom in / out  
- **Q** → Add a new object:
  - First press: choose position
  - Second press: set velocity (based on mouse drag)  
- Objects display velocity direction as arrows  
- (Optional) Speed values shown on screen

## ▶How to run

1. Install dependencies:
   ```bash
   pip install pygame
2. Run the example:
   ```bash
   python3 example.py  
