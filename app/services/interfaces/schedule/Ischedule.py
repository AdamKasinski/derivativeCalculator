from abc import ABC, abstractmethod, abstractproperty

class ISchedule(ABC):

    @abstractmethod
    def generate_schedule(self,valuation_date):
        pass

    @property
    @abstractmethod
    def schedule(self):
        pass

    @schedule.setter
    def schedule(self, valuation_date):
        pass