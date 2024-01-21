import numpy as np
from app.services.core.core import Core
from app.services.curve.projection_curve import Projection_curve
from app.services.curve.historical_curve import Curve

# TODO: do not calculate discount factors and forward rates each time - save to database
class Projection_curve(Curve): 
    
    def __init__(self, curve_name, start_date, end_date):
        super().__init__(self,curve_name,start_date,end_date)
        self._yearfracs = self.__generate_yearfracs()
        self._discount_factors = self.generate_discount_factors(start_date)
        self._forward_rates = self.generate_forward_rates()

    def generate_discount_factors(self):
        return Core.calculate_discount_factor(self._yearfracs, self._curve['values'])

    def generate_forward_rates(self):
        forward_rates = np.zeros(np.size(self._curve['dates'][:-1])).dtype('float')
        for index, (date,value) in enumerate(self._curve['dates'][:-1],
                                             self._curve['values'][:-1]):
            date_after = self._curve['dates'][index+1]
            value_after = self._curve['values'][index+1]
            forward_rates[index] = Core.calculate_forward_rate(self._start_date, 
                                                                date, date_after,
                                                                value, value_after)
        return forward_rates
    
    def __generate_yearfracs(self):
        return Core.yearfrac(self._start_date,self._curve['dates'])
