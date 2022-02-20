import logger
import configparser
config = configparser.ConfigParser()
out = config.read("config.ini")
logger.startup_test(str(config['SMTP_OUTPUT']['receivingAddr']))
