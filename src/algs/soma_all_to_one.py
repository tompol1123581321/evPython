import math
import numpy as np


from src.algs.helpers.reflectionHandler import handle_possible_collision
from src.algs.helpers.contants import MAX,MIN

def soma_all_to_one_alg(obj_func, dim, num_iterations):
    STEPS = 0.11
    population_size = 10 if dim == 2 else 20 if dim == 10 else 50


    allowed_fes_calls = num_iterations
    def call_obj_function_with_limitation(pos): 
        nonlocal allowed_fes_calls
        allowed_fes_calls -= 1 
        return obj_func(pos)


    population = np.random.uniform(low=MIN, high=MAX, size=(population_size, dim))

    while 0 < allowed_fes_calls:
        leader_index = np.argmin([call_obj_function_with_limitation(p) for p in population])
        leader_position = np.copy(population[leader_index]) 
        best_positions = np.copy(population)

        for i in range(len(population)):
            population[i] = migrate_to_leader(population[i], leader_position, STEPS)

            current_fitness = call_obj_function_with_limitation(population[i])
            best_fitness = call_obj_function_with_limitation(best_positions[i])

            if current_fitness < best_fitness:
                best_positions[i] = np.copy(population[i])

        population = np.copy(best_positions)

    best_index = np.argmin([call_obj_function_with_limitation(p) for p in population])
    best_vector = np.copy(population[best_index])
    best_fitness = call_obj_function_with_limitation(best_vector)

    return best_fitness


def migrate_to_leader(individual, leader_position, step_size):
    direction = leader_position - individual
    distance = np.linalg.norm(direction)

    if distance > 0: 
        velocity = step_size * direction / distance
        individual = handle_possible_collision(individual,velocity,MIN,MAX)

    return individual