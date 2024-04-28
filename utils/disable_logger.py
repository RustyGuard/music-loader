import logging


def disable_pytube_logger():
    logger = logging.getLogger("pytube.contrib.search")
    logger.propagate = False
    logger.setLevel(logging.CRITICAL)
