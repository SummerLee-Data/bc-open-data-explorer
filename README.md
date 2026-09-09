# BC Open Data Explorer

This project uses the BC Data Catalogue API to explore open datasets published by the Government of British Columbia.

I wanted to work with a real API and a dataset that was large enough to practice data collection, cleaning, and basic exploratory analysis. I was also curious about what kinds of datasets the BC government publishes and how easy they are to actually use.

## Data

I collected metadata from the BC Data Catalogue using its CKAN API. There were 3,356 datasets when I pulled the data.

The API only returns a limited number of results at once, so I fetched the datasets in batches of 100.

For each dataset, I kept:

* Title
* Organization
* Created date
* Modified date
* Formats
* Tags

Some of the API response was nested, especially formats and tags, so I had to extract the information I wanted before putting everything into a pandas DataFrame.

The processed data is saved in `data/bc_datasets.csv`.

## What I found

### Organizations

First, I looked at which organizations had the most datasets.

| Organization                                  | Datasets |
| --------------------------------------------- | -------- |
| Treasury Board Staff                          |      443 |
| GeoBC Branch                                  |      399 |
| Local Government Infrastructure and Finance   |      198 |
| Knowledge Management                          |      116 |
| BC Stats                                      |       96 |
| Regional Operations - Thompson Okanagan       |       71 |
| GeoBC - Geospatial Services                   |       69 |
| Forest Tenures Branch                         |       65 |
| Forest Science, Planning and Practices Branch |       65 |
| Environmental Monitoring and Analysis Branch  |       64 |

Treasury Board Staff and GeoBC Branch had the most by a fairly large margin.

### Formats

I also looked at the formats available for each dataset.

| Format      | Count |
| ----------- | ----- |
| CSV         | 1,204 |
| multiple    | 1,149 |
| XLSX        | 1,015 |
| WMS         |   886 |
| KML         |   883 |
| other       |   499 |
| Oracle SDE  |   461 |
| PDF         |   348 |
| XLS         |   322 |
| ArcGIS REST |   219 |

These numbers count individual resources, not datasets. One dataset can have multiple resources, including multiple resources with the same format.

For example, CSV appeared 1,204 times, but only **587 of the 3,356 datasets** had at least one CSV resource. That's about **17.5%** of the datasets.

### Tags

The most common tags were:

| Tag         | Count |
| ----------- | ----: |
| Canada      |   624 |
| statistics  |   596 |
| expenditure |   453 |
| Ministry    |   435 |
| GDP         |   428 |
| employment  |   399 |
| debt        |   398 |
| revenue     |   398 |
| liability   |   397 |
| indicator   |   394 |

`Canada` was the most common tag with 624 datasets.

I checked this a little further and found that 142 of those datasets came from GeoBC Branch, which is about 22.8%.

### Modification dates

I grouped the datasets by the year their catalogue metadata was last modified.

| Year | Records |
| ---- | ------- |
| 2022 |   1,155 |
| 2026 |   1,101 |
| 2023 |     371 |
| 2025 |     350 |
| 2021 |     138 |
| 2024 |     129 |
| 2020 |      64 |
| 2019 |      16 |
| 2018 |      16 |
| 2017 |      16 |

2022 looked strange because 1,155 records had their last modification date in that year, so I looked into it.

Treasury Board Staff had 388 records modified in 2022. All 388 were modified on June 1, within about 12.5 minutes.

I checked another organization to see if this was a one-off. Local Government Infrastructure and Finance had 178 records modified in 2022, and 176 of them were modified on April 6. Those 176 modifications happened within about an hour.

I don't know from the metadata alone what caused these changes, but the pattern looks like the records may have been updated in batches. Because of that, I'm being careful about using `metadata_modified` as a measure of how current the actual data is.

## Tools

* Python
* pandas
* requests
* matplotlib
* Git / GitHub
* BC Data Catalogue CKAN API

## Project structure

```text id="kl2f77"
bc-open-data-explorer/
├── data/
│   └── bc_datasets.csv
├── src/
│   └── fetch_data.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Running the project

```bash id="bjfjv5"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src/fetch_data.py
```

## Next

I'm still working on this project. Next, I want to look more closely at the resources themselves instead of only the dataset metadata. I'm especially interested in whether datasets from different organizations differ in how accessible and analysis-friendly their formats are.

## Data source

BC Data Catalogue, accessed through the CKAN API.
