import requests
import json


def reader(d: dict):
    for key, value in d.items():
        print('{:<29} ---->  {}'.format(key, value))


url = 'https://api.github.com/search/repositories'
response = requests.get(url, params={})
response = requests.get(url, params={'q': 'requests+language:python'})
# response.raise_for_status()
json_data = response.json()
repository = json_data['items'][0]

print(repository['name'])
print(repository['description'])
with open('file.json', 'w') as f:
    json.dump(json_data, f, indent=5)
