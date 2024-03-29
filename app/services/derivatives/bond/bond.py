
from datetime import date

class FVBond():

    def __init__(self, notional, start_date, end_date, leg, interest_rate, 
                 margin, frequency, type, float_leg_curve,schedule):
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
