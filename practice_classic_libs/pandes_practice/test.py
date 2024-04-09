import pandas as pd
import json
import requests


# response = requests.get('https://www.w3schools.com/python/pandas/data.js')
# data = json.dumps(response.json())
# with open('data.json', 'w') as f:
#     json.dump(response.json(), f, indent=4)

# with open('data.json') as f:
#     data = json.load(f)
# data = pd.read_json('data.json')
# data = pd.read_csv('100 Sales Records.csv')
from oooo import data
pd.DataFrame(data).to_csv('for_data.csv', index=False)

# print(data)
# print(res.to_string())
