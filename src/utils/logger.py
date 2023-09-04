import logging

def log() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    return logger