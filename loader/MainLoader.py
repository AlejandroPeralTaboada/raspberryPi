from  properties.Properties import Properties
from importlib import import_module

class MainLoader:
    def __init__(self):
        self.modules = []
        self.comunications = []
        self.properties = Properties()
    def load(self):
        self.__loadComunications()
        self.__loadModules()


    def __loadComunications(self):
        comunicators = self.properties.getComunicators()
        for comunicator in comunicators:
            self.comunications.append(self.__loadModule('comunications',comunicator['name']))
        for comunicator in self.comunications:
            comunicator.addHandler(self.notify)

    def __loadModules(self):
        modules = self.properties.getModules()
        for module in modules:
            self.modules.append(self.__loadModule('modules',module['name']))

    def __loadModule(self,modulePackage,moduleName):
        print(moduleName)
        _temp = import_module(modulePackage+'.' + moduleName)
        myclass = getattr(_temp, moduleName)
        return myclass()

    def notify(self,msg):
        print (msg)



