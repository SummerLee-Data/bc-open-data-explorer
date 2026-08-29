import requests
import pandas as pd

url = "https://catalogue.data.gov.bc.ca/api/3/action/package_search"

params = {
    "rows": 10
}

response = requests.get(url, params=params)

data=response.json()
datasets=data["result"]["results"]

rows=[]
for dataset in datasets:

    tags=[]
    for tag in dataset["tags"]:
        tags.append(tag["name"])
        

    formats=[]
    for resource in dataset["resources"]:
        formats.append(resource["format"])


    row = {
        "Title":dataset["title"],
        "Organization":dataset["organization"]["title"],
        "Created":dataset["metadata_created"],
        "Modified":dataset["metadata_modified"],
        "Formats":formats,
        "Tags":tags
    }
    
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("data/bc_datasets.csv", index=False)