from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def push(self, element):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def element(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_full(self):
        pass
