import math
import numpy as np
import random

def get_column(table, column_index):
    column = []
    for row in table:
        if row[column_index] != 'NA':
            column.append(row[column_index])
    return column

def compute_distances(v1,v2,table):
    assert(len(v1) == len(v2))

    dist = 0
    for i in range(1, len(v1)-1):
        Min = min(get_column(table, i))
        Max = max(get_column(table, i))
        v1_N = normalize(v1[i], Min, Max)
        v2_N = normalize(v2[i], Min, Max)
    
        dist += (v1_N- v2_N) ** 2
    return math.sqrt(dist)

def normalize(x, Min, Max):
    '''
    normalizes data before distance calculations
    '''
    normalized = ((x - Min) / (Max - Min)) * 1.0
    return normalized

def k_fold(table):
    randomized = table[:]
    n = len(randomized)

    for i in range(n):
        rand_index = random.randrange(0,n)
        randomized[i], randomized[rand_index] = randomized[rand_index], randomized[i]


    folds = [[] for i in range(10)]
    x = 0
    for i in range(len(randomized)):
        if x > 9:
            x = 0
        folds[x].append(randomized[i])
        x += 1
    return folds

def convert_to_numeric(values):
    '''
    converts values read from a file into correct types
    '''
    for i in range(len(values)):
        try:
            #converts numerical values from strings to floats
            numeric_val = float(values[i])
            values[i] = numeric_val
        except ValueError:
            values[i] = values[i].strip('\"')
