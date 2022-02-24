class Cfg:
    def __init__(self):
        import configparser
        config = configparser.ConfigParser()
        config.read("config.ini")
        for i in config:
            for j in config[i]:
                exec("self.{} = '{}'".format(("%s_%s" % (i,j)), str(config[i][j])))

        #todo need to make a func like getfield passing the param from for loop so a return of the field can be sent each time
        #todo to dynamically set the instance data
