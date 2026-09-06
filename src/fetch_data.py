import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://catalogue.data.gov.bc.ca/api/3/action/package_search"

all_datasets=[]

for start in range(0,3400,100):
    params = {
        "rows": 100,
        "start": start
    }

    response = requests.get(url, params=params)

    data=response.json()
    datasets=data["result"]["results"]
    all_datasets.extend(datasets)

rows=[]
for dataset in all_datasets:

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
top_orgs=df["Organization"].value_counts().head(10)
top_orgs.plot(kind="bar")
plt.show()
