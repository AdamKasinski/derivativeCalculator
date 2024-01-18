from abc import ABC, abstractmethod, abstractproperty

class IBond_pricing(ABC):

    @property
    @abstractmethod
    def generate_cashflows(self):
        pass

    @property
    @abstractmethod
    def valuate(self):
        pass