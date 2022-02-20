import SQL_LOG
import mailer
from Traffic import Traffic
def log(timestamp, up, down):
    SQL_LOG.post(timestamp, up, down)

def startup_test(receivingAddr):
    traffic = Traffic()
    mailer.sendMail(receivingAddr['SMTP_OUTPUT']['receivingAddr'], traffic.get('down'), traffic.get('up'))