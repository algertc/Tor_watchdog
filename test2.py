import logger
import cfg

logger.startup_test(cfg.get()['SMTP_OUTPUT']['receivingAddr'])
