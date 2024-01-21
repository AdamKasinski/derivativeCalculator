import numpy as np
from dateutil.relativedelta import relativedelta

class Core():

    @staticmethod
    def generate_date_range(start,end,freq):
        dates = []
        curr = start
        while curr < end:
            dates.append(curr)
            curr += relativedelta(months=freq)    
        if curr == end:
            dates.append(end)
        else:
            end_to_next_len = Core.yearfrac(end,curr)
            end_to_last_len = Core.yearfrac(end,dates[-1])
            
            if end_to_next_len < end_to_last_len:
                dates.append(end)
            else:
                dates[-1] = end
    
        return np.array(dates)
    
    @staticmethod
    def yearfrac(earlier_date, later_date):
        return (later_date-earlier_date).days/365

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
    def calculate_discount_factor(yearfrac,discount_rate):
        return 1/(1+discount_rate)**yearfrac
    