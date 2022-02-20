from stem.control import Controller
import getAuth
from datetime import datetime
import configparser
import base64
config = configparser.ConfigParser()
config.read("config.ini")

import mysql.connector
db = mysql.connector.connect(host=str(config['SQL']['host']), user=str(config['SQL']['user']), passwd = (base64.b64decode(str(config['SQL']['passwd']).encode('ascii')).decode('ascii')))
db.cursor()

class Log(object):
  #write the sql fucntions within this class then just use a class wrapper on some call of traffic
  def __call__(self, func):
    def wrapper(self):
      #run func first. (so object can be created), THEN, post to sql
      traffic = self()
      print(traffic.get('up'))
      #sql_post(returnVal)
      return traffic
    return wrapper

#Traffic report
class Traffic:
  @Log
  def __init__(self):
    # get traffic through the inbuilt api via the "control port" 9051
    with Controller.from_port(port=9051) as controller:
      # access tor hash password from config.ini
      controller.authenticate(getAuth.hash())
      self.bytes_read = float(controller.get_info("traffic/read")) / 1000000000
      self.bytes_written = float(controller.get_info("traffic/written")) / 1000000000
      #timestamp for sorting and logging in SQL
      self.timeStamp = "%s/%s/%s" % (datetime.today().month, datetime.today().day, datetime.today().year)


  def get(self, updown):
      if updown == 'up':
        return self.bytes_written
      if updown == 'down':
        return self.bytes_read