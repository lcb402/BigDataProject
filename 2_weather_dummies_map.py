import sys
import numpy as np
from datetime import datetime
import pytz
from astral import Astral

a = Astral()
city = a['New York'] 
rush_hour = range(7,10) + range(17,20)


for line in sys.stdin:
    line = line.strip().split(',')
    if line[1] != 'date':
        speed = line[2]
        if speed == '*** ':
            speed = np.nan
        speed = float(speed)
        if speed > 25.0:
            excess_speed = 1
        else:
            excess_speed = 0
        date = line[1]
        datetime = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
        sun_date = pytz.timezone('US/Central').localize(datetime)
        sun = city.sun(date=sun_date, local=True)
        if sun_date >= sun['dusk'] or sun_date <= sun['dawn']:
            dark = 1.0
        else:
            dark = 0.0
        day = datetime.weekday()
        if day == 0 or day == 6:
            weekend = 1.0
        else:
            weekend = 0.0
        time = datetime.time()
        hour = int(time.hour)
        if hour in rush_hour:
            rush = 1.0
        else:
            rush = 0.0
        sky = line[3]
        if sky == '***':
            sky = np.nan
        visib = line[4]
        if visib == '****' or visib == '***':
            visib = np.nan
        visib = float(visib)
        if visib < 1.0:
            bad_visib = 1
        else:
            bad_visib = 0
        temp = line[5]
        if temp == '****':
            temp = np.nan
        temp = float(temp)
        dew = line[6]
        if dew == ' ****':
            dew = np.nan
        dew = float(dew)
        sea = line[7]
        if sea == '******' or sea == ' *****':
            sea = np.nan
        sea = float(sea)
        precip1,precip6,precip24 = line[8:11]
        if precip1 == '*****':
            precip1 = precip6
        if precip1 == '*****':
            precip1 = precip24
        if precip1 == '*****':
            precip1 = np.nan
        if precip1 > 0.0:
            precip1 = 1
        else:
            precip1 = 0
        precip1 = float(precip1)
        snow = line[11]
        if snow == '**' or snow == ' *':
            if temp > 35.0:
                snow = 0.0
            elif precip1 == 0:
                snow = 0.0
            elif precip1 == 1:
                snow = 1.0
            else:
                snow = np.nan
        snow = float(snow)
        if temp < 85 and temp > 55 and precip1 == 0 and bad_visib == 0 and excess_speed == 0:
            temperate = 1.0
        else:
            temperate = 0.0
        print '%s,%f,%s,%f,%f,%f,%f,%f,%f,%d,%d,%d,%d,%d,%d' % (date, speed, sky, visib,
                                             temp, dew, sea, precip1, snow, excess_speed,
                                                            dark, weekend, rush, bad_visib, temperate)

