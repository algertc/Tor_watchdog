def notif(func):
    def wrap(*args, **kwargs):
        print("Handling Report")
        func(*args, **kwargs)
    return wrap

@notif
def handler(config, up, down, timeStamp):
    import mailer
    import logger
    logger.log(timeStamp, up, down)
    #sent to mailer
    tmp = timeStamp
    mailer.sendMail(config, down, up)