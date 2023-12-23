import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from src.algs.alg_list import alg_list
from src.functions.functions import functions_list

get_FES = lambda dimension: 2000 * dimension
DIMENSIONS = [2, 10, 30]
LOOP_SIZE = 30
results = {}

def run_algorithm(obj_func, dimension, alg, fes):
    result = alg(obj_func, dimension, fes)
    return result

def update_results(dim_name, obj_func_name, alg_name, result):
    if dim_name not in results:
        results[dim_name] = {}
    if obj_func_name not in results[dim_name]:
        results[dim_name][obj_func_name] = {}
    if alg_name not in results[dim_name][obj_func_name]:
        results[dim_name][obj_func_name][alg_name] = []
    print("exec",dim_name, obj_func_name, alg_name, result)
    results[dim_name][obj_func_name][alg_name].append(result)

def save_results_to_file(filename):
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)
    print(f"Results saved to {filename}")

def main():
    with ProcessPoolExecutor() as executor:
        futures = []
        for dimension in DIMENSIONS:
            dim_name = str(dimension)
            for i, obj_func in enumerate(functions_list):
                obj_func_name = obj_func.__name__
                for alg in alg_list:
                    alg_name = alg.__name__
                    fes = get_FES(dimension)
                    for _ in range(LOOP_SIZE):
                        future = executor.submit(
                            update_results,
                            dim_name,
                            obj_func_name,
                            alg_name,
                            run_algorithm(obj_func, dimension, alg, fes),
                        )
                        futures.append(future)

        print("Waiting for all tasks to complete...")
        for future in as_completed(futures):
            future.result()
           
    print(results)
    save_results_to_file("results.json")

if __name__ == "__main__":
    main()

