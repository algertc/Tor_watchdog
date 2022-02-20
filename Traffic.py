from stem.control import Controller
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

class Traffic():
  def __init__(self):
    # get traffic through the inbuilt api via the "control port" 9051
    with Controller.from_port(port=9051) as controller:
      controller.authenticate(str(config['RELAY_AUTH']['hashPass']))  # access tor hash password from config.ini
      self.bytes_read = float(controller.get_info("traffic/read")) / 1000000000
      self.bytes_written = float(controller.get_info("traffic/written")) / 1000000000
      #timestamp for sorting and logging in SQL
      self.timeStamp = str(time.strftime("%H:%M %m/%d/%Y"))
      print(self.timeStamp)
  def get(self, data):
      if data == 'up':
        return self.bytes_written
      if data == 'down':
        return self.bytes_read
      if data == 'timeStamp':
        return self.timeStamp