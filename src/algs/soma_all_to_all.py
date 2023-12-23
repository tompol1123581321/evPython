import math
import numpy as np


from  src.algs.helpers.reflectionHandler import handle_possible_collision
from  src.algs.helpers.contants import MAX,MIN

def soma_all_to_all_alg(obj_func, dim, num_iterations):
    PRT = 0.7
    PL = 3
    STEPS = 0.11
    population_size = 10 if dim == 2 else 20 if dim == 10 else 50

    global_best_fitness = float('inf')

    allowed_fes_calls = num_iterations
    def call_obj_function_with_limitation(pos): 
        nonlocal allowed_fes_calls
        allowed_fes_calls -= 1 
        return obj_func(pos)



    population = np.random.uniform(low=MIN, high=MAX, size=(population_size, dim))
    new_population = np.copy(population)

    while allowed_fes_calls > 0:
        for active in range(len(population)):
            act_fit = call_obj_function_with_limitation(population[active])

            for second in range(len(population)):
                if active == second:
                    continue

                current_position = population[active]
                best_pos = current_position
                best_val = float('inf')
                for _ in range(math.ceil(PL/STEPS)):
                    direction = np.random.choice([0, 1], size=dim, p=[1 - PRT, PRT])
                    new_position = current_position + (population[second] - population[active]) * STEPS * direction
                    current_position = handle_possible_collision(new_position, (population[second] - population[active]) * STEPS * direction,MIN,MAX)
                    val = call_obj_function_with_limitation(current_position)
                    if val < best_val:
                        best_val = val
                        best_pos = current_position
                    

            if best_val < act_fit:
                new_population[active] = np.copy(best_pos)

            if best_val < global_best_fitness:
                global_best_fitness = best_val

        population = np.copy(new_population)
    return global_best_fitness
