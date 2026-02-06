from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    @abstractmethod
    def get_details(self):
        pass
