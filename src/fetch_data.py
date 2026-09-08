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
# top_orgs=df["Organization"].value_counts().head(10)
# top_orgs.plot(kind="bar")
# ##plt.show()

# df["Created"]=pd.to_datetime(df["Created"])
# df["Modified"]=pd.to_datetime(df["Modified"])
# modified_by_year=df["Modified"].dt.year.value_counts().sort_index()

# modified_2022=df[df["Modified"].dt.year==2022]
# modified_by_year.plot(kind="bar")
# 49% of data in 2022 was modified by Treasury Board Staff and Local Government Infrastructure

# treasury_2022=modified_2022[modified_2022["Organization"]=="Treasury Board Staff"]
# All 388 metadata was modified on the same day 

# LGIF_2022=modified_2022[modified_2022["Organization"]=="Local Government Infrastructure and Finance"]
# ##print(LGIF_2022["Modified"].dt.date.value_counts())
# LGIF_bulk=LGIF_2022[LGIF_2022["Modified"].dt.date==pd.to_datetime("2022-04-06").date()]
# print(LGIF_bulk["Modified"].min())
# print(LGIF_bulk["Modified"].max())
# 176 of 178 metadata was modified in about an hour in 2022

# print(df["Formats"].head())
# print(df["Formats"].explode().value_counts().head(10))
# print(df["Formats"].apply(lambda x : "csv" in x).value_counts())
# About 17.5%(587) of datasets are providing more than one csv format

#print(df["Tags"].explode().value_counts().head(10))
tag_canada=df[df["Tags"].apply(lambda x : "Canada" in x)]
print(tag_canada["Organization"].value_counts().head(10))
# tag "Canada" is widely used, but 22.8% of datasets with this tag were from GeoBC.