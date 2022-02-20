import mailer

def interface(func):
  # write the sql fucntions within this class then just use a class wrapper on some call of traffic
  def wrapper(config, up, down, timeStamp):
    # run func first. (so object can be created), THEN, post to sql
    import logger
    logger.log(timeStamp, up, down)
    tmp = config
    # sql_post(returnVal)
  return wrapper

@interface
def handler(config, up, down, timeStamp):
    mailer.sendMail(config, down, up)