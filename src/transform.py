import logging
import pandas as pd


def load_bike_counter_sheet(file_path: str, sheet_name: str) -> pd.DataFrame:
    """
    Load the Berlin bike counter Excel sheet.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

    logging.info("Loaded sheet '%s' with shape %s", sheet_name, df.shape)

    return df


def clean_bike_counter_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the wide bike counter dataset.
    """
    df = df.copy()

    # Rename first column to timestamp
    df.rename(columns={df.columns[0]: "timestamp"}, inplace=True)

    # Convert timestamp column
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Remove rows without valid timestamp
    df = df.dropna(subset=["timestamp"])

    # Normalize station column names
    station_columns = [col for col in df.columns if col != "timestamp"]
    df[station_columns] = df[station_columns].apply(pd.to_numeric, errors="coerce")

    logging.info("Cleaned data shape: %s", df.shape)

    return df


def reshape_to_long_format(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert wide station columns into long format.
    """
    df_long = df.melt(
        id_vars="timestamp",
        var_name="station_id",
        value_name="bike_count",
    )

    df_long["date"] = df_long["timestamp"].dt.date
    df_long["hour"] = df_long["timestamp"].dt.hour
    df_long["weekday"] = df_long["timestamp"].dt.day_name()
    df_long["month"] = df_long["timestamp"].dt.month

    logging.info("Reshaped data to long format: %s", df_long.shape)

    return df_long
