import pandas as pd
import numpy as np
from services.interfaces.Ischedule import ISchedule

class Schedule(ISchedule):

    def __init__(self, start_date,end_date, frequency):
        self._start_date = start_date
        self._end_date = end_date
        self._frequency = frequency

    
    def generate_schedule(self, valuation_date):
        full_schedule  = pd.date_range(self.start_date,self.end_date,freq=pd.DateOffset(months=self.frequency))
        current_start_date = full_schedule[full_schedule<valuation_date][-1]
        index = np.where(full_schedule == current_start_date)[0][0]
        start_dates = full_schedule[index:-1]
        end_dates = full_schedule[index+1:]
        return start_dates

    @property
    def frequency(self):
        return self._frequency
    
