from modules.AbstractModule import AbstractModule


class CpuTemperature(AbstractModule):
    def __init__(self):
        self.operations = ['cpuTemperature']

    def getOperations(self):
        return self.operations

    def cpuTemperature(self):
        return 100
