from abc import abstractmethod
from Icurve import ICurve

class IProjectionCurve(ICurve):

    @abstractmethod
    def generate_forward_rates(self):
        pass
    
    @abstractmethod
    def generate_discount_factors(self):
        pass