import pandas as pd

from src.transform import clean_bike_counter_data, reshape_to_long_format


def test_clean_bike_counter_data_cleans_station_ids():
    raw_df = pd.DataFrame(
        {
            "Zählstelle": ["2025-01-01 00:00:00", "2025-01-01 01:00:00"],
            "01-MI-AL-W\n16.12.2021": [5, 7],
            "02-MI-JAN-N\n01.04.2015": [10, 12],
        }
    )

    clean_df = clean_bike_counter_data(raw_df)

    assert "timestamp" in clean_df.columns
    assert "01-MI-AL-W" in clean_df.columns
    assert "02-MI-JAN-N" in clean_df.columns
    assert "01-MI-AL-W\n16.12.2021" not in clean_df.columns


def test_clean_bike_counter_data_converts_timestamp():
    raw_df = pd.DataFrame(
        {
            "Zählstelle": ["2025-01-01 00:00:00", "invalid-date"],
            "01-MI-AL-W\n16.12.2021": [5, 7],
        }
    )

    clean_df = clean_bike_counter_data(raw_df)

    assert pd.api.types.is_datetime64_any_dtype(clean_df["timestamp"])
    assert len(clean_df) == 1


def test_reshape_to_long_format():
    clean_df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(
                ["2025-01-01 00:00:00", "2025-01-01 01:00:00"]
            ),
            "01-MI-AL-W": [5, 7],
            "02-MI-JAN-N": [10, 12],
        }
    )

    long_df = reshape_to_long_format(clean_df)

    assert long_df.shape[0] == 4
    assert set(long_df.columns) == {
        "timestamp",
        "station_id",
        "bike_count",
        "date",
        "hour",
        "weekday",
        "month",
    }
    assert long_df["station_id"].nunique() == 2
    assert long_df["bike_count"].sum() == 34
