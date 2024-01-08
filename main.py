import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Manager
from multiprocessing.managers import DictProxy, ListProxy

from src.algs.alg_list import alg_list
from src.functions.functions import functions_list

get_FES = lambda dimension: 2000 * dimension
DIMENSIONS = [2,10,30]
LOOP_SIZE = 30
manager = Manager()
results = manager.dict()

def convert_manager_dict_to_dict(manager_dict):
    # Convert manager.dict() to a regular dictionary recursively
    result_dict = {}
    for key, value in manager_dict.items():
        if type(value) == DictProxy:
            result_dict[key] = convert_manager_dict_to_dict(value)
        elif type(value) == ListProxy:
            result_dict[key] = convert_manager_list_to_list(value)
        else:
            result_dict[key] = value
    return result_dict

def convert_manager_list_to_list(manager_list, replace_infinity_with=None):
    # Convert manager.list() to a regular list recursively
    result_list = []
    for item in manager_list:
        if type(item) == ListProxy:
            result_list.append(convert_manager_list_to_list(item, replace_infinity_with))
        elif type(item) == DictProxy:
            result_list.append(convert_manager_dict_to_dict(item))
        elif item == float('inf'):
            result_list.append(replace_infinity_with)  # Replace infinity with the specified value
        else:
            result_list.append(item)
    return result_list



def run_algorithm(obj_func, dimension, alg, fes):
    result = alg(obj_func, dimension, fes)
    return result

def update_results(dim_name, obj_func_name, alg_name, result):
    print(alg_name,result)
    if dim_name not in results:
        results[dim_name] = manager.dict()
    if obj_func_name not in results[dim_name]:
        results[dim_name][obj_func_name] = manager.dict()
    if alg_name not in results[dim_name][obj_func_name]:
        results[dim_name][obj_func_name][alg_name] = manager.list()
    print("exec", dim_name, obj_func_name, alg_name, result)
    results[dim_name][obj_func_name][alg_name].append(result)

def save_results_to_file(filename):
    result_as_dict = convert_manager_dict_to_dict(results)
    print(result_as_dict)
    with open(filename, "w") as file:
        json.dump(result_as_dict, file, indent=4)
    # print(f"Results saved to {filename}")

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
    save_results_to_file("results2.json")

if __name__ == "__main__":
    main()
