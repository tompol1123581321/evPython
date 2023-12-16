import numpy as np
from math import cos, sin, exp, sqrt, pi

def ackley(x):
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * np.sum(x**2))) - np.exp(0.5 * (np.cos(2 * pi * x[0]) + np.cos(2 * pi * x[1]))) + np.e + 20

def sphere(x):
    return np.sum((x - 5)**2) + np.sum(np.cos(x - 5))

def rosenbrock(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

def griewank(x):
    return 1 + np.sum(x**2) / 4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))

def michalewicz(x, m=10):
    return -np.sum(np.sin(x) * np.sin(np.arange(1, len(x) + 1) * x**2 / pi)**(2 * m))

def rastrigin(x):
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * pi * x))

def schwefel(x):
    return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

def bohachevsky(x):
    return np.sum(x**2 + 2 * x[1:]**2 - 0.3 * np.cos(3 * pi * x[:-1]) - 0.4 * np.cos(4 * pi * x[1:]) + 0.7)

def zakharov(x):
    return np.sum(x**2) + (0.5 * np.sum(np.arange(1, len(x) + 1) * x))**2 + (0.5 * np.sum(np.arange(1, len(x) + 1) * x**2))**4

def styblinski_tang(x):
    return 0.5 * np.sum(x**4 - 16 * x**2 + 5 * x)

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def easom(x):
    return -cos(x[0]) * cos(x[1]) * exp(-((x[0] - pi)**2 + (x[1] - pi)**2))

def schaffer_n2(x):
    num = sin(x[0]**2 + x[1]**2)**2 - 0.5
    denom = (1 + 0.001 * (x[0]**2 + x[1]**2))**2
    return 0.5 + num / denom

def schaffer_n4(x):
    num = cos(sin(np.abs(x[0]**2 - x[1]**2))) - 0.5
    denom = (1 + 0.001 * (x[0]**2 + x[1]**2))**2
    return 0.5 + num / denom

def six_hump_camel(x):
    return (4 - 2.1*x[0]**2 + (x[0]**4)/3) * x[0]**2 + x[0]*x[1] + (-4 + 4*x[1]**2) * x[1]**2

def schwefel_problem_2_21(x):
    return np.sum(np.abs(x) * np.sin(np.sqrt(np.abs(x))))

def rotated_hyper_ellipsoid(x):
    return np.sum(np.cumsum(x**2))

def generalized_penalized_1(x):
    term1 = (np.sin(3 * pi * x[0]) / (3 * pi))**2
    term2 = np.sum(((x[:-1] - 1) / (1 + 0.1 * x[:-1]**2))**2)
    term3 = (np.sin(3 * pi * x[-1]) / (3 * pi))**2
    return 0.5 * (term1 + term2 + term3)

def generalized_penalized_2(x):
    term1 = (np.sin(3 * pi * x[0]) / (3 * pi))**2
    term2 = np.sum(((x[:-1] - 1) / (1 + 0.1 * x[:-1]**2))**2)
    term3 = (np.sin(3 * pi * x[-1]) / (3 * pi))**2
    term4 = np.sum(u(x, 5, 100, 4) + v(x, 5, 100, 4))
    return 0.5 * (term1 + term2 + term3) + 0.5 * term4

def modified_schwefel_problem_1_2(x):
    term1 = np.sum((x)**2)
    term2 = np.sum(np.sin(np.sqrt(np.abs(x))) / np.sqrt(np.abs(x)))
    return term1 + term2

def pinter_function_8(x):
    term1 = np.sum(10**(4 * np.arange(len(x))) * (x - x[0]**2 / x))
    term2 = np.sum((1 - x)**2)
    return term1 + term2

def alpine_function(x):
    return np.sum(np.abs(x * np.sin(x) + 0.1 * x))

def quartic_function(x):
    return np.sum(np.arange(1, len(x) + 1) * x**4) + np.random.uniform(-0.1, 0.1)

def sum_of_different_powers(x):
    return np.sum(np.abs(x)**(np.arange(1, len(x) + 1) + 1))

def salomon_function(x):
    return 1 - cos(2 * pi * sqrt(np.sum(x**2))) + 0.1 * sqrt(np.sum(x**2))

def u(x, a, k, m):
    return np.where(x > a, k * (x - a)**m, 0)

def v(x, a, k, m):
    return np.where(x < -a, k * (-x - a)**m, 0)


def generate_mathematical_function_info(fun):
    return {"name":fun.__name__,"evaluate":fun}

# # Example usage
# n_dimensions = 2
# x_example = np.random.uniform(-100, 100, n_dimensions)

# print("Ackley:", ackley(x_example))
# print("Sphere:", sphere(x_example))
# print("Rosenbrock:", rosenbrock(x_example))
# ... (test other functions as needed)
