from pathlib import Path

PKG_DIR = Path(__file__).parent


class Config:
    LOGGING_CONFIG = {
        "level": "INFO",
        "format": "[ %(levelname)s - %(name)s - %(asctime)s ]: %(message)s",
    }
