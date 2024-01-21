import copy
import pandas as pd
import numpy as np
from datetime import date
from app.services.core.core import Core
from app.services.curve.curve import Curve
from app.services.curve.projection_curve import Projection_curve


class FVBond_pricing():
    
    def __init__(self,bond,historical_curve,projection_curve,valuation_date):
        self._valuation_date = valuation_date
        self._bond = bond
        self._historical_curve = historical_curve
        self._projection_curve = projection_curve
        self._generate_interest_rate = {
            'fixed': self.__generate_fixed,
            'float': self.__generate_float
        }
        self._cashflows = self.__init_cashflows()
        
    def generate_cashflows(self):
        self._cashflows['interest rate'] = self._generate_interest_rate[self._interest_rate]()
        self._cashflows['yearfracs'] = self.__generate_yearfracs()
        self._cashflows['cashflows'] = self.__calculate_cashflow()
        self._cashflows['discount factor'] = self.__get_discount_factors()
        self._cashflows['discounted cashflows'] = self.__discount_cashflows()
        
        
    def valuate(self) -> float:
        return 2+2
    
    
    def __generate_fixed(self):
        return self._bond.interest_rate

    def __generate_float(self):
        forward_rates =  self._projection_curve._forward_rates.where(
            self._projection_curve._curve['dates'] == self._bond.schedule['start_dates']
        )
        curr_interest_rate = self._historical_curve.curve['values'].where(
            self._historical_curve._curve['dates'] == self._bond.schedule['start_dates']
        )
        return np.insert(forward_rates,0,curr_interest_rate)

    def __init_cashflows(self):
        cfs = copy.deepcopy(self._bond.schedule)
        cfs['interest rate'] = []
        cfs['yearfracs'] = []
        cfs['cashflows'] = []
        cfs['discount factor'] = []
        cfs['discounted cashflows'] = []
        return pd.DataFrame(cfs)

    def __calculate_cashflow(self):
        return self._bond.notional*self._cfs['interest rate']*self._yearfracs
    
    def __get_discount_factors(self):
        pass
    
    def __discount_cashflows(self):
        pass
    
    def __generate_yearfracs(self):
        return Core.yearfrac(self._bond.schedule.schedule['start date'],
                              self._bond.schedule.schedule['end date'])