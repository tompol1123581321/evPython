from src.algs.alg_list import alg_list
from src.functions.functions import functions_list

get_FES =  lambda dimension:2000*dimension
DIMENSIONS = [2,10,30]
LOOP_SIZE = 30
best_results = {}

def main():
    for obj_func in functions_list:
        obj_func_name = obj_func.__name__   
        if obj_func_name not in best_results:
            best_results[obj_func_name] = {}
        for alg in alg_list:
            alg_name = alg.__name__
            if alg_name not in best_results[obj_func_name]:
                best_results[obj_func_name][alg_name] = {}
            for dimension in DIMENSIONS:
                fes = get_FES(dimension)
                for _ in range(LOOP_SIZE):
                    result = alg(obj_func,dimension,fes)
                    print(result,alg_name,dimension,obj_func_name)
                    current_best_result =  best_results[obj_func_name][alg_name][dimension] if alg_name in best_results[obj_func_name] and dimension in best_results[obj_func_name][alg_name] else None
                    if not current_best_result:
                        best_results[obj_func_name][alg_name][dimension] = result
                    else:
                        best_results[obj_func_name][alg_name][dimension] = result if current_best_result < result else current_best_result
    print(best_results)

if __name__ == "__main__":
    main()
