import json
class Properties:
    def __init__(self):
        self.file = 'config.json'
        self.data = None

    def getModules(self):
        if (self.data == None):
            with open(self.file) as jsonFile:
                self.data = json.load(jsonFile)
        return self.data['modules']

    def getComunicators(self):
        if (self.data == None):
            with open(self.file) as jsonFile:
                self.data = json.load(jsonFile)
        return self.data['comunications']