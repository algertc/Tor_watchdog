from datetime import datetime
from Traffic import Traffic
import cfg
import logger
import mailer
import time

config = cfg.get()

#test to ensure fucntionality on start
logger.startup_test(config)

#always on loop to send mail at hour zero of the day
while True:
  if str(datetime.now().strftime("%H:%M")) == "00:00":
    #Generate traffic report object and log it remotely with mysql
    traffic = logger.generate_report()
    #Send A plaintext
    mailer.sendMail(config, traffic.get('down'), traffic.get('up'))
    time.sleep(62)


