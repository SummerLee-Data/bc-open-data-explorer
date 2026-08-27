import requests
import pandas as pd

url = "https://catalogue.data.gov.bc.ca/api/3/action/package_search"

params = {
    "rows": 10
}

response = requests.get(url, params=params)

data=response.json()
datasets=data["result"]["results"]

for dataset in datasets:
    print(dataset["title"])