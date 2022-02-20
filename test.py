import mysql.connector
import base64
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
db = mysql.connector.connect(host=str(config['SQL']['host']), user=str(config['SQL']['user']),
                             passwd=(base64.b64decode(str(config['SQL']['passwd']).encode('ascii')).decode('ascii')))
cursor = db.cursor()
cursor.execute("show databases")
for i in cursor:
    print(i)