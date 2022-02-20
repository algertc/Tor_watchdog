from datetime import datetime
import configparser
import mailer
import time
import Traffic
#create config object
#todo make a config class/file with the getAuth.py stuff and use that instead of accessing from main
config = configparser.ConfigParser()
#declaring the file from which config should retrieve its data
config.read("config.ini")

#use a decorator with the constructor to

#test to ensure fucntionality on start
testTraf = Traffic.Traffic()
mailer.sendMail(config['SMTP_OUTPUT']['receivingAddr'], testTraf.get('down'), testTraf.get('up'))

#always on loop to send mail at hour zero of the day
while True:
  if str(datetime.now().strftime("%H:%M")) == "00:00":
    traffic = Traffic.Traffic()
    mailer.sendMail(config['SMTP_OUTPUT']['receivingAddr'], traffic.get('down'), traffic.get('up'))
    time.sleep(62)


