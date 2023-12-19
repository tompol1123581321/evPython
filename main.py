from functions.functions import functions_list
from algorythms.algorythms import alg_list

print (functions_list)

get_FES =  lambda dimension:2000*dimension
DIMENSIONS = [2,10,30]
LOOP_SIZE = 30
best_results = {}

def main():
    for alg in alg_list:
        for dimension in DIMENSIONS:
            fes = get_FES(dimension)
            for _ in range(LOOP_SIZE):
                result = alg(fes)
                current_best_result = best_results[alg.__name__][dimension]
                if not current_best_result:
                    best_results[alg.__name__][dimension] = alg(fes)
                else:
                    best_results[alg.__name__][dimension] = result if current_best_result < result else current_best_result
    print(best_results)

if __name__ == "__main__":
    main()
