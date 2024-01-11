import pandas as pd
import numpy as np
from app.services.interfaces.schedule.Ischedule import ISchedule

class Schedule(ISchedule):

    def __init__(self, start_date,end_date, frequency, valuation_date):
        self._start_date = start_date
        self._end_date = end_date
        self._frequency = frequency
        self._schedule = self.generate_schedule(self,valuation_date)

    
    def generate_schedule(self, valuation_date):
        full_schedule  = pd.date_range(self._start_date,self._end_date,freq=pd.DateOffset(months=self._frequency))
        current_start_date = full_schedule[full_schedule<valuation_date][-1]
        index = np.where(full_schedule == current_start_date)[0][0]
        start_dates = full_schedule[index:-1]
        end_dates = full_schedule[index+1:]
        self._schedule = start_dates, end_dates

    @property
    def schedule(self):
        return self._schedule    
 