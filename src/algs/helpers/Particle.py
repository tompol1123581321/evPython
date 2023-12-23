import numpy as np


class Particle:
    def __init__(self, dim):
        self.position = np.random.rand(dim)
        self.velocity = np.random.rand(dim)
        self.personal_best_position = np.copy(self.position)
        self.personal_best_fitness = float('inf')