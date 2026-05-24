# Berlin Mobility Pipeline

![Tests](https://github.com/muhannadnajjar1-hash/berlin-mobility-pipeline/actions/workflows/tests.yml/badge.svg)

A local data engineering pipeline for Berlin bike counter data.

This project is part of my **Berlin Data Engineering Lab** portfolio. It demonstrates how raw Excel data can be ingested, cleaned, validated, transformed, and stored in analysis-ready formats.

## Project Purpose

The goal of this project is to build a reproducible batch ETL pipeline for real-world Berlin mobility data.

The pipeline processes raw bike counter data for 2025 and produces clean outputs that can be used for analysis, SQL queries, and downstream projects.

This project is the first project in the portfolio and provides the mobility dataset used later by the **Berlin Analytics Warehouse** project.

## Portfolio Role

This project is the foundation of the portfolio data flow:

```text
Project 1: Berlin Mobility Pipeline
        ↓ produces bike_counts_2025_clean.parquet
Project 3: Berlin Analytics Warehouse
```

The cleaned Parquet output from this project is consumed by the analytics warehouse together with historical weather data from the Berlin Weather Pipeline.

## Data Source

The project uses Berlin bike counter data from the Berlin Open Data portal.

In this version, the pipeline processes the Excel sheet:

```text
Jahresdatei 2025
```

The raw Excel file is expected locally at:

```text
data/raw/bike_counts.xlsx
```

The `data/` folder is ignored by Git because it contains local or generated data files.

## ETL Pipeline

```text
Raw Excel file
      ↓
Ingest
      ↓
Transform
      ↓
Validate
      ↓
Load
      ↓
CSV / Parquet / SQLite outputs
```

## Architecture

1. Load the project configuration.
2. Check that the raw Excel file exists locally.
3. Read the 2025 bike counter sheet.
4. Clean timestamps and station headers.
5. Transform the data from wide format to long format.
6. Validate the processed dataset.
7. Store the clean data as CSV, Parquet, and SQLite.
8. Run tests and linting through GitHub Actions.

## Project Structure

```text
berlin-mobility-pipeline/
├── .github/workflows/     # GitHub Actions CI
├── config/                # Pipeline configuration
├── notebooks/             # Exploratory analysis notebook and figure
├── src/                   # ETL pipeline source code
├── tests/                 # Unit tests
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Tool configuration
└── .gitignore
```

## Main Pipeline Components

### Ingest

`src/ingest.py` loads the configuration and checks whether the raw input file exists.

### Transform

`src/transform.py` contains the main transformation logic:

- reads the 2025 Excel sheet
- cleans timestamp values
- cleans station names from messy Excel headers
- converts bike count values to numeric format
- transforms the data from wide format to long format
- creates useful date features such as `date`, `hour`, `weekday`, and `month`

### Validate

`src/validate.py` checks the processed dataset before it is saved.

Validation checks include:

- dataset is not empty
- required columns are present
- timestamps are not missing
- station IDs are not missing
- bike counts are not negative
- hour values are between 0 and 23
- month values are between 1 and 12

### Load

`src/load.py` stores the validated dataset as:

```text
data/processed/bike_counts_2025_clean.csv
data/processed/bike_counts_2025_clean.parquet
data/processed/berlin_mobility.db
```

## Configuration

Pipeline settings are stored in:

```text
config/config.yaml
```

Example:

```yaml
dataset:
  raw_file_path: "data/raw/bike_counts.xlsx"
  sheet_name: "Jahresdatei 2025"

output:
  processed_csv_path: "data/processed/bike_counts_2025_clean.csv"
  processed_parquet_path: "data/processed/bike_counts_2025_clean.parquet"

database:
  sqlite_path: "data/processed/berlin_mobility.db"
  table_name: "bike_counts_2025"

logging:
  level: "INFO"
```

## Local Setup

Clone the repository:

```bash
git clone https://github.com/muhannadnajjar1-hash/berlin-mobility-pipeline.git
cd berlin-mobility-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create local data folders:

```bash
mkdir -p data/raw data/processed
```

Place the raw Excel file here:

```text
data/raw/bike_counts.xlsx
```

## Run the Pipeline

Run the full ETL pipeline:

```bash
python src/main.py
```

Expected outputs:

```text
data/processed/bike_counts_2025_clean.csv
data/processed/bike_counts_2025_clean.parquet
data/processed/berlin_mobility.db
```

Optional SQLite check:

```bash
sqlite3 data/processed/berlin_mobility.db
```

Example query:

```sql
SELECT COUNT(*) FROM bike_counts_2025;
```

## Current Results

A successful local pipeline run creates:

```text
8,760 hourly timestamps
35 bike counting stations
306,600 rows after transformation to long format
```

The processed dataset contains the following columns:

```text
timestamp, station_id, bike_count, date, hour, weekday, month
```

## Visualization

The following chart shows daily bike counts across all stations for 2025.

![Daily bike counts 2025](notebooks/daily_bike_counts.png)

## Quality Checks

Run unit tests:

```bash
pytest
```

Run Ruff linting:

```bash
ruff check src tests
```

The tests check that:

- station IDs are cleaned correctly
- invalid timestamps are handled
- data is transformed correctly from wide to long format
- valid processed data passes validation
- invalid processed data fails validation
- SQLite export creates a queryable table

## Continuous Integration

This project uses GitHub Actions to run Ruff linting and unit tests automatically on every push and pull request to the `main` branch.

The workflow is defined in:

```text
.github/workflows/tests.yml
```

The workflow runs:

```bash
ruff check src tests
pytest
```

## Design Decisions

- Raw data is not committed to Git because it is a local/generated data asset.
- The pipeline is configuration-driven so file paths and settings are not hard-coded in the main code.
- Transformation logic is implemented in `src/transform.py`; notebooks are used only for exploration.
- The processed data is stored in CSV, Parquet, and SQLite to demonstrate multiple storage formats.
- Validation runs before loading so invalid data is not written silently.
- GitHub Actions checks code quality and tests automatically.
- The project stays local and free at this stage, with cloud storage as a possible later extension.

## Current Limitations

- The raw Excel file must be downloaded manually and placed in `data/raw/`.
- The visualization is currently stored under `notebooks/`; a future cleanup could move final figures to `reports/figures/`.
- The pipeline is currently a local batch pipeline and is not scheduled automatically.

## Future Improvements

- Move final figures to `reports/figures/`.
- Add a small data dictionary for the processed output columns.
- Add a script for regenerating figures from the processed data.
- Add scheduled execution or cloud storage in a later version.
- Connect this pipeline more explicitly with downstream warehouse and API projects.

## Portfolio Context

This is the first project in my Berlin Data Engineering Lab portfolio.

```text
Project 1: Berlin Mobility Pipeline
        ↓
Project 2: Berlin Weather Pipeline
        ↓
Project 3: Berlin Analytics Warehouse
```

Together, these projects show a progression from raw data ingestion and cleaning to API ingestion and analytical data modeling.
