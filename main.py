from datetime import datetime
from Traffic import Traffic
import cfg
import logger
import mailer
import time
import Report

config = cfg.get()

#test to ensure fucntionality on start
logger.startup_test(config['SMTP_OUTPUT']['receivingAddr'])

#always on loop to send mail at hour zero of the day
while True:
  if str(datetime.now().strftime("%H:%M")) == "00:00":
    #Generate traffic report object and log it remotely with mysql
    traffic = Traffic()
    down = traffic.get('down')
    up = traffic.get('up')
    timeStamp = traffic.get('timeStamp')
    Report.handler(config['SMTP_OUTPUT']['receivingAddr'], up, down, timeStamp)
    time.sleep(62)


