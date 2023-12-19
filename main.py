from src.algs.alg_list import alg_list

get_FES =  lambda dimension:2000*dimension
DIMENSIONS = [2,10,30]
LOOP_SIZE = 30
best_results = {}

def main():
    for alg in alg_list:
        alg_name = alg.__name__
        if alg_name not in best_results:
            best_results[alg_name] = {}
        for dimension in DIMENSIONS:
            fes = get_FES(dimension)
            for _ in range(LOOP_SIZE):
                result = alg()
                current_best_result =  best_results[alg_name][dimension] if alg_name in best_results and dimension in best_results[alg_name] else None
                if not current_best_result:
                    best_results[alg_name][dimension] = result
                else:
                    best_results[alg_name][dimension] = result if current_best_result < result else current_best_result
    print(best_results)

if __name__ == "__main__":
    main()
