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

def save_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str) -> None:
        """
        Save processed data to a local SQLite database.
        """
        import sqlite3

        path = Path(db_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with sqlite3.connect(path) as conn:
            df.to_sql(table_name, conn, if_exists="replace", index=False)

        logging.info("Saved processed data to SQLite table '%s' in %s",
                    table_name,
                     path,
                     )