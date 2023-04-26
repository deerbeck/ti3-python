import os
import requests
import re
from datetime import datetime
from datetime import timedelta


class LfuBay:

    def __init__(self):
        self.__restrictedmetrics = ['NO2', 'PM10']
        self.__datadir = 'data/'
        try:
            os.mkdir(self.__datadir)
        except OSError as error:
            pass

    def available_data(self):
        filenames = os.listdir(self.__datadir)
        metricdata = [filename[:-4] for filename in filenames if 'csv' in filename]

        return metricdata

    def __parse(self, timestamp, value):
        date = ''
        time = ''
        try:
            date = timestamp.split(' ')[0]
            time = timestamp.split(' ')[1]
            # 24 h not accepted by python
            # flip to 0 h next day
            if time == '24:00':
                timestamp0 = datetime.strptime(date, '%d.%m.%Y')
                timestamp0 += timedelta(days=1)
                date = timestamp0.strftime('%d.%m.%Y')
                time = '00:00'
        except IndexError:
            pass

        try:
            # some invalid values are: #, ?
            value = float(value)
        except ValueError:
            value = None

        return [date, time, value]

    def metric_data(self, location, metric, start=2018, end=2021):
        all_data = []
        filenames = os.listdir(self.__datadir)
        metric_files = [filename for filename in filenames if metric in filename and filename[-3:] == 'csv']
        metric_files.sort()
        for file in metric_files:
            filedate = int(file.split('_')[1][:4])
            if start <= filedate <= end:
                filename = self.__datadir + file
                with open(filename, 'r', encoding='utf-8') as fp:
                    header = fp.readline().split(',')
                    loc_index = header.index(location)
                    # parse csv data and extract timestamp and location data
                    try:
                        # length filtering for proper date format
                        filtered_data = [self.__parse(line_[0], line_[loc_index]) for line_ in [line.strip().split(',') for line in fp.readlines()] if len(line_[0]) == 16]
                        all_data += filtered_data
                    except IndexError:
                        print('location not found')

        return all_data

    # extract all links in web page
    @staticmethod
    def __extract(content):
        html_tag_regex = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
        return [match[1] for match in html_tag_regex.findall(content)]

    def download_data(self, metric='NO2', start=2018, end=2021):
        # get web page content
        resp = requests.get('https://www.lfu.bayern.de/luft/immissionsmessungen/messwertarchiv/index.htm')
        if resp.status_code != 200:
            return -1

        # extract all links
        all_urls = LfuBay.__extract(resp.text)
        # filter for metric
        urls = [link for link in all_urls if metric in link]

        # download file and conversion of xlsx to csv
        import pandas as pd
        for url in urls:
            download_url = url
            index = download_url.rfind('/')
            filename = download_url[index+1:]
            filedate = int(filename.split('_')[1][:4])
            if start <= filedate <= end:
                online_file = requests.get(download_url, allow_redirects=True)
                fq_filename = self.__datadir + filename
                # only download if file doesn't exist
                if os.path.exists(fq_filename[:-4] + 'csv'):
                    continue

                with open(fq_filename, 'wb') as f:
                    f.write(online_file.content)

                # conversion
                # header=1 for data before 2021_01
                # header=2 for data after 2021_01
                hid = 2
                # 25.04.2023
                # Header format changed for >=2022
                # year = datetime.now().date().year
                if filedate < 2022:
                    hid=1
                read_file = pd.read_excel(fq_filename, header=hid)
                #tmp = read_file[['Zeitpunkt', 'München/Lothstraße']]
                read_file.to_csv(fq_filename[:-4] + 'csv', index=None, header=True)

                # delete xlsx
                os.remove(fq_filename)

        return 0


if __name__ == '__main__':
    lfu = LfuBay()
    result = lfu.download_data('NO2', 2012, 2022)
    print(f'NO2 Download result: {result}')
    result = lfu.download_data('PM10', 2012, 2022)
    print(f'PM10 Download result: {result}')
    no2data = lfu.metric_data('München/Lothstraße', 'NO2')
    print(f'NO2-Data: {len(no2data)}')
    pm10data = lfu.metric_data('München/Lothstraße', 'PM10')
    print(f'PM10-Data: {len(pm10data)}')

