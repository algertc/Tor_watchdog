from stem.control import Controller
import getAuth
from datetime import datetime

def interface(func):

  #write the sql fucntions within this class then just use a class wrapper on some call of traffic
  def wrapper(self):
    #run func first. (so object can be created), THEN, post to sql
    import logger
    traffic = func(self)
    up = traffic.get("up")
    down = traffic.get("down")
    timestamp = traffic.get("timeStamp")
    logger.log(timestamp, up, down)
    return traffic
    #sql_post(returnVal)
  return wrapper

#Traffic report
class Traffic():
  @interface
  def __init__(self):
    # get traffic through the inbuilt api via the "control port" 9051
    with Controller.from_port(port=9051) as controller:
      # access tor hash password from config.ini
      controller.authenticate(getAuth.hash())
      self.bytes_read = float(controller.get_info("traffic/read")) / 1000000000
      self.bytes_written = float(controller.get_info("traffic/written")) / 1000000000
      #timestamp for sorting and logging in SQL
      self.timeStamp = "%s/%s/%s" % (datetime.today().month, datetime.today().day, datetime.today().year)


  def get(self, data):
      if data == 'up':
        return self.bytes_written
      if data == 'down':
        return self.bytes_read
      if data == 'timeStamp':
        return self.timeStamp