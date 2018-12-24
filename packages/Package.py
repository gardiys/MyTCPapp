from abc import ABC, abstractmethod
from DataStream import DataStream

class Package(ABC):
    """Abstract class for packages"""
    @property
    @abstractmethod
    def id(self):
        pass

    def __init__(self, stream:DataStream):
        self.stream = stream

    @abstractmethod
    def read_stream(self):
        pass

    @abstractmethod
    def write_stream(self):
        pass
