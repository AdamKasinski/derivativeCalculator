from abc import ABC, abstractmethod, abstractproperty

class IBond(ABC):
    
    @property
    @abstractmethod
    def generate_cashflows(self, valuation_date,schedule):
        pass

    @property
    @abstractmethod
    def valuate(self, valuation_date):
        pass

    @property
    @abstractmethod
    def cashflows(self):
        pass

    @property
    @abstractmethod
    def schedule(self):
        pass

    @property
    @abstractmethod
    def notional(self) -> float:
        pass

    @property
    @abstractmethod
    def start_date(self) -> date:
        pass

    @property
    @abstractmethod
    def end_date(self) -> date:
        pass

    @property
    @abstractmethod
    def leg(self) -> str:
        pass

    @property
    @abstractmethod
    def interest_rate(self) -> float:
        pass

    @property
    @abstractmethod
    def margin(self) -> float:
        pass

    @property
    @abstractmethod
    def frequency(self) -> str:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def float_leg_curve(self):
        pass