from pathlib import Path

PKG_DIR = Path(__file__).parent


class Config:
    LOGGING_LEVEL = "INFO"
    LOGGING_FORMAT = "[ %(levelname)s - %(name)s - %(asctime)s ]: %(message)s"
