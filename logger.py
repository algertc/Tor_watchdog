import SQL_LOG
import Traffic
import Report

#send to sql handler for post
def log(config, timestamp, up, down):
    SQL_LOG.post(config, timestamp, up, down)


#ensure functionality on start
def startup_test(receivingAddr):
    traffic = Traffic.Traffic()
    down = traffic.get('down')
    up = traffic.get('up')
    timeStamp = traffic.get('timeStamp')
    Report.handler(str(receivingAddr), str(up), str(down), str(timeStamp))
