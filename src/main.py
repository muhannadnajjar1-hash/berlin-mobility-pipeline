import logging

from ingest import get_raw_file_path
from transform import (
    load_bike_counter_sheet,
    clean_bike_counter_data,
    reshape_to_long_format,
)
from load import save_processed_data


RAW_FILE_PATH = "data/raw/bike_counts.xlsx"
SHEET_NAME = "Jahresdatei 2025"
OUTPUT_PATH = "data/processed/bike_counts_2025_clean.csv"


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logging.info("Starting Berlin bike counter ETL pipeline")

    raw_file_path = get_raw_file_path(RAW_FILE_PATH)

    raw_df = load_bike_counter_sheet(raw_file_path, SHEET_NAME)
    clean_df = clean_bike_counter_data(raw_df)
    long_df = reshape_to_long_format(clean_df)

    save_processed_data(long_df, OUTPUT_PATH)

    logging.info("ETL pipeline finished successfully")
    logging.info("Final rows: %s", len(long_df))


if __name__ == "__main__":
    main()
