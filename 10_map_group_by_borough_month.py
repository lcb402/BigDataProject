#!/usr/bin/python

import sys
from datetime import datetime
import datetime as dt

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    result = line.split(",")
    date = result[0]
    borough = result[1]
    if 'borough' not in result:
        date = datetime.strptime(date, '%m/%d/%Y %H:%M')
        month = date.month
        print '%s\t%d' % (borough, month)
