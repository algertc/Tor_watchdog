from datetime import datetime
import Traffic
import configparser
import mailer
import time
#create config object
#todo make a config class/file with the getAuth.py stuff and use that instead of accessing from main
config = configparser.ConfigParser()
#declaring the file from which config should retrieve its data
config.read("config.ini")

#test to ensure fucntionality on start
mailer.sendMail(config['OUTPUT']['receivingAddr'], Traffic.get('down'), Traffic.get('up'))

#always on loop to send mail at hour zero of the day
while True:
  if str(datetime.now().strftime("%H:%M")) == "00:00":
    mailer.sendMail(config['OUTPUT']['receivingAddr'], Traffic.get('down'), Traffic.get('up'))
    time.sleep(62)


