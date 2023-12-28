import datetime
from services.implementations.Bond import Bond

b = Bond(10,1,1,1,1,1,1,1,1)

print(b.valuate(datetime.date(2020,12,21)))