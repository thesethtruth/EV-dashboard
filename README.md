# EV-dashboard
Data browsing dashboard based on Dash, based on early version of the WB thesis energy model (27-01-2021).

 Data browsed is based on hourly timeseries, weekly totals and PI of every solution. Achieved using 2 DOFs, chargers and batterysize. 
 + Chargers = [ 1 : 1 : 4 ]
 + Batterysize = [ 0 : 100 : 2000 ]
 [ min : step : max ] (including min and max)
 
Solutions space of 4 by 21 discrete points, thus 84 unique solutions. 
 
 1. Wind generation based on actual turbine 90 kW production scaled to desired size. [private]
 2. PV power based on TMY irradiation from PVGIS, converted to POA using isotropic conversion from PVLIB. 
 (https://re.jrc.ec.europa.eu/)
 3. EV charging behavior generated through stochastic filtering of real life traffic data to estimate SOC of passing vehicles. 
 (http://indicatoren.verkeerscentrum.be/)
 4. Petrol station consumption based on scale industrial power profile supplied by NEDU 
 (https://www.nedu.nl/documenten/verbruiksprofielen/)
 5. Costs estimated per expert consult
 6. Simple battery control. 
 7. Merit order balance. 
 8. Limmited grid capacity. 
