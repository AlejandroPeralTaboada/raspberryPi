import os

from comunications.Telegram import Telegram
from properties.Properties import Properties
from importlib import import_module
from loader.MainLoader import MainLoader


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))

def loadModule(moduleName):
    _temp = import_module('modules.' + moduleName)
    myclass = getattr(_temp, moduleName)
    return myclass()

def loadProps():
    props = Properties()
    module = props.getModules()[0]
    myobject = loadModule(module['name'])
    print(getattr(myobject, myobject.getOperations()[0])())

def main():
    mainLoader = MainLoader()
    mainLoader.load()

if __name__ == '__main__':
    main()
