import numpy as np
from services.interfaces.core.Icore import ICore

class Core(ICore):

    @staticmethod
    def yearfrac(earlier_date, later_date):
        return (later_date-earlier_date).astype(int)/365

    @staticmethod
    def logarithmic_interpolation(on_date,date_before,date_after,value_before,value_after):
        total_duration = (date_after - date_before).astype(int)
        later_duration = (date_after - on_date).astype(int)
        later_frac = later_duration/total_duration
        return value_after**later_frac*value_before**(1-later_duration)

    @staticmethod
    def linear_interpolation(on_date,date_before,date_after,value_before,value_after):
        return np.interp(on_date,[date_before,date_after],[value_before,value_after])

    @staticmethod
    def calculate_forward_rate(valuation_date,date_before,date_after,value_before,value_after):
        t1 = Core.yearfrac(valuation_date,date_before)
        t2 = Core.yearfrac(valuation_date,date_after)
        return (1+value_before)**t1/(1+value_after)**t2-1
    
    @staticmethod    
    def calculate_discount_factor(yearfrac,interest_rate):
        return 1/(1+interest_rate)**yearfrac
    