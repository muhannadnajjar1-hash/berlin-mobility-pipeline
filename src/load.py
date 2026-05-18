import logging
from pathlib import Path

import pandas as pd


def save_processed_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Save processed data as CSV.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)

    logging.info("Saved processed CSV data to %s", path)


def save_processed_parquet(df: pd.DataFrame, output_path: str) -> None:
    """
    Save processed data as Parquet.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(path, index=False)

    logging.info("Saved processed Parquet data to %s", path)