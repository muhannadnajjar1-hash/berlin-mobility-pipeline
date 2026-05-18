import sqlite3

import pandas as pd

from src.load import save_to_sqlite


def test_save_to_sqlite_creates_table(tmp_path):
    df = pd.DataFrame(
        {
            "timestamp": ["2025-01-01 00:00:00"],
            "station_id": ["01-MI-AL-W"],
            "bike_count": [5],
            "date": ["2025-01-01"],
            "hour": [0],
            "weekday": ["Wednesday"],
            "month": [1],
        }
    )

    db_path = tmp_path / "test.db"
    table_name = "bike_counts_test"

    save_to_sqlite(df, str(db_path), table_name)

    with sqlite3.connect(db_path) as conn:
        result = conn.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        ).fetchone()[0]

    assert result == 1
