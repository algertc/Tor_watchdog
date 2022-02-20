import SQL_LOG
import mailer
import Traffic
def log(timestamp, up, down):
    SQL_LOG.post(timestamp, up, down)

def startup_test(receivingAddr):
    traffic = Traffic.Traffic()
    down = traffic.get('down')
    up = traffic.get('up')
    print(down)
    mailer.sendMail(receivingAddr, str(down), str(up))