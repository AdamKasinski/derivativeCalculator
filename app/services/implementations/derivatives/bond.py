import pandas as pd
import numpy as np
from datetime import date
from app.services.interfaces.derivatives.Ibond import IBond
from app.services.interfaces.core.Icore import Icore
import copy

class FVBond(IBond):

    def __init__(self, notional, start_date, end_date, leg, interest_rate, margin, frequency, type, float_leg_curve,schedule, curve_class):
        self._notional = notional
        self._start_date = start_date
        self._end_date = end_date
        self._leg = leg
        self._interest_rate = interest_rate
        self._margin = margin
        self._frequency = frequency
        self._type = type
        self._float_leg_curve = float_leg_curve
        self._schedule = schedule
        self._cashflows = self.__init_cashflows()
        self._generate_interest_rate = {
            'fixed': self.__generate_fixed,
            'float': self.__generate_float
        }
        self._curve_class = curve_class

    def __generate_fixed(self):
        return self.interest_rate

    def __generate_float(self):
        
        return self._curve_class.get_forward_rates(self.schedule,self.interest_rate)

    def __init_cashflows(self):
        cfs = copy.deepcopy(self.schedule)
        cfs['interest rate'] = []
        cfs['cashflows'] = []
        cfs['discount factor'] = []
        cfs['discounted cashflows'] = []
        return pd.DataFrame(cfs)

    def generate_cashflows(self):
        self._cashflows['interest rate'] = self._generate_interest_rate[self._interest_rate]()
        self._cashflows['cashflows'] = self._cashflows['interest rate']*self._notional*self._cashflows['yearfrac']
        self._cashflows['discounted factors'] = self._curve_class.generate_discount_factors(self._schedule['yearfracs'], self._schedule['interest rate'])
        self._cashflows['discounted cashflows'] = self._cashflows['discounted factors']*self._cashflows['cashflows']

    def valuate(self, valuation_date) -> float:
        return 2+2

    @property
    def schedule(self):
        return self._schedule
    
    @property
    def cashflows(self):
        return self._cashflows

    @property
    def notional(self) -> float:
        return self._notional

    @property
    def start_date(self) -> date:
        return self._start_date

    @property
    def end_date(self) -> date:
        return self._end_date

    @property
    def leg(self) -> str:
        return self._leg

    @property
    def interest_rate(self) -> float:
        return self._interest_rate

    @property
    def margin(self) -> float:
        return self._margin

    @property
    def frequency(self) -> str:
        return self._frequency

    @property
    def type(self) -> str:
        return self._type

    @property
    def float_leg_curve(self):
        return self._float_leg_curve
