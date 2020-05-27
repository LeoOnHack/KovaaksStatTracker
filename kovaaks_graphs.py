from os import listdir, mkdir
from datetime import datetime
import matplotlib.pyplot as plt
import csv

dir = input("Enter your Kovaak's stats directory: \n")

def csv_file(name):
    if name[-4:] == '.csv':
        return True
    else:
        return False
    
files = filter(csv_file, listdir(dir))

scenario_scores = {}

for f in files:
    with open(dir + f, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if any(row) and row[0] == 'Score:':
                scenario = f[:f.find('Challenge') - 3]
                date = f[f.find('Challenge') + 12:-19]
                score = float(row[1])
                
                if scenario in scenario_scores:
                    scenario_scores[scenario].append([date, score])
                else:
                    scenario_scores[scenario] = [[date, score]]

graph_dir = dir + 'graphs/'
try:
    mkdir(graph_dir)
except FileExistsError:
    pass

for s in scenario_scores:
    sorted_s = sorted(scenario_scores[s], key=lambda k: [k[1], k[0]])
    dates = [datetime.strptime(x[0], '%Y.%M.%d').date() for x in sorted_s]
    scores = [x[1] for x in sorted_s]
    plt.scatter(dates, scores)
    plt.title(s)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(graph_dir + s + '.png')
    plt.close()