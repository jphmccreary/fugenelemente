import pandas as pd
import dill as pickle
from constants import FUGENELEMENTE_FREQUENCY_ORDER
import numpy as np
from sklearn.linear_model import LinearRegression
from collections import defaultdict

# results_file = open('results/test.csv')
# results = pd.read_csv(results_file)
# results_file.close()

results = pickle.load(open('dumps/results', 'rb'))

# remove first column
for row in results:
    row.pop(0)
# remove first row
results.pop(0)
# convert to numbers
for row in results:
    for i, col in enumerate(row):
        row[i] = float(col)

stats = defaultdict(float)
for fn in FUGENELEMENTE_FREQUENCY_ORDER:
    stats[fn] = {
        'ratios': [],
    }

for fn_index, fn in enumerate(stats):
    for year_index, year in enumerate(range(1995, 2023)):
        pass
        stats[fn]['ratios'].append(results[year_index][fn_index])

    x = np.array(range(1995, 2023)).reshape((-1, 1))
    y = np.array(stats[fn]['ratios'])
    model = LinearRegression()
    model.fit(x, y)
    stats[fn]['score'] = model.score(x, y)
    stats[fn]['intercept'] = model.intercept_
    stats[fn]['slope'] = model.coef_[0]
    stats[fn]['start_pred'] = model.predict([[1995]])[0]
    stats[fn]['end_pred'] = model.predict([[2022]])[0]
    stats[fn]['delta'] = stats[fn]['end_pred'] - stats[fn]['start_pred']

def avg(l):
    return sum(l) / len(l)

for fn in stats:
    stats[fn]['avg'] = avg(stats[fn]['ratios'])
    stats[fn]['proportional_slope'] = stats[fn]['slope'] / stats[fn]['avg']

# create top row
output_stats = [['Fugenelement',
                 'Start Proportion',
                 'End Proportion',
                 '27-Year Delta',
                 'Average Proportion',
                 'Average Change/Year',
                 'Proportional Average Change/Year',
                 'R^2',
                 ]]

stat_sort_order = sorted(stats, key=lambda x: stats[x]["delta"], reverse=True)
sorted_stats = {}
for stat in stat_sort_order:
    sorted_stats[stat] = stats[stat]
for fn in stats:
    fni = stats[fn]
    # output_stats.append([f'{fn}',
    #                     f'{fni["slope"][0] * 100}%',
    #                     f'+{fni["delta"] * 100}%' if fni['delta'] > 0 else f'{fni["delta"]}%',
    #                     f'{fni["score"]}'])
    output_stats.append([f'{fn}',
                         f'{fni["start_pred"]}',
                         f'{fni["end_pred"]}',
                         f'{fni["delta"]}',
                         f'{fni["avg"]}',
                         f'{fni["slope"]}',
                         f'{fni["proportional_slope"]}',
                         f'{fni["score"]}'
                        ])
csv_string = ''
for line in output_stats:
    csv_string += ','.join(line) + '\n'

with open('results/stats.csv', 'w') as outfile:
    outfile.write(csv_string)




