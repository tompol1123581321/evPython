import json
from statistics import mean
import pandas as pd
from scipy.stats import rankdata

def read_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def normalize_ranks(input_list):
    values = [item['value'] for item in input_list]
    ranks = rankdata(values)

    for item, rank in zip(input_list, ranks):
        item['rank'] = rank

    # Normalize the ranks to a sum of 15

    return input_list

def transform_results_to_means(data):
    result = {}
    for dim_key in data:
        dim_table_data = data[dim_key]
        result[dim_key] = {}
        for func_key in dim_table_data:
            result[dim_key][func_key] = {}
            function_data = dim_table_data[func_key]
            list_to_sort = []
            for alg_key in function_data:
                avg = mean(function_data[alg_key])
                list_to_sort.append({'name': alg_key, 'value': avg})
            
            sorted_ranks = sorted(list_to_sort, key=lambda x: x['value'])
            result[dim_key][func_key] = normalize_ranks(sorted_ranks)
            
    return result

def flatten_data(dimension, data):
    dimension_data = data[dimension]
    flattened_data = {function: {} for function in dimension_data}
    
    for function, rankings in dimension_data.items():
        for entry in rankings:
            name = entry['name']
            rank = entry['rank']
            flattened_data[function][name] = rank
    
    return flattened_data

def save_and_display_table(df, dimension):
    # Add a row for the sum of each column
    df.loc['Sum'] = df.sum()
    
    # Save the table to a CSV file
    file_name = f'table_dimension_{dimension}.csv'
    df.to_csv(file_name)
    
    # Display the table
    print(f'\nTable for Dimension {dimension}:\n')
    print(df)

# Specify the file path
file_path = 'results.json'

# Read the data from the file
data = read_data(file_path)

# Transform the data and generate tables for each dimension
for dimension in transform_results_to_means(data):
    dimension_data = flatten_data(dimension, transform_results_to_means(data))
    df = pd.DataFrame(dimension_data).transpose()
    save_and_display_table(df, dimension)
