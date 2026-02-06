from abc import ABC, abstractmethod
# Abstract base class
class Person(ABC):
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name
# Abstract method to be overridden
    @abstractmethod
    def get_details(self):
        pass
