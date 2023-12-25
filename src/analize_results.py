import json
from statistics import mean 
import pandas as pd

file = open('results.json')
data = json.load(file)

def transform_data(data):
    # Extract values from the dictionaries
    values = [list(item.values())[0] for item in data]

    # Sort values and create a dictionary with original values as keys and ranks as values
    sorted_values_with_rank = {value: i + 1 for i, value in enumerate(sorted(set(values)))}

    # Transform the original data by assigning ranks
    transformed_data = [{'name': list(item.keys())[0], 'rank': sorted_values_with_rank[list(item.values())[0]]} for item in data]

    return transformed_data

# Example usage:



def transform_results_to_means():
    result = {}
    for dim_key in data:
        dim_table_data = data[dim_key]
        result[dim_key] = {}
        for func_key in dim_table_data:
            result[dim_key][func_key]={}
            function_data = dim_table_data[func_key]
            list_to_sort = []
            for alg_key in function_data:
                avg = mean(function_data[alg_key])
                # result[dim_key][func_key][alg_key] = avg
                list_to_sort.append({alg_key:avg})
            ranked_means =  transform_data(list_to_sort)
            result[dim_key][func_key]= ranked_means
    return result

def flatten_data(dimension):
    data = transform_results_to_means()[dimension]
    flattened_data = {function: {} for function in data}
    
    for function, rankings in data.items():
        for entry in rankings:
            name = entry['name']
            rank = entry['rank']
            flattened_data[function][name] = rank
    
    return flattened_data

# Generate tables for each dimension
for dimension in transform_results_to_means():
    flattened_data = flatten_data(dimension)
    df = pd.DataFrame(flattened_data).transpose()
    
    # Add a row for the sum of each column
    df.loc['Sum'] = df.sum()
    
    # Save the table to a CSV file (you can modify the file name accordingly)
    df.to_csv(f'table_dimension_{dimension}.csv')
    
    # Display the table
    print(f'\nTable for Dimension {dimension}:\n')
    print(df)

            

            
            


