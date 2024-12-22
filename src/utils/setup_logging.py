import logging
from logging.handlers import RotatingFileHandler


from core import settings


def setup_logging():
    console_formatter = logging.Formatter(
        fmt=f"%(asctime)s.%(msecs)03d - {settings.APP_NAME} - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(settings.LOG_LEVEL)
    console_handler.setFormatter(console_formatter)

    try:
        file_handler = RotatingFileHandler(settings.LOG_PATH, "a", 10000000, 3)
    except FileNotFoundError:
        file_handler = RotatingFileHandler("log.log", "a", 10000000, 3)
    file_handler.setLevel(settings.LOG_LEVEL)

    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False
