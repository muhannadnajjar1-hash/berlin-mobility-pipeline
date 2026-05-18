import pandas as pd
import pytest

from src.validate import validate_processed_data


def test_validate_processed_data_passes_for_valid_data():
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2025-01-01 00:00:00"]),
            "station_id": ["01-MI-AL-W"],
            "bike_count": [5],
            "date": ["2025-01-01"],
            "hour": [0],
            "weekday": ["Wednesday"],
            "month": [1],
        }
    )

    validate_processed_data(df)


def test_validate_processed_data_fails_for_missing_column():
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2025-01-01 00:00:00"]),
            "station_id": ["01-MI-AL-W"],
            "bike_count": [5],
        }
    )

    with pytest.raises(ValueError, match="missing columns"):
        validate_processed_data(df)


def test_validate_processed_data_fails_for_negative_bike_count():
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2025-01-01 00:00:00"]),
            "station_id": ["01-MI-AL-W"],
            "bike_count": [-1],
            "date": ["2025-01-01"],
            "hour": [0],
            "weekday": ["Wednesday"],
            "month": [1],
        }
    )

    with pytest.raises(ValueError, match="negative"):
        validate_processed_data(df)
