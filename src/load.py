from pathlib import Path
import logging


def save_processed_data(df, output_path: str) -> None:
    """
    Save processed data as CSV.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)

    logging.info("Saved processed data to %s", path)
