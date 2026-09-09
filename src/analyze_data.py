import pandas as pd
pd.set_option("display.max_colwidth", None)
import matplotlib.pyplot as plt
import ast
df = pd.read_csv("data/bc_datasets.csv")
df["Formats"] = df["Formats"].apply(ast.literal_eval)
df["Tags"] = df["Tags"].apply(ast.literal_eval)
df["Created"] = pd.to_datetime(df["Created"])
df["Modified"] = pd.to_datetime(df["Modified"])

def analyze_organizations(df):
    top_orgs=df["Organization"].value_counts().head(10)
    top_orgs.plot(kind="bar")
    plt.show()

def analyze_modified_dates(df):
    df["Created"]=pd.to_datetime(df["Created"])
    df["Modified"]=pd.to_datetime(df["Modified"])
    modified_by_year=df["Modified"].dt.year.value_counts().sort_index()

    modified_2022=df[df["Modified"].dt.year==2022]
    modified_by_year.plot(kind="bar")
    # 49% of data in 2022 was modified by Treasury Board Staff and Local Government Infrastructure

    treasury_2022=modified_2022[modified_2022["Organization"]=="Treasury Board Staff"]
    # All 388 metadata was modified on the same day 

    LGIF_2022=modified_2022[modified_2022["Organization"]=="Local Government Infrastructure and Finance"]
    print(LGIF_2022["Modified"].dt.date.value_counts())
    LGIF_bulk=LGIF_2022[LGIF_2022["Modified"].dt.date==pd.to_datetime("2022-04-06").date()]
    print(LGIF_bulk["Modified"].min())
    print(LGIF_bulk["Modified"].max())
    # 176 of 178 metadata was modified in about an hour in 2022


def analyze_formats(df):
    print(df["Formats"].head())
    print(df["Formats"].explode().value_counts().head(10))
    print(df["Formats"].apply(lambda x : "csv" in x).value_counts())
    # About 17.5% (587) of datasets provide at least one CSV resource

def analyze_tags(df):
    print(df["Tags"].explode().value_counts().head(10))
    tag_canada=df[df["Tags"].apply(lambda x : "Canada" in x)]
    print(tag_canada["Organization"].value_counts().head(10))
    # tag "Canada" is widely used, but 22.8% of datasets with this tag were from GeoBC.
    
def analyze_created_year(df):
    created_year = df["Created"].dt.year.value_counts()
    print(created_year)
    created_2014 = df[df["Created"].dt.year==2014]
    print(created_2014["Created"].dt.date.value_counts())
    # In 2014, 2,080 of 2,105 datasets were created within just 3 days,
    # suggesting a possible bulk catalogue update or migration.
    not_created_2014 = df[df["Created"].dt.year != 2014]
    print(not_created_2014["Created"].dt.year.value_counts().sort_index())
    created_2019 = df[df["Created"].dt.year == 2019]
    print(created_2019["Created"].dt.date.value_counts())
    print(created_2019["Created"].dt.date.nunique())
    # In comparison, 223 datasets created in 2019 were spread across 85 different days.

def analyze_stale_datasets(df):
    stale_candidates = df[(df["Created"].dt.year<2019) & (df["Modified"].dt.year<2021)]
    print(len(stale_candidates))
    print(stale_candidates["Organization"].value_counts().head(10))
    TBS_stale_candidates = stale_candidates[stale_candidates["Organization"]=="Treasury Board Staff"]
    print(TBS_stale_candidates["Created"].dt.year.value_counts())
    print(TBS_stale_candidates["Title"])
    # Many of the Treasury Board Staff stale candidates are historical financial reports, so old metadata does not necessarily mean the dataset has been abandoned.
    RoadSafetyBC_stale_candidates = stale_candidates[stale_candidates["Organization"]=="RoadSafetyBC"]
    print(RoadSafetyBC_stale_candidates["Created"].dt.year.value_counts())
    print(RoadSafetyBC_stale_candidates["Title"])
    LGIF_stale_candidates = stale_candidates[stale_candidates["Organization"]=="Local Government Infrastructure and Finance"]
    print(LGIF_stale_candidates["Created"].dt.year.value_counts())
    print(LGIF_stale_candidates["Title"].to_string(index=False))
    
    
    # 98 datasets were identified as stale candidates based on creation before 2019 and no metadata modification since 2020.
    # The top three organizations account for 67 candidates, all created in 2014-2015.
analyze_stale_datasets(df)