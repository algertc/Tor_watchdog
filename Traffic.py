from stem.control import Controller
import getAuth
from datetime import datetime

#Traffic report
class Traffic():
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