#!/usr/bin/python

import sys
from datetime import datetime

start_date = datetime.strptime('01/01/2015/00:00', '%m/%d/%Y/%H:%M')
end_date = datetime.strptime('12/31/2015/00:00', '%m/%d/%Y/%H:%M')

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    result = line.split(",")
    date = result[0]
    time = result[1]
    if 'BOROUGH' not in result:
        date_time = datetime.strptime(date + "/" + time, '%m/%d/%Y/%H:%M')
        if date_time >= start_date and date_time <= end_date:
            value = ",".join(result[2:])
            print '%s\t%s' % (start_date, value)
        