import logging, os
def get_logger():
    os.makedirs('reports', exist_ok=True)
    logger = logging.getLogger('rr_qa')
    if not logger.handlers:
        fh = logging.FileHandler('reports/test_log.log')
        fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(fmt)
        logger.addHandler(fh)
        logger.setLevel(logging.INFO)
    return logger

