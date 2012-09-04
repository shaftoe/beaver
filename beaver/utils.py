import datetime
import logging


def log(line):
    """Log a single line"""
    logging.info("[%s] %s", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), line)


def warn(line):
    """Log a single warning line"""
    logging.warning("[%s] %s", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), line)
