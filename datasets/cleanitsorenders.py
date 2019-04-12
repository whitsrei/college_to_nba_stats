import csv

def get_table(filename):
    table = []
    infile = open(filename)
    lines = infile.readlines()
    for line in lines:
        yup = True
        line = line.strip()
        line = line.strip('\n')
        values = line.split(",")
        table.append(values)
    infile.close()
    return table

def main():
    table = get_table('firstRoundPicks_withCollegeStats.csv')    
    for row in table:
        while len(row) < 58:
            row.append('NA')
    









main()
