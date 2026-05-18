import logging

import pandas as pd

REQUIRED_COLUMNS = {
    "timestamp",
    "station_id",
    "bike_count",
    "date",
    "hour",
    "weekday",
    "month",
}


def validate_processed_data(df: pd.DataFrame) -> None:
    """
    Validate the processed bike counter dataset.

    Raises:
        ValueError: If validation fails.
    """
    logging.info("Starting data validation")

    if df.empty:
        raise ValueError("Validation failed: processed dataset is empty")

    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Validation failed: missing columns {missing_columns}")

    if df["timestamp"].isna().any():
        raise ValueError("Validation failed: timestamp contains missing values")

    if df["station_id"].isna().any():
        raise ValueError("Validation failed: station_id contains missing values")

    if df["bike_count"].isna().all():
        raise ValueError("Validation failed: bike_count column is completely empty")

    if (df["bike_count"].dropna() < 0).any():
        raise ValueError("Validation failed: bike_count contains negative values")

    if not df["hour"].between(0, 23).all():
        raise ValueError("Validation failed: hour values must be between 0 and 23")

    if not df["month"].between(1, 12).all():
        raise ValueError("Validation failed: month values must be between 1 and 12")

    logging.info("Data validation passed")
