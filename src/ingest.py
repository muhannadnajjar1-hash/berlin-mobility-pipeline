from pathlib import Path
import logging


def get_raw_file_path(raw_file_path: str) -> Path:
    """
    Check that the raw Excel file exists and return its path.
    """
    path = Path(raw_file_path)

    if not path.exists():
        raise FileNotFoundError(f"Raw file not found: {path}")

    logging.info("Raw file found: %s", path)
    return path
