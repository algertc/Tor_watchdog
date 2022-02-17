from stem.control import Controller
from datetime import datetime
import getAuth
import configparser
import mailer
import time
config = configparser.ConfigParser()
config.read("config.ini")


with Controller.from_port(port = 9051) as controller:

  controller.authenticate(getAuth.hash())  #access tor hash password from config.ini

  bytes_read = controller.get_info("traffic/read")
  bytes_written = controller.get_info("traffic/written")

  print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))

  mailer.sendMail(config['OUTPUT']['receivingAddr'], bytes_read, bytes_written)

while True:
  if str(datetime.now().strftime("%H:%M")) == "00:00":
    mailer.sendMail(config['OUTPUT']['receivingAddr'], bytes_read, bytes_written)
    time.sleep(62)


