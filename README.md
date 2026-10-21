# Retail Sales Exploratory Data Analysis

**Python | pandas | Matplotlib | Data cleaning | Financial and operational analysis**

## Project overview

This project analyzes a retail transaction dataset by joining sales events, product categories, and country reference data. The goals are to clean and validate multi-table data, calculate revenue and gross profit, and investigate differences in product performance, sales channels, and shipping times.

**Data context:** These are results for a supplied practice dataset, not audited financial statements for a real company. Dataset provenance and redistribution permissions have not yet been verified.

## Questions explored

- Which categories contribute the most recorded revenue and gross profit?
- How do online and offline sales channels compare?
- What is the average shipping duration?
- How do missing or unmatched data affect financial and geographic reporting?

## Data and methodology

The analysis uses three CSV datasets: `events.csv` (1,330 transactions), `products.csv` (12 product categories), and `countries.csv` (249 country reference rows).

The cleaned analysis:
1. Reads standardized source files using relative paths.
2. Checks identifiers, missing values, and categorical labels.
3. Joins transaction, product, and country tables with many-to-one validation to prevent row multiplication.
4. Computes recorded revenue, cost, gross profit, gross margin, and shipping duration.
5. Compares sales channels and product categories using summary tables and visualizations.

## Validated results

| Metric | Result |
| --- | ---: |
| Transactions | 1,330 |
| Revenue (known-quantity transactions) | $1,702,129,408.21 |
| Gross profit (known-quantity transactions) | $501,434,459.00 |
| Gross margin (known-quantity transactions) | 29.46% |
| Average shipping duration | 24.78 days |
| Identified countries in transactions | 45 |
| Transactions missing country codes | 82 |
| Transactions missing units sold | 2 |

The three leading categories by recorded profit were **Cosmetics ($92.72M)**, **Office Supplies ($77.98M)**, and **Household ($72.96M)**. Combined, they contributed approximately **48.6%** of recorded profit.

Recorded offline gross profit was approximately **$253.47M**, compared with **$247.97M** online.

## Data limitations

- Two transactions lack units sold; their revenue and cost contributions are **unknown**, not zero.
- 82 transactions have missing country codes and must be classified as unknown geography.
- Figures describe the practice dataset and should not be interpreted as real-company performance.
- Descriptive associations should not be interpreted as causal explanations.
- The CSV files are not redistributed here until their source and public-use permissions can be established.

## Running the analysis

1. Obtain authorized copies of `events.csv`, `products.csv`, and `countries.csv`.
2. Put these files in a local `data_clean/` directory, after applying the documented cleaning rules.
3. Install requirements: `python -m pip install -r requirements.txt`.
4. Run the notebook with the project root as the working directory.

> The notebook may be reviewed on GitHub without the CSVs. Running it requires separately obtained, appropriately cleaned input files. The cleaned notebook is published as `retail_eda_cleaned.ipynb`. It requires the three cleaned CSV files, which are not hosted publicly.

## Project status

Core financial calculations were independently checked against the supplied datasets; the cleaned working notebook was executed locally. The cleaned notebook replaces the older Colab version in this repository. Source CSV files remain excluded pending redistribution review.
