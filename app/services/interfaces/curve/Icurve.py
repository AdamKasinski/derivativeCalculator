from abc import ABC, abstractmethod

class ICurve(ABC):
    
    @abstractmethod
    def get_data(self):
        pass
    
    @abstractmethod
    def interpolate_curve(self):
        pass
    
