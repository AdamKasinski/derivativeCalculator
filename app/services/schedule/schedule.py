import pandas as pd
import numpy as np
from services.core.core import Core


class Schedule():

    def __init__(self, start_date, end_date, frequency, valuation_date):
        self._start_date = start_date
        self._end_date = end_date
        self._frequency = frequency
        self._valuation_date = valuation_date
        self._schedule = self.__generate_schedule()

    
    def __generate_schedule(self):
        schedule = dict()
        full_schedule  = Core.generate_date_range(self._start_date,self._end_date,
                                                  self._frequency)
        current_start_date = full_schedule[full_schedule<self._valuation_date][-1]
        index = np.where(full_schedule == current_start_date)[0][0]
        start_dates = full_schedule[index:-1]
        end_dates = full_schedule[index+1:]
        schedule['start_dates'] = start_dates 
        schedule['end_dates'] = end_dates
        return schedule

    @property
    def schedule(self):
        return self._schedule    
 