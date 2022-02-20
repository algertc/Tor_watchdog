import configparser
config = configparser.ConfigParser()
out = config.read("config.ini")

def get():
    return out