from v3_util import check_time
import lfubay

# Task 1: Reading in the measured values


def read_data(location, val_name):
    # read in data with the gifen lfubay function
    lfu = lfubay.LfuBay()
    data = lfu.metric_data(location, val_name)

    # using this method you get a result approx (0:00:00.027134 - 0:00:00.005667) = 0.021467 ms faster results (and can use 1 line of code)
    # assign date time and val_name keys to the given values in one line of code
    data_dict = {'date': [row[0] for row in data], 'time': [
        row[1] for row in data], val_name: [row[2] for row in data]}

    return data_dict

# Task 2: Typical characteristics of the measurements


def stats(table, val_name):
    # clean up list from any None Values with filter function and lambda function (Every entry will be allowed that is not None)
    values = list(filter(lambda x: x != None, table[val_name]))

    # return asked tuple in the form of (number of entries, minimum, maximum, mean)
    return (len(values), min(values), max(values), sum(values)/len(values))


# Task 3: Preparing the merging of two measured value tables


def add_entry(table, d, t, val_name0, val_name1, val0, val1):
    # add date and time entry to given table dictionary
    table['date'].append(d)
    table['time'].append(t)

    # add corresponding value names and add nothing if val = None
    table[val_name0].append(val0)
    table[val_name1].append(val1)

# Task 5: Merging both measurements into one table

def merge(data0, data1):
    # get measuredata names from data_dicts with xor operator
    val_name0, val_name1 = sorted(list(data0.keys() ^ data1.keys()))
    # create initial merged_dict with needed keys and lists to be filled
    merged = {'date': [], 'time': [], val_name0: [], val_name1: []}

    # set starting index for merge-algorithm
    curr_ndx0 = 0
    curr_ndx1 = 0

    while(True):
        try:
            time_val = check_time(data0, data1, curr_ndx0, curr_ndx1)
            # loop through indizes and check_time of entry if 'timestamps' are identical add data to merged_dict with add_entry funtcion
            if time_val == 0:
                #add entry using helpfunction
                add_entry(merged, data0['date'][curr_ndx0], data0['time'][curr_ndx0], val_name0=val_name0,
                          val_name1=val_name1, val0=data0[val_name0][curr_ndx0], val1=data1[val_name1][curr_ndx0])
                #count up each index given definition of merge algorithm
                curr_ndx1 += 1
                curr_ndx0 += 1

            elif time_val == -1:
                # only add entry of data0 because it has earlier the earlier timestamp Use None for val1 to append "nothing"
                add_entry(merged, data0['date'][curr_ndx0], data0['time'][curr_ndx0],
                          val_name0=val_name0, val_name1=val_name1, val0=data0[val_name0][curr_ndx0], val1=[])
                # only count up index0
                curr_ndx0 += 1

            elif time_val == 1:
                # only add entry of data1 because it has earlier the earlier timestamp Use None for val0 to append "nothing"
                add_entry(merged, data1['date'][curr_ndx1], data1['time'][curr_ndx1],
                          val_name0=val_name0, val_name1=val_name1, val0=None, val1=data1[val_name1][curr_ndx0])
                # only count up index1
                curr_ndx1 += 1

                # when 'timestamps' are not identical use the return value of check_time to correct wrong index
        # use EAFP to get out of algorithm when all data of one of the data sets is reached
        except IndexError:
               # add left over measurement data
            if curr_ndx0 < len(data0[val_name0]):
                #add remaining entries of left over data0
                add_entry(merged, data0['date'][curr_ndx0], data0['time'][curr_ndx0], val_name0=val_name0,
                          val_name1=val_name1, val0=data0[val_name0][curr_ndx0:], val1=None)
            elif curr_ndx1 < len(data1[val_name1]):
                #add remaining entries of left over data1
                add_entry(merged, data1['date'][curr_ndx1], data1['time'][curr_ndx1], val_name0=val_name0,
                          val_name1=val_name1, val0=None, val1=data1[val_name1][curr_ndx1:])
            break
        # add left over measurement data
    return merged


# Task 6: Evaluate NO2 limit values
def no2_stats(table, year):
    # NO2 limit #1
    data = [[table['date'][i], table['time'][i], table['NO2'][i]] for i, val in enumerate(
        table['date']) if str(year) in val and table['NO2'][i] is not None]
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
    three_hourly_avg_gen = (hourly_avg[i:i+sliding_window_size]
                            for i in range(len(hourly_avg) - sliding_window_size + 1))
    for tha in three_hourly_avg_gen:
        limit_exceed = [i for i in tha if i >= 400.0]
        if len(limit_exceed) == sliding_window_size:
            alarm_limit += 1

    return anual_avg, hourly_avg_count, alarm_limit, min_, max_


if __name__ == '__main__':
    # Task 1: Reading in NO2 and PM10 data
    tab_no2 = read_data('München/Lothstraße', 'NO2')
    tab_pm10 = read_data('München/Lothstraße', 'PM10')

    # Task 2: Output of characteristic data
    print("NO2: Anzahl der Messdaten: {}, Minimum: {}, Maximum: {}, Durchschnitt: {}".format(stats(
        tab_no2, "NO2")[0], stats(tab_no2, "NO2")[1], stats(tab_no2, "NO2")[2], stats(tab_no2, "NO2")[3]))
    print("PM10: Anzahl der Messdaten: {}, Minimum: {}, Maximum: {}, Durchschnitt: {}".format(stats(
        tab_pm10, "PM10")[0], stats(tab_pm10, "PM10")[1], stats(tab_pm10, "PM10")[2], stats(tab_pm10, "PM10")[3]))

    # Task 3: Test add_entry
    #creaty dummy dict and add dummy entries
    weather = {'date': [], 'time': [], 'temp': [], 'hygro': []}
    add_entry(weather, '22.11.2019', '8:15', 'temp', 'hygro', '5.5', '54')
    add_entry(weather, '23.11.2019', '8:15', 'temp', 'hygro', '6.0', None)
    add_entry(weather, '24.11.2019', '8:15', 'temp', 'hygro', '6.4', '65')
    print(weather)

    # Task 4 (check_time is in v3_util), Compare indexes
    # check dict to get used to check_times
    print(check_time(tab_no2, tab_pm10, 100, 100))
    print(check_time(tab_no2, tab_pm10, 100, 98))
    print(check_time(tab_no2, tab_pm10, 98, 100))

    # Task 5: Merging the dictionaries
    # merging both data dicts
    merge(tab_no2, tab_pm10)

    # Task 6: Output results to console and file

    # print out year average to console
    for year in range(2018, 2022):
        print("{}: {}".format(year, no2_stats(tab_no2, year)))

    # write data into .csv file
    with open("Auswertung_NO2_München_Lothstraße_2018-2021.csv", "w") as file:
        file.write(
            "Jahr;Jährlicher Durchschnitt;Verletzungen Einstundenmittel;Verletzungen 3 Einstundenmittel;Minimum;Maximum\n")
        #loop through years and get each no2_stats
        for year in range(2018, 2022):
            #store stats in buffer list to easily modify
            buffer = [str(e) for e in no2_stats(tab_no2, year)]
            #format string on first entry to only 3 significant places
            buffer[0] = f"{float(buffer[0]):.3f}"
            #write each line using string formating and joining into csv file
            file.write(f"{year};" + ";".join(buffer) + "\n")