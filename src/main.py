import logging

from ingest import get_raw_file_path, load_config
from load import save_processed_csv, save_processed_parquet, save_to_sqlite
from transform import (
    clean_bike_counter_data,
    load_bike_counter_sheet,
    reshape_to_long_format,
)
from validate import validate_processed_data

CONFIG_PATH = "config/config.yaml"


def main():
    config = load_config(CONFIG_PATH)

    logging.basicConfig(
        level=getattr(logging, config["logging"]["level"]),
        format="%(asctime)s %(levelname)s %(message)s",
        force=True,
    )

    logging.info("Starting Berlin bike counter ETL pipeline")

    raw_file_path = get_raw_file_path(config["dataset"]["raw_file_path"])

    raw_df = load_bike_counter_sheet(
        raw_file_path,
        config["dataset"]["sheet_name"],
    )

    clean_df = clean_bike_counter_data(raw_df)
    long_df = reshape_to_long_format(clean_df)

    validate_processed_data(long_df)

    save_processed_csv(
        long_df,
        config["output"]["processed_csv_path"],
    )

    save_processed_parquet(
        long_df,
        config["output"]["processed_parquet_path"],
    )
    save_to_sqlite(
        long_df,
        config["database"]["sqlite_path"],
        config["database"]["table_name"],
    )

    logging.info("ETL pipeline finished successfully")
    logging.info("Final rows: %s", len(long_df))


if __name__ == "__main__":
    main()