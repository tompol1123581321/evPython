import random
import numpy as np
from src.algs.helpers.reflectionHandler import handle_possible_collision
from src.algs.helpers.contants import MIN,MAX


from  src.algs.helpers.Particle import Particle



def pso_alg(obj_func, dim, num_iterations):
    w = 0.7298
    c1 = 1.49618
    c2 = c1
    population_size = 10 if dim == 10 else 20 if dim == 10 else 50
    particles = [Particle(dim) for _ in range(population_size)]
    global_best_position = None
    global_best_fitness = float('inf')

    for _ in range(num_iterations):  
        for particle in particles:
            fitness = obj_func(particle.position)

            if fitness < particle.personal_best_fitness:
                particle.personal_best_fitness = fitness
                particle.personal_best_position = np.copy(particle.position)

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = np.copy(particle.position)

            r1, r2 = random.random(), random.random()
            particle.velocity = (w * particle.velocity +
                                 c1 * r1 * (particle.personal_best_position - particle.position) +
                                 c2 * r2 * (global_best_position - particle.position))
            
            particle.position = handle_possible_collision(particle.position,particle.velocity,MIN,MAX)

    return global_best_fitness
