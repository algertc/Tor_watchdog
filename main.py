from datetime import datetime
from Traffic import Traffic
import logger
import time
import Report
from Cfg import Cfg

#parse the config object from config.ini
config = Cfg("config.ini")

def main():
  # always on loop to send mail at hour zero of the day
  while True:
    if str(datetime.now().strftime("%H:%M")) == "00:00":
      #Generate traffic report object and log it remotely with mysql
      traffic = Traffic()
      #store instance data
      down = traffic.get("down")
      up = traffic.get("up")
      timeStamp = traffic.get("timestamp")
      #pass the destination and data to the handler
      Report.handler(config, up, down, timeStamp)
      #62 to prevent double run
      time.sleep(62)

#test to ensure fucntionality on start
def init():
  print("starting")
  logger.startup_test(config.SMTP_OUTPUT_receivingAddr)
  time.sleep(5)
  print("check passed, running main")
  main()

init()
