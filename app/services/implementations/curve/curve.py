from app.services.interfaces.curve.Icurve import ICurve

class Curve(ICurve):
    
    def __init__(self,curve_name,start_date,end_date):
        self._curve_name = curve_name
        self._start_date = start_date
        self._end_date = end_date
    
    def interpolate_curve(self):
        pass