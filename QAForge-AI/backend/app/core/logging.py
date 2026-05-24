import logging
from logging.handlers import RotatingFileHandler

def setup_audit_logging():
    audit_logger = logging.getLogger('audit')
    audit_logger.setLevel(logging.INFO)

    handler = RotatingFileHandler('audit.log', maxBytes=1024*1024, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    audit_logger.addHandler(handler)
    return audit_logger

audit_logger = setup_audit_logging()