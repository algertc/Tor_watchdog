import SQL_LOG
from Traffic import Traffic
import mailer
def log(object):
    up = object.get("up")
    down = object.get("down")
    timestamp = object.get("timeStamp")
    SQL_LOG.post(timestamp, up, down)

def interface(func):
  #write the sql fucntions within this class then just use a class wrapper on some call of traffic
  def wrapper(self):
    #run func first. (so object can be created), THEN, post to sql
    traffic = func(self)
    log(traffic)
    return traffic
    #sql_post(returnVal)
  return wrapper

def generate_report():
    return Traffic()

def startup_test(receivingAddr):
    traffic = generate_report()
    mailer.sendMail(receivingAddr['SMTP_OUTPUT']['receivingAddr'], traffic.get('down'), traffic.get('up'))