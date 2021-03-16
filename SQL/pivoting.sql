select * from car_info;

select *
from
(select 
Manufacturer, Model, Sales_in_thousands, year_resale_value,price_in_thousands, Engine_size,Horsepower,Fuel_capacity,Fuel_efficiency,Latest_launch,power_perf_factor
from dbo.car_info )
As Car_model_info
pivot 
	(sum(Price_in_thousands)
	for  Manufacturer in ([Acura],[Audi],[BMW],[Buick],[Cadillac],[Chevrolet],[Chrysler],[Dodge],[Ford],[Honda],[Hyundai],[Infiniti],[Jaguar],[Jeep],[Lexus],[Lincoln],[Mitsubishi],[Mercury],[Mercedes-B],
	[Nissan],[Oldsmobile],[Plymouth],[Pontiac],
	[Porsche],[Saab],[Saturn],[Subaru],[Toyota],[Volkswagen],[Volvo]))
As car_manufacturer