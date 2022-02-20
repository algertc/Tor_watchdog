import mysql.connector
import base64
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

#post entry to mysql
def post(time, up, down):
    db = mysql.connector.connect(
        host=str(config['MYSQL']['host']),
        user=str(config['MYSQL']['user']),
        passwd=(base64.b64decode(str(config['MYSQL']['passwd']).encode('ascii')).decode('ascii'))
        )
    cursor = db.cursor() #pointer in db
    cursor.execute("USE tor_logging;") #tor_logging - db name
    #truncate float for sql limit
    cursor.execute("INSERT INTO log (timestamp, bytesUP, bytesDOWN) VALUES (%s,%s,%s);" % (time, str(round(int(up), 3)), str(round(int(down, 3)))))
    db.commit()
