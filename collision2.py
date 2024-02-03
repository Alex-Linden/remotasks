import numpy as np

class GameObject:
    def __init__(self, vel, acc, resist, mass):
        self.position = [0, 0]
        self.velocity = vel
        self.acceleration = acc
        self.resist = resist
        self.mass = mass

    def update_position(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    def collide(self, other):
        # Calculate the relative speed of the two objects
        relative_speed = np.linalg.norm(self.velocity - other.velocity)

        # Compute the angle between the objects and the vector of their relative velocity
        diff = self.position - other.position
        dot_prod = np.dot(diff, self.velocity - other.velocity)
        dot_diff = np.linalg.norm(diff)
        angle = np.arccos(dot_prod / (dot_diff *