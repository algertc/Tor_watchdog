#config
class Cfg:
    def __init__(self, file):
        import configparser
        config = configparser.ConfigParser()
        config.read(file)#use configparser lib to conver ini file to dictionary with 2D array keys
        #i = outer header []
        for i in config:
            #j = individual entry
            for j in config[i]:
                #use exec fucntion to dynamically create instance data attributes and names depending on config content
                exec("self.{} = '{}'".format(("%s_%s" % (i,j)), str(config[i][j])))

                #benefits
                #todo if you can explain the benefit of having it as instance data of a config
                #todo   object instead of a list. This is valid.
                #no need to import and read each time
                #same time compelxity but will run faster withiuot the need to query a hashmap
                #big O noation time complexity
