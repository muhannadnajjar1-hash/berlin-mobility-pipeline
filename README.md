# Berlin Mobility Pipeline

A data engineering portfolio project that builds a local ETL pipeline for Berlin bike counter data.

The pipeline loads raw Berlin Open Data from an Excel file, cleans and reshapes the data, and saves a processed CSV file that is ready for analysis or later cloud storage.

## Project Goal

The goal of this project is to demonstrate core data engineering skills:

- Exploratory data analysis
- ETL pipeline design
- Data cleaning and reshaping
- Configuration-driven pipeline execution
- Logging
- Unit testing
- Git/GitHub project organization

This project is part of a larger portfolio focused on data engineering and cloud workflows.

## Dataset

The project uses Berlin bike counter data from the Berlin Open Data portal.

The raw dataset contains hourly bike counts for multiple counting stations across Berlin. For this version of the project, the pipeline processes the sheet:

```text
Jahresdatei 2025
