from decimal import Decimal, getcontext

getcontext().prec=100
for k in range(100):

	print sum(1/Decimal(16)**k * 
          	(Decimal(4)/(8*k+1) - 
           	Decimal(2)/(8*k+4) - 
           	Decimal(1)/(8*k+5) -
           	Decimal(1)/(8*k+6)))