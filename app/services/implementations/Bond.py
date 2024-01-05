import pandas as pd
import numpy as np

from datetime import date
from services.interfaces.Ibond import IBond


class FVBond(IBond):
    def __init__(self, notional, start_date, end_date, leg, interest_rate, margin, frequency, type, float_leg_curve,schedule):
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


    def generate_schedule(self, valuation_date):
        return 2+2
    
    def generate_cashflow(self, valuation_date):
        return 2+2

    def valuate(self, valuation_date) -> float:
        return 2+2

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        self._schedule = schedule

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
