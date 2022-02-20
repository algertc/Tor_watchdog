#mysql decorator
def interface(func):
  def wrapper(config, up, down, timeStamp):
    #log to mysql DB with HH:MM:SS - MM/DD/YYYY - UP - DOWN
    import logger
    logger.log(timeStamp, up, down)
    tmp = config
  return wrapper

@interface
def handler(config, up, down, timeStamp):
    import mailer
    #sent to mailer
    tmp = timeStamp
    mailer.sendMail(config, down, up)