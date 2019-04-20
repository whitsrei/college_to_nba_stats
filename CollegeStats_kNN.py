#from tabulate import tabulate
import operator
import random
import math
import numpy as np

def main():
    #fxn that calls KNN-self-done

    start_table = get_table('firstRoundPicks_withCollegeStats.csv')
    headers = start_table[0]
    table = start_table[1:]

    find_stat_correlation_to_NBA_PTS(table, headers)
        
    knn(table, headers)

def get_table(filename):
    table = []
    infile = open(filename)
    lines = infile.readlines()
    
    i = 0
    for line in lines:
        add_it = True
        line = line.strip()
        line = line.strip('\n')
        values = line.split(",")
       
        #this is only grabbing columns that are completely filled in
        if len(values) > 27:        
            for val in values:
                #Get rid of columns with NA in them
                if val == 'NA':
                    add_it = False
            if add_it:
                
                #player - 6
                #pick - 4
                #MP - 31
                #FG - 32
                #FG% - 34
                #3p - 38
                #3pt% - 40
                #FT - 41
                #PTS - 52
                #SOS - 54
                #NBA PTS - 15
                
                to_add = []
                to_add.append(values[6])
                to_add.append(values[4])
                to_add.append(values[31])
                to_add.append(values[32])
                to_add.append(values[34])
                to_add.append(values[38])
                if values[40] == '':
                    to_add.append(0.0)
                else:
                    to_add.append(values[40])
                to_add.append(values[41])
                to_add.append(values[52])
                to_add.append(values[54])
                to_add.append(values[15])
                convert_to_numeric(to_add)
                table.append(to_add)
    infile.close()
    return table

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


def knn_guess(train_set, test_set, k_val):
    '''
    classifier using knn given a test set, train set and k value
    '''
    
    init_len = len(train_set)
    
    right = 0
    wrong = 0

    for row in train_set:
        row.append(compute_distances(row, test_set, train_set))  

    k = k_val
    
    length_of_rows = len(train_set[0])
    train_set.sort(key=operator.itemgetter(length_of_rows-1))

    top_k = train_set[:k]

    # calculate the averages from the nearest neighbors
    
    avg_list = [[] for i in range(len(top_k[0]))]
    for row in top_k:
        for i in range(1,len(row)):
            avg_list[i].append(float(row[i]))
    
    avg_list = avg_list[1:]
    avgs = [np.mean(i) for i in avg_list]
    
    for row in train_set:
        row.pop()
    
    return avgs

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

def knn(table, headers):    
    folds = k_fold(table)
    print("---------------------")
    print("Self-Coded: KNN")
    print("---------------------")

    for i in range(len(folds)):
        train_set = []
        for x in folds:
            if x != folds[i]:
                for item in x:
                    train_set.append(item)
        for j in folds[i]:
            my_guess = knn_guess(train_set, j, 10)
            print("----------------------------------------")
            print("Player -> ", j[0])
            for i in range(1, len(headers)):
                print(headers[i] + " -> " + "%.2f" % my_guess[i-1])
            print("This is the weird value at the end... i think it might be left over from adding values to the end: " + str(my_guess[-1]))
            print("----------------------------------------")

def find_stat_correlation_to_NBA_PTS(table, headers):
    NBA_PTS = get_column(table, 10)
    for i in range(1, len(headers)-1):
        cur_column = get_column(table, i)
        vals = np.corrcoef(cur_column, NBA_PTS)
        r = str(vals[0][-1])
        print (headers[i] + " correlation coefficent = " + r)

if __name__ == "__main__":
    main()