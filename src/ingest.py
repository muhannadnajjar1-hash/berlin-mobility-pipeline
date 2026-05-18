import logging
from pathlib import Path

import yaml


def load_config(config_path: str) -> dict:
    """
    Load pipeline configuration from a YAML file.
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path) as file:
        config = yaml.safe_load(file)

    logging.info("Loaded config from %s", path)
    return config


def get_raw_file_path(raw_file_path: str) -> Path:
    """
    Check that the raw Excel file exists and return its path.
    """
    path = Path(raw_file_path)

    if not path.exists():
        raise FileNotFoundError(f"Raw file not found: {path}")

    logging.info("Raw file found: %s", path)
    return path
