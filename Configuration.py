import json

class Configuration:
    def __init__(self):
        try:
            with open("./DataBaseConfig.json", 'r') as f:
                config = json.load(f)
            self.database = config["database"]
            self.user = config["user"] 
            self.password = config["password"]
            self.host = config["host"]
            self.port = config["port"]
        except :
            print("error by reading the configuration file!")
            raise 
