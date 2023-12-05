from abc import ABC, abstractmethod


class LimitedContainer(ABC):
    @abstractmethod
    def enqueue(self, element):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_full(self):
        pass