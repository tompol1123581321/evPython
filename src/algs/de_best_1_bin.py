import random
import numpy as np
from src.algs.helpers.contants import MIN,MAX
from src.algs.helpers.reflectionHandler import handle_possible_collision

from src.algs.helpers.get_best import get_best_from_population
from src.algs.helpers.Particle import Particle


def de_best_one_alg(obj_func, dim, num_iterations):
    F: float = 0.5
    CR: float = 0.9

    population_size = 10 if dim == 2 else 20 if dim == 10 else 50


    allowed_fes_calls = num_iterations
    def call_obj_function_with_limitation(pos): 
        nonlocal allowed_fes_calls
        allowed_fes_calls -= 1 
        return obj_func(pos)

    population = np.array([Particle(dim) for _ in range(population_size)])
    new_population = population.copy()
    global_best_fitness = float('inf')

    best_one, best_index = get_best_from_population(call_obj_function_with_limitation, population)
    fit = best_one.personal_best_fitness
    
    while allowed_fes_calls > 0:
        for active in range(len(population)):
            if active == best_index: continue

            population[active].personal_best_fitness = call_obj_function_with_limitation(population[active].position)

            can_indx = np.array(range(len(population)))
            can_indx = np.delete(can_indx, [best_index, active])
            b, c = population[np.random.choice(can_indx, 2, replace=False)]
            mutation_vector = handle_possible_collision(best_one.position.copy(),  F * (b.position.copy() - c.position.copy()),MIN,MAX)

            offspring = Particle(dim)
            R: int = random.choice(range(0, dim))
            for i in range(dim):
                if random.uniform(0, 1) < CR or i == R:
                    offspring.position[i] = mutation_vector[i]
                else:
                    offspring.position[i] = population[active].position[i]

            offspring.personal_best_fitness = call_obj_function_with_limitation(offspring.position)

            if offspring.personal_best_fitness <= population[active].personal_best_fitness:
                new_population[active] = offspring
                if offspring.personal_best_fitness < best_one.personal_best_fitness:
                    best_index = active
                    fit = offspring.personal_best_fitness

        population = new_population

        best_one, best_index = get_best_from_population(call_obj_function_with_limitation, population)
        best_one.personal_best_fitness = global_best_fitness = fit

    return global_best_fitness


