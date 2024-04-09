import json


with open('techcrunch.csv') as f:
    data = (line for line in f)
    columns = next(data).strip().split(',')
    res = {}
    for line in data:
        info = line.strip().split(',')
        temporary = dict(zip(columns, info))
        if temporary['round'] == 'c':
            name = temporary.pop('company')
            res[name] = temporary

with open('for_data.json', 'w') as f:
    json.dump(res, f, indent=4)

total_profit = 0
for value in res.values():
    profit = int(value['raisedAmt'])
    total_profit += profit

print(total_profit)
