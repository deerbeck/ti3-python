from v3_util import check_time
import lfubay
import numpy as np

# Task 1: Reading in the measured values
def read_data(location, val_name):
	#read in data with the gifen lfubay function
	lfu = lfubay.LfuBay()
	data = lfu.metric_data(location, val_name)

	#assign date time and val_name keys to the given values in one line of code
	data_dict = {'date': [row[0] for row in data], 'time': [row[1] for row in data], val_name : [row[2] for row in data]}

	return data_dict

# Task 2: Typical characteristics of the measurements
def stats(table, val_name):
	#clean up list from any None Values with filter function and lambda function (Every entry will be allowed that is not None)
	values = list(filter(lambda x: x != None, table[val_name]))

	#return asked tuple in the form of (number of entries, minimum, maximum, mean)
	return (len(values), min(values), max(values), sum(values)/len(values))
	

# Task 3: Preparing the merging of two measured value tables


# Task 5: Merging both measurements into one table


# Task 6: Evaluate NO2 limit values
def no2_stats(table, year):
	# NO2 limit #1
	data = [[table['date'][i], table['time'][i], table['NO2'][i]] for i,val in enumerate(table['date']) if str(year) in val and table['NO2'][i] is not None]
	hourly_avg = [c for (a, b, c) in data]
	anual_avg = sum(hourly_avg) / len(hourly_avg)

	# additional data
	min_ = min(hourly_avg)
	max_ = max(hourly_avg)

	# NO2 limit #2
	hourly_avg = [value[2] for value in data if value[2] >= 200.0]
	hourly_avg_count = len(hourly_avg)

	# NO2 limit #3
	alarm_limit = 0
	sliding_window_size = 3
	hourly_avg = [value for value in table['NO2'] if value is not None]
	three_hourly_avg_gen = (hourly_avg[i:i+sliding_window_size] for i in range(len(hourly_avg) - sliding_window_size + 1))
	for tha in three_hourly_avg_gen:
		limit_exceed = [i for i in tha if i >= 400.0]
		if len(limit_exceed) == sliding_window_size:
			alarm_limit += 1

	return anual_avg, hourly_avg_count, alarm_limit, min_, max_


if __name__=='__main__':
	# Task 1: Reading in NO2 and PM10 data
	tab_no2 = read_data('München/Lothstraße', 'NO2')
	tab_pm10 = read_data('München/Lothstraße', 'PM10')
	print("Test")

	# Task 2: Output of characteristic data
	#print("NO2: Anzahl der Messdaten: {}, Minimum: {}, Maximum: {}, Durchschnitt: {}".format(stats(tab_no2, "NO2")[0], stats(tab_no2, "NO2")[1], stats(tab_no2, "NO2")[2], stats(tab_no2, "NO2")[3]))
	print("PM10: Anzahl der Messdaten: {}, Minimum: {}, Maximum: {}, Durchschnitt: {}".format(stats(tab_pm10, "PM10")[0], stats(tab_pm10, "PM10")[1], stats(tab_pm10, "PM10")[2], stats(tab_pm10, "PM10")[3]))
	# Task 3: Test add_entry


	# Task 4 (check_time is in v3_util), Compare indexes


	# Task 5: Merging the dictionaries


	# Task 6: Output results to console and file





