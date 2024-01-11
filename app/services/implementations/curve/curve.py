import numpy as np
import pandas as pd
from app.services.interfaces.curve.Icurve import ICurve
from app.services.interfaces.core.Icore import ICore


class Curve(ICurve):
    
    def __init__(self,curve_name,start_date,end_date, core):
        self._curve_name = curve_name
        self._start_date = start_date
        self._end_date = end_date
        self._curve = self.get_data()
        self._core = core
        self._yearfrac = core.yearfrac(self._start_date,self._end_date)
    
    def get_data(self):
        pass
    
    def interpolate_curve(self, method = 'linear'):
        
        full_range = pd.date_range(start=self._start_date, end=self._end_date, freq='D')
        to_series = pd.Series(data=self._curve['values'], index=self._curve['dates'])
        full_series = to_series.reindex(full_range)
        
        if method == 'linear':
            full_series = full_series.interpolate()
        
        elif method == 'logarythmic':
            for date, value in full_series.iteritems():
                if pd.isna(value):
                    db, da, vb, va = self.__find_nearest_dates_values(full_series, date)
                    full_series.at[date] = self._core.logarithmic_interpolation(date, db, 
                                                                                da, vb, va)

        interpolated_dates = full_series.index.to_pydatetime()
        interpolated_values = full_series.values
            
        return interpolated_dates, interpolated_values
    
    def __find_nearest_dates_values(series, target_date):
        before = series[series.index < target_date].last_valid_index()
        after = series[series.index > target_date].first_valid_index()
        if before is None or after is None:
            return None, None, None, None  
        date_before, value_before = before, series[before]
        date_after, value_after = after, series[after]
        return date_before, date_after, value_before, value_after
