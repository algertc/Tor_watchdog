import SQL_LOG
import mailer
def log(timestamp, up, down):
    SQL_LOG.post(timestamp, up, down)

def interface(func):
  #write the sql fucntions within this class then just use a class wrapper on some call of traffic
  def wrapper(self):
    #run func first. (so object can be created), THEN, post to sql
    traffic = func(self)
    up = traffic.get("up")
    down = traffic.get("down")
    timestamp = traffic.get("timeStamp")
    log(timestamp, up, down)
    return traffic
    #sql_post(returnVal)
  return wrapper

def generate_report():
    from Traffic import Traffic
    return Traffic()

def startup_test(receivingAddr):
    from Traffic import Traffic
    traffic = generate_report()
    mailer.sendMail(receivingAddr['SMTP_OUTPUT']['receivingAddr'], traffic.get('down'), traffic.get('up'))