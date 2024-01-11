from app.services.interfaces.curve.Iprojection_curve import IProjection_curve
from app.services.implementations.curve.historical_curve import Curve

class Projection_curve(Curve, IProjection_curve):
    
    def __init__(self, curve_name, start_date, end_date):
        super().__init__(curve_name,start_date,end_date)

    def generate_forward_rates(self):
        pass

    def generate_discount_factors(self):
        pass