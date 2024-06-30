date_cols = ['Year', 'Quarter', 'Month', 'DayofMonth', 'DayOfWeek', 'FlightDate']
flight_info_cols = ['Reporting_Airline', 'Airline_Name', 'Tail_Number', 'Flight_Number_Reporting_Airline', 'Flight_Id']
origin_cols = ['OriginAirportID', 'Origin', 'OriginCityName', 'OriginState', 'OriginStateName']
dest_cols = ['DestAirportID', 'Dest', 'DestCityName', 'DestState', 'DestStateName']
dep_cols = ['CRSDepTime', 'DepTime', 'DepDelay', 'DepDelayMinutes', 'DepDel15', 'DepartureDelayGroups']
taxi_cols = ['TaxiOut', 'WheelsOff', 'WheelsOn', 'TaxiIn']
arr_cols = ['CRSArrTime', 'ArrTime', 'ArrDelay', 'ArrDelayMinutes', 'ArrDel15', 'ArrivalDelayGroups']
time_cols = ['CRSDepTime', 'DepTime', 'CRSArrTime', 'ArrTime']
cancel_cols = ['Cancelled', 'CancellationCode', 'Diverted']
sum_cols = ['Distance', 'DistanceGroup', 'CRSElapsedTime', 'ActualElapsedTime']
delay_cols = ['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
dev_cols = ['FirstDepTime', 'TotalAddGTime', 'LongestAddGTime', 'DivAirportLandings', 'DivReachedDest', 'DivActualElapsedTime', 'DivArrDelay', 'DivDistance', 'Div1Airport', 'Div1AirportID', 'Div1WheelsOn', 'Div1TotalGTime', 'Div1LongestGTime', 'Div1WheelsOff', 'Div1TailNum', 'Div2Airport', 'Div2AirportID', 'Div2WheelsOn', 'Div2TotalGTime', 'Div2LongestGTime', 'Div2WheelsOff', 'Div2TailNum', 'Div3Airport', 'Div3AirportID', 'Div3WheelsOn', 'Div3TotalGTime', 'Div3LongestGTime', 'Div3WheelsOff', 'Div3TailNum', 'Div4Airport', 'Div4AirportID', 'Div4WheelsOn', 'Div4TotalGTime', 'Div4LongestGTime', 'Div4WheelsOff', 'Div4TailNum', 'Div5Airport', 'Div5AirportID', 'Div5WheelsOn', 'Div5TotalGTime', 'Div5LongestGTime', 'Div5WheelsOff', 'Div5TailNum']
base_cols = ['Year', 'Quarter', 'Month', 'DayofMonth', 'DayOfWeek', 'FlightDate', 'Reporting_Airline', 'Tail_Number', 'Flight_Number_Reporting_Airline', 'OriginAirportID', 'Origin', 'OriginCityName', 'OriginState', 'OriginStateName', 'DestAirportID', 'Dest', 'DestCityName', 'DestState', 'DestStateName', 'CRSDepTime', 'DepTime', 'DepDelay', 'DepDelayMinutes', 'DepDel15', 'DepartureDelayGroups', 'TaxiOut', 'WheelsOff', 'WheelsOn', 'TaxiIn', 'CRSArrTime', 'ArrTime', 'ArrDelay', 'ArrDelayMinutes', 'ArrDel15', 'ArrivalDelayGroups', 'Cancelled', 'CancellationCode', 'Diverted', 'CRSElapsedTime', 'ActualElapsedTime', 'AirTime', 'Flights', 'Distance', 'DistanceGroup', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']
time_loc_cols = ['Origin', 'CRSDepTime', 'DepTime', 'Dest', 'CRSArrTime', 'ArrTime']
utc_cols = ['CRSDepTime_UTC', 'DepTime_UTC', 'CRSArrTime_UTC', 'ArrTime_UTC']
