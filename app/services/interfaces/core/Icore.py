from abc import ABC, abstractmethod

class ICore(ABC):
    
    @abstractmethod
    def yearfrac(earlier_date, later_date):
        pass
    
    @abstractmethod
    def logarithmic_interpolation(on_date,date_before,date_after,value_before,value_after):
        pass

    @abstractmethod
    def linear_interpolation(on_date,date_before,date_after,value_before,value_after):
        pass

    @abstractmethod
    def calculate_forward_rate(valuation_date,date_before,date_after,value_before,value_after):
        pass
    
    @abstractmethod
    def calculate_discount_factor(yearfrac,interest_rate):
        pass
