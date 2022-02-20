class Log(object):
  #write the sql fucntions within this class then just use a class wrapper on some call of traffic
  def __call__(self, func):
    def wrapper(self):
      #run func first. (so object can be created), THEN, post to sql
      traffic = self()
      print(traffic.get('up'))
      #sql_post(returnVal)
      return traffic
    return wrapper

  import mysql.connector
  import base64
  import configparser
  config = configparser.ConfigParser()
  config.read("config.ini")
  db = mysql.connector.connect(host=str(config['SQL']['host']), user=str(config['SQL']['user']),
                               passwd=(base64.b64decode(str(config['SQL']['passwd']).encode('ascii')).decode('ascii')))
  cursor = db.cursor()
