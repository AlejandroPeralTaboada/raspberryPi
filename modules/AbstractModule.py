from abc import ABCMeta, abstractmethod


class AbstractModule:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getOperations(self):
        pass
