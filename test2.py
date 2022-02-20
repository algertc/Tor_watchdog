import logger
import cfg
import configparser
logger.startup_test(str(cfg.get()['SMTP_OUTPUT']['receivingAddr']))
