from abc import ABC, abstractmethod, abstractproperty

class IBond(ABC):
    
    @property
    @abstractmethod
    def valuate(valuation_date):
        pass

    @property
    @abstractmethod
    def notional(self):
        pass
#
    #@property
    #@abstractmethod
    #def start_date(self):
    #    pass
#
    #@property
    #@abstractmethod
    #def end_date(self):
    #    pass
#
    #@property
    #@abstractmethod
    #def leg(self):
    #    pass
#
    #@property
    #@abstractmethod
    #def interest_rate(self):
    #    pass
#
    #@property
    #@abstractmethod
    #def margin(self):
    #    pass
    #
    #@property
    #@abstractmethod
    #def frequency(self):
    #    pass
#
    #@property
    #@abstractmethod
    #def type(self):
    #    pass
#
    #@property
    #@abstractmethod
    #def float_leg_curve(self):
    #    pass
#