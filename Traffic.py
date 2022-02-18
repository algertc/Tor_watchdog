from stem.control import Controller
import getAuth
def get(updown):
  with Controller.from_port(port = 9051) as controller:
    controller.authenticate(getAuth.hash())  #access tor hash password from config.ini
    bytes_read = str((float(controller.get_info("traffic/read"))/1000000000)) + "GB" #Format to GB for readability
    bytes_written = str(float(controller.get_info("traffic/written")/1000000000)) + "GB"
    print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))
    if updown == 'up':
      return bytes_written
    if updown == 'down':
      return bytes_read