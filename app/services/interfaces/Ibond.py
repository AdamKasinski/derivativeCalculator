from abc import ABC, abstractmethod, abstractproperty

class IBond(ABC):
    
    @property
    @abstractmethod
    def schedule(self):
        pass

    @schedule.setter
    @abstractmethod
    def schedule(self, schedule):
        pass

    @property
    @abstractmethod
    def generate_cashflow(self, valuation_date):
        pass

    @property
    @abstractmethod
    def valuate(self, valuation_date):
        pass
