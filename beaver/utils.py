import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)


def log(line):
    """Log a single line"""
    logging.info(line)


def warn(line):
    """Log a single warning line"""
    logging.warning(line)
