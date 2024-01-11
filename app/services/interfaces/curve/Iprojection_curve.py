from abc import abstractmethod
from Icurve import ICurve

class IProjectionCurve(ICurve):

    @abstractmethod
    def generate_forward_rates(start_date,end_date):
        pass
    
    @abstractmethod
    def generate_discount_factors(start_date,end_date):
        pass