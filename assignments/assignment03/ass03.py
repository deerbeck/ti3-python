from v3_util import check_time
import lfubay

# Aufgabe 1: Einlesen der Messwerte
def read_data(location, val_name):
	#read in data with the gifen lfubay function
	lfu = lfubay.LfuBay()
	data = lfu.metric_data(location, val_name)

	#assign date time and val_name keys to the given values in one line of code
	data_dict = {'date': [row[0] for row in data], 'time': [row[1] for row in data], val_name : [row[2] for row in data]}

	return data_dict

# Aufgabe 2: Typische Kenndaten der Messungen


# Aufgabe 3: Vorbereitung der Zusammenführung zweier Messwerttabellen


# Aufgabe 5: Zusammenführen beider Messungen zu einer Tabelle


# Aufgabe 6: NO2 Grenzwerte auswerten
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
	# Aufgabe 1: Einlesen der NO2 und PM10 Daten
	tab_no2 = read_data('München/Lothstraße', 'NO2')
	tab_pm10 = read_data('München/Lothstraße', 'PM10')
	print("Test")

	# Aufgabe 2: Ausgabe der Kenndaten


	# Aufgabe 3: Test von add_entry


	# Aufgabe 4 (check_time ist in v3_util), Vergleiche Indizes


	# Aufgabe 5: Zusammenführen der Dictionaries


	# Aufgabe 6: Ergebnisse auf Konsole und in Datei ausgeben





