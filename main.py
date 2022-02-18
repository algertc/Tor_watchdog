from datetime import datetime
import Traffic
import configparser
import mailer
import time
config = configparser.ConfigParser()
config.read("config.ini")

#test to ensure fucntionality on start
mailer.sendMail(config['OUTPUT']['receivingAddr'], Traffic.get('down'), Traffic.get('up'))

while True:
  if str(datetime.now().strftime("%H:%M")) == "00:00":
    mailer.sendMail(config['OUTPUT']['receivingAddr'], Traffic.get('down'), Traffic.get('up'))
    time.sleep(62)


