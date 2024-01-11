from abc import ABC, abstractmethod

class ICurve(ABC):
    
    @abstractmethod
    def interpolate_curve(start_date,end_date):
        pass
    
