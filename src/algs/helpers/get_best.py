import numpy as np


def get_best_from_population(objective_function, population):
    fitness_values = np.array([objective_function(candidate.position) for candidate in population])
    best_index = np.argmin(fitness_values)
    best_candidate = population[best_index]
    best_candidate.personal_best_fitness = fitness_values[best_index]
    return best_candidate, best_index
