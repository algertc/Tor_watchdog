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

              
                """
                  #######  #Why convert to a separate object?   #######
                  
                1) Negates the need to import the parser and create separate dictioanry config objects in each file
               
                2) The parser returns a dictioanry created from the content in "config.ini"
                    -Speed improvement 
                    - In python, dictionaries make use of a hash table. (The fastest inbuilt data structure)
                    - Take advantage of the capabilities of the hashmap by querying it only once and create lightweight object from its content (cfg), 
                        - Result: Config references now access instance data rather the array, making a speed improvement, albeit marginal (both at O(1))
               
                3) increased readability, shorter lines, and simplified naming conventions
                """
